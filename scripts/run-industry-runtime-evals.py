#!/usr/bin/env python3
"""Run or assemble runtime artifacts for industry certification scenarios."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "industries"
SCENARIOS = EVALS / "scenarios"
RUNS = EVALS / "runs"
REFERENCE_RESPONSES = EVALS / "reference-responses" / "trust-heavy-v1"
CERTIFICATION = EVALS / "certification.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def scenario_paths(selected: list[str]) -> list[Path]:
    cert = load_json(CERTIFICATION)
    industries = cert["industries"]
    selected = selected or sorted(industries)
    paths: list[Path] = []
    for industry in selected:
        if industry not in industries:
            raise SystemExit(f"unknown certified industry: {industry}")
        for agent in industries[industry]["agents"]:
            paths.append(SCENARIOS / f"{agent['scenario_id']}.json")
    return paths


def render_prompt(scenario: dict) -> str:
    lines = [
        f"# Industry Runtime Eval: {scenario['title']}",
        "",
        "Respond as the certified industry agent would.",
        "Preserve human gates and evidence requirements.",
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

    path = REFERENCE_RESPONSES / f"{scenario_id}.md"
    if not path.exists():
        raise SystemExit(f"missing reference response: {path}")
    return path.read_text(), f"reference:{path}", False


def score_response(scenario: dict, rubric: dict, response: str, pending: bool, source: str) -> dict:
    response_lower = response.lower()
    score = 0
    max_score = 0
    criteria = []
    for criterion in rubric["criteria"]:
        weight = criterion["weight"]
        max_score += weight
        missing_terms = [
            term for term in criterion["required_terms"] if term.lower() not in response_lower
        ]
        passed = not pending and not missing_terms
        if passed:
            score += weight
        criteria.append(
            {
                "id": criterion["id"],
                "description": criterion["description"],
                "weight": weight,
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
        "industry": scenario["industry"],
        "agent_file": scenario["agent_file"],
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
    passed = sum(1 for score in scores if score["passed"])
    pending = sum(1 for score in scores if score["pending"])
    violations = sum(len(score["forbidden_violations"]) for score in scores)
    lines = [
        "# Industry Runtime Eval Summary",
        "",
        f"Run: `{run_dir.name}`",
        f"Scenarios: {len(scores)}",
        f"Passed: {passed}",
        f"Pending: {pending}",
        f"Forbidden behavior violations: {violations}",
        "",
        "| Industry | Scenario | Score | Status |",
        "| --- | --- | ---: | --- |",
    ]
    for score in scores:
        if score["pending"]:
            status = "PENDING"
        elif score["passed"]:
            status = "PASS"
        else:
            status = "FAIL"
        lines.append(f"| {score['industry']} | `{score['scenario_id']}` | {score['score']}/{score['max_score']} | {status} |")
    lines.append("")
    run_dir.joinpath("summary.md").write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("industry", nargs="*", help="certified industry slug(s) to run")
    parser.add_argument("--run-id", help="custom run id")
    parser.add_argument("--responses", type=Path, help="directory of <scenario-id>.md responses")
    parser.add_argument("--command", help="command template; supports {prompt_file} and {scenario_id}")
    args = parser.parse_args()

    run_id = args.run_id or dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    scores = []
    for scenario_path in scenario_paths(args.industry):
        scenario = load_json(scenario_path)
        rubric = load_json((scenario_path.parent / scenario["rubric"]).resolve())
        scenario_dir = run_dir / scenario["id"]
        scenario_dir.mkdir()
        prompt_path = scenario_dir / "prompt.md"
        prompt_path.write_text(render_prompt(scenario))
        response, source, pending = read_response(
            scenario["id"], prompt_path, args.responses, args.command
        )
        scenario_dir.joinpath("response.md").write_text(response)
        score = score_response(scenario, rubric, response, pending, source)
        scenario_dir.joinpath("score.json").write_text(json.dumps(score, indent=2) + "\n")
        scores.append(score)

    write_summary(run_dir, scores)
    print(f"wrote industry runtime eval run: {run_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
