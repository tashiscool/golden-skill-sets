#!/usr/bin/env python3
"""Validate development capability certification fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "development"
SCENARIOS = EVALS / "scenarios"
RUBRICS = EVALS / "rubrics"
EXPECTED = EVALS / "expected"
CERTIFICATION = EVALS / "certification.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def validate(selected: list[str]) -> list[str]:
    errors: list[str] = []
    if not CERTIFICATION.exists():
        return ["missing evals/development/certification.json"]
    cert = load_json(CERTIFICATION)
    capabilities = cert.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        return [f"{CERTIFICATION}: capabilities must be a non-empty list"]

    selected_set = set(selected)
    seen: set[str] = set()
    for capability in capabilities:
        cid = capability.get("id")
        if selected_set and cid not in selected_set:
            continue
        if not cid:
            errors.append(f"{CERTIFICATION}: capability missing id")
            continue
        if cid in seen:
            errors.append(f"{CERTIFICATION}: duplicate capability id {cid}")
        seen.add(cid)

        for agent in capability.get("expected_agents", []):
            if not (ROOT / agent).exists():
                errors.append(f"{CERTIFICATION}: {cid} missing expected agent {agent}")

        scenario_path = SCENARIOS / f"{cid}.json"
        rubric_path = RUBRICS / f"{cid}.json"
        expected_path = EXPECTED / f"{cid}.md"
        for path in [scenario_path, rubric_path, expected_path]:
            if not path.exists():
                errors.append(f"missing {path.relative_to(ROOT)}")

        if scenario_path.exists():
            scenario = load_json(scenario_path)
            for field in [
                "id",
                "title",
                "risk",
                "hats",
                "prompt",
                "expected_agents",
                "required_behaviors",
                "forbidden_behaviors",
                "expected_output",
                "rubric",
            ]:
                if field not in scenario:
                    errors.append(f"{scenario_path}: missing {field}")
            if scenario.get("id") != cid:
                errors.append(f"{scenario_path}: id must match filename")

        if rubric_path.exists():
            rubric = load_json(rubric_path)
            if rubric.get("id") != cid:
                errors.append(f"{rubric_path}: id must match scenario")
            for field in [
                "hats",
                "expected_agents",
                "required_behaviors",
                "forbidden_behaviors",
                "evidence_quality",
                "human_gate_compliance",
                "criteria",
                "forbidden_terms",
            ]:
                if not isinstance(rubric.get(field), list) or not rubric[field]:
                    errors.append(f"{rubric_path}: {field} must be a non-empty list")
            if not isinstance(rubric.get("minimum_score"), int) or rubric["minimum_score"] < 1:
                errors.append(f"{rubric_path}: minimum_score must be positive integer")
            for criterion in rubric.get("criteria", []):
                if not criterion.get("id") or not criterion.get("description"):
                    errors.append(f"{rubric_path}: criterion missing id or description")
                if not isinstance(criterion.get("required_terms"), list) or not criterion["required_terms"]:
                    errors.append(f"{rubric_path}: criterion required_terms must be non-empty")
                if not isinstance(criterion.get("weight"), int) or criterion["weight"] < 1:
                    errors.append(f"{rubric_path}: criterion weight must be positive integer")

        if expected_path.exists():
            text = expected_path.read_text()
            if "# Expected Output Shape" not in text:
                errors.append(f"{expected_path}: missing expected output heading")
            if len(text.split()) < 60:
                errors.append(f"{expected_path}: expected output too short")

    missing = selected_set - seen
    for cid in sorted(missing):
        errors.append(f"unknown capability {cid}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capability", nargs="*", help="capability id(s) to validate")
    args = parser.parse_args()
    errors = validate(args.capability)
    for error in errors:
        print(f"ERROR {error}")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
