#!/usr/bin/env python3
"""Validate saved runtime evaluation run artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "evals" / "runs"
SCENARIOS = ROOT / "evals" / "scenarios"


def run_dirs(selected: str | None, latest: bool) -> list[Path]:
    if not RUNS.exists():
        return []
    runs = sorted(path for path in RUNS.iterdir() if path.is_dir() and not path.name.startswith("."))
    if selected:
        path = RUNS / selected
        return [path] if path.exists() else []
    if latest and runs:
        return [runs[-1]]
    return runs


def validate_run(path: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    if not path.joinpath("summary.md").exists():
        errors.append(f"{path}: missing summary.md")

    scenario_dirs = sorted(child for child in path.iterdir() if child.is_dir())
    if not scenario_dirs:
        errors.append(f"{path}: no scenario result directories")
        return errors

    known_scenarios = {scenario.stem for scenario in SCENARIOS.glob("*.json")}
    for scenario_dir in scenario_dirs:
        scenario_id = scenario_dir.name
        if scenario_id not in known_scenarios:
            errors.append(f"{scenario_dir}: unknown scenario id")

        for filename in ["prompt.md", "response.md", "score.json"]:
            if not scenario_dir.joinpath(filename).exists():
                errors.append(f"{scenario_dir}: missing {filename}")

        score_path = scenario_dir / "score.json"
        if not score_path.exists():
            continue

        try:
            score = json.loads(score_path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{score_path}: invalid json: {exc}")
            continue

        for field in [
            "scenario_id",
            "title",
            "generated_at",
            "response_source",
            "pending",
            "score",
            "max_score",
            "minimum_score",
            "passed",
            "criteria",
            "forbidden_violations",
        ]:
            if field not in score:
                errors.append(f"{score_path}: missing {field}")

        if score.get("scenario_id") != scenario_id:
            errors.append(f"{score_path}: scenario_id must match directory name")
        if not isinstance(score.get("criteria"), list) or not score["criteria"]:
            errors.append(f"{score_path}: criteria must be a non-empty list")
        if not isinstance(score.get("forbidden_violations"), list):
            errors.append(f"{score_path}: forbidden_violations must be a list")
        if strict and score.get("pending"):
            errors.append(f"{score_path}: pending result is not allowed in strict mode")
        if strict and not score.get("passed"):
            errors.append(f"{score_path}: scenario did not pass")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", help="validate one run directory by name")
    parser.add_argument("--latest", action="store_true", help="validate only the latest run")
    parser.add_argument("--require-run", action="store_true", help="fail when no runtime runs exist")
    parser.add_argument("--strict", action="store_true", help="require every scenario result to pass")
    args = parser.parse_args()

    runs = run_dirs(args.run_id, args.latest)
    errors: list[str] = []
    if args.require_run and not runs:
        if args.run_id:
            errors.append(f"runtime eval run not found: {args.run_id}")
        else:
            errors.append("no runtime eval runs found")

    for path in runs:
        errors.extend(validate_run(path, args.strict))

    for error in errors:
        print(f"ERROR {error}")
    print(f"checked {len(runs)} runtime run(s)")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
