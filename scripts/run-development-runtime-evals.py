#!/usr/bin/env python3
"""Run development capability runtime certification scenarios."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "development"
SCENARIOS = EVALS / "scenarios"
RUNS = EVALS / "runs"
CERTIFICATION = EVALS / "certification.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def scenario_paths(selected: list[str]) -> list[Path]:
    cert = load_json(CERTIFICATION)
    capabilities = cert["capabilities"]
    selected_set = set(selected)
    paths = []
    for capability in capabilities:
        cid = capability["id"]
        if selected_set and cid not in selected_set:
            continue
        paths.append(SCENARIOS / f"{cid}.json")
    missing = selected_set - {path.stem for path in paths}
    if missing:
        raise SystemExit(f"unknown capability id(s): {', '.join(sorted(missing))}")
    return paths


def render_prompt(scenario: dict) -> str:
    lines = [
        f"# Development Runtime Eval: {scenario['title']}",
        "",
        "Respond as the golden workflow system using specialist hats only inside scope.",
        "",
        "## Prompt",
        "",
        scenario["prompt"],
        "",
        "## Required Behaviors",
        "",
    ]
    lines.extend(f"- {item}" for item in scenario["required_behaviors"])
    lines.extend(["", "## Forbidden Behaviors", ""])
    lines.extend(f"- {item}" for item in scenario["forbidden_behaviors"])
    lines.append("")
    return "\n".join(lines)


def read_response(
    scenario_id: str,
    prompt_path: Path,
    responses_dir: Path | None,
    command: str | None,
    run_id: str,
) -> tuple[str, str, bool]:
    if responses_dir:
        path = responses_dir / f"{scenario_id}.md"
        if not path.exists():
            raise SystemExit(f"missing recorded response: {path}")
        return path.read_text(), f"recorded:{path}", False
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
        return response, f"command:{command}", completed.returncode != 0
    path = EVALS / "reference-responses" / run_id / f"{scenario_id}.md"
    if not path.exists():
        raise SystemExit(f"missing reference response: {path}")
    return path.read_text(), f"reference:{path}", False


def score_response(scenario: dict, rubric: dict, response: str, pending: bool, source: str) -> dict:
    response_lower = response.lower()
    score = 0
    max_score = 0
    criteria = []
    for criterion in rubric["criteria"]:
        max_score += criterion["weight"]
        missing_terms = [
            term for term in criterion["required_terms"] if term.lower() not in response_lower
        ]
        passed = not pending and not missing_terms
        if passed:
            score += criterion["weight"]
        criteria.append(
            {
                "id": criterion["id"],
                "description": criterion["description"],
                "weight": criterion["weight"],
                "passed": passed,
                "missing_terms": missing_terms,
            }
        )
    forbidden_violations = [
        term for term in rubric["forbidden_terms"] if term.lower() in response_lower
    ]
    passed = not pending and not forbidden_violations and score >= rubric["minimum_score"]
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
        "criteria": criteria,
        "forbidden_violations": forbidden_violations,
    }


def write_summary(run_dir: Path, scores: list[dict]) -> None:
    lines = [
        "# Development Runtime Eval Summary",
        "",
        f"Run: `{run_dir.name}`",
        f"Scenarios: {len(scores)}",
        f"Passed: {sum(1 for score in scores if score['passed'])}",
        f"Pending: {sum(1 for score in scores if score['pending'])}",
        "",
        "| Scenario | Score | Status |",
        "| --- | ---: | --- |",
    ]
    for score in scores:
        status = "PENDING" if score["pending"] else "PASS" if score["passed"] else "FAIL"
        lines.append(f"| `{score['scenario_id']}` | {score['score']}/{score['max_score']} | {status} |")
    lines.append("")
    run_dir.joinpath("summary.md").write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capability", nargs="*", help="capability id(s) to run")
    parser.add_argument("--run-id", default="development-capabilities-v1")
    parser.add_argument("--responses", type=Path)
    parser.add_argument("--command")
    args = parser.parse_args()

    run_dir = RUNS / args.run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    scores = []
    for scenario_path in scenario_paths(args.capability):
        scenario = load_json(scenario_path)
        rubric = load_json((scenario_path.parent / scenario["rubric"]).resolve())
        scenario_dir = run_dir / scenario["id"]
        scenario_dir.mkdir()
        prompt_path = scenario_dir / "prompt.md"
        prompt_path.write_text(render_prompt(scenario))
        response, source, pending = read_response(
            scenario["id"], prompt_path, args.responses, args.command, args.run_id
        )
        scenario_dir.joinpath("response.md").write_text(response)
        score = score_response(scenario, rubric, response, pending, source)
        scenario_dir.joinpath("score.json").write_text(json.dumps(score, indent=2) + "\n")
        scores.append(score)
    write_summary(run_dir, scores)
    print(f"wrote development runtime eval run: {run_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
