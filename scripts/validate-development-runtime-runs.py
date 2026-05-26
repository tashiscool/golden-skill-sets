#!/usr/bin/env python3
"""Validate saved development runtime eval artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "evals" / "development" / "runs"
SCENARIOS = ROOT / "evals" / "development" / "scenarios"


def run_dirs(selected: str | None) -> list[Path]:
    if not RUNS.exists():
        return []
    if selected:
        path = RUNS / selected
        return [path] if path.exists() else []
    return sorted(path for path in RUNS.iterdir() if path.is_dir() and not path.name.startswith("."))


def validate_run(path: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    if not path.joinpath("summary.md").exists():
        errors.append(f"{path}: missing summary.md")
    scenario_dirs = sorted(child for child in path.iterdir() if child.is_dir())
    if not scenario_dirs:
        errors.append(f"{path}: no scenario result directories")
        return errors
    known = {path.stem for path in SCENARIOS.glob("*.json")}
    for scenario_dir in scenario_dirs:
        if scenario_dir.name not in known:
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
        if strict and score.get("pending"):
            errors.append(f"{score_path}: pending result is not allowed in strict mode")
        if strict and not score.get("passed"):
            errors.append(f"{score_path}: scenario did not pass")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id")
    parser.add_argument("--require-run", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    runs = run_dirs(args.run_id)
    errors = []
    if args.require_run and not runs:
        errors.append(f"development runtime eval run not found: {args.run_id or '<any>'}")
    for path in runs:
        errors.extend(validate_run(path, args.strict))
    for error in errors:
        print(f"ERROR {error}")
    print(f"checked {len(runs)} development runtime run(s)")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
