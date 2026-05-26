#!/usr/bin/env python3
"""Run or assemble runtime evaluation artifacts for golden scenarios."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evals" / "scenarios"
RUNS = ROOT / "evals" / "runs"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def scenario_files(selected: list[str]) -> list[Path]:
    files = sorted(SCENARIOS.glob("*.json"))
    if not selected:
        return files
    selected_set = set(selected)
    matched = [path for path in files if path.stem in selected_set]
    missing = selected_set - {path.stem for path in matched}
    if missing:
        raise SystemExit(f"unknown scenario id(s): {', '.join(sorted(missing))}")
    return matched


def render_prompt(scenario: dict) -> str:
    lines = [
        f"# Runtime Eval: {scenario['title']}",
        "",
        "You are running a golden-skill-sets runtime scenario.",
        "Respond as the active agent setup would in a real coding session.",
        "",
        "## User Prompt",
        "",
        scenario["prompt"],
        "",
        "## Expected Skills",
        "",
    ]
    lines.extend(f"- `{skill}`" for skill in scenario["expected_skills"])
    lines.extend(
        [
            "",
            "## Required Behaviors",
            "",
        ]
    )
    lines.extend(f"- {behavior}" for behavior in scenario["required_behaviors"])
    lines.extend(
        [
            "",
            "## Forbidden Behaviors",
            "",
        ]
    )
    lines.extend(f"- {behavior}" for behavior in scenario["forbidden_behaviors"])
    lines.append("")
    return "\n".join(lines)


def read_response(
    scenario_id: str,
    prompt_path: Path,
    responses_dir: Path | None,
    command: str | None,
    dry_run: bool,
) -> tuple[str, str, bool]:
    if responses_dir:
        response_path = responses_dir / f"{scenario_id}.md"
        if not response_path.exists():
            raise SystemExit(f"missing recorded response: {response_path}")
        return response_path.read_text(), f"recorded:{response_path}", False

    if command:
        command_text = command.format(
            prompt_file=shlex.quote(str(prompt_path)),
            scenario_id=shlex.quote(scenario_id),
        )
        completed = subprocess.run(
            command_text,
            cwd=ROOT,
            shell=True,
            text=True,
            capture_output=True,
            check=False,
        )
        response = completed.stdout
        if completed.stderr:
            response += "\n\n## Command stderr\n\n```text\n" + completed.stderr + "\n```\n"
        if completed.returncode != 0:
            response += f"\n\nCommand exited with status {completed.returncode}.\n"
        return response, f"command:{command}", completed.returncode != 0

    if dry_run:
        return (
            "PENDING: paste or generate a runtime response for this scenario, then rerun scoring.",
            "dry-run",
            True,
        )

    raise SystemExit("provide --responses, --command, or --dry-run")


def score_response(scenario: dict, rubric: dict, response: str, pending: bool, source: str) -> dict:
    response_lower = response.lower()
    criteria_results = []
    score = 0
    max_score = 0

    for criterion in rubric["criteria"]:
        weight = criterion["weight"]
        max_score += weight
        missing_terms = [
            term for term in criterion["required_terms"] if term.lower() not in response_lower
        ]
        passed = not missing_terms and not pending
        if passed:
            score += weight
        criteria_results.append(
            {
                "id": criterion["id"],
                "description": criterion["description"],
                "weight": weight,
                "passed": passed,
                "missing_terms": missing_terms,
            }
        )

    forbidden_violations = [
        term for term in rubric.get("forbidden_terms", []) if term.lower() in response_lower
    ]
    passed = (
        not pending
        and not forbidden_violations
        and score >= rubric["minimum_score"]
    )

    return {
        "scenario_id": scenario["id"],
        "title": scenario["title"],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "response_source": source,
        "pending": pending,
        "score": score,
        "max_score": max_score,
        "minimum_score": rubric["minimum_score"],
        "passed": passed,
        "criteria": criteria_results,
        "forbidden_violations": forbidden_violations,
    }


def write_summary(run_dir: Path, scores: list[dict]) -> None:
    passed = sum(1 for score in scores if score["passed"])
    pending = sum(1 for score in scores if score["pending"])
    lines = [
        "# Runtime Eval Summary",
        "",
        f"Run: `{run_dir.name}`",
        f"Scenarios: {len(scores)}",
        f"Passed: {passed}",
        f"Pending: {pending}",
        "",
        "| Scenario | Score | Status | Forbidden Violations |",
        "| --- | ---: | --- | --- |",
    ]
    for score in scores:
        if score["pending"]:
            status = "PENDING"
        elif score["passed"]:
            status = "PASS"
        else:
            status = "FAIL"
        violations = ", ".join(score["forbidden_violations"]) or "-"
        lines.append(
            f"| `{score['scenario_id']}` | {score['score']}/{score['max_score']} | {status} | {violations} |"
        )
    lines.append("")
    run_dir.joinpath("summary.md").write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", nargs="*", help="scenario id(s) to run")
    parser.add_argument("--run-id", help="custom run directory name")
    parser.add_argument("--responses", type=Path, help="directory of <scenario-id>.md responses")
    parser.add_argument(
        "--command",
        help="shell command template that prints a response; supports {prompt_file} and {scenario_id}",
    )
    parser.add_argument("--dry-run", action="store_true", help="write pending artifacts only")
    args = parser.parse_args()

    run_id = args.run_id or dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    scores: list[dict] = []
    for scenario_path in scenario_files(args.scenario):
        scenario = load_json(scenario_path)
        rubric = load_json((scenario_path.parent / scenario["rubric"]).resolve())
        scenario_dir = run_dir / scenario["id"]
        scenario_dir.mkdir()

        prompt_path = scenario_dir / "prompt.md"
        prompt_path.write_text(render_prompt(scenario))

        response, source, pending = read_response(
            scenario["id"],
            prompt_path,
            args.responses,
            args.command,
            args.dry_run,
        )
        scenario_dir.joinpath("response.md").write_text(response)

        score = score_response(scenario, rubric, response, pending, source)
        scenario_dir.joinpath("score.json").write_text(json.dumps(score, indent=2) + "\n")
        scores.append(score)

    write_summary(run_dir, scores)
    print(f"wrote runtime eval run: {run_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
