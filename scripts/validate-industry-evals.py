#!/usr/bin/env python3
"""Validate golden industry certification fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals" / "industries"
SCENARIOS = EVALS / "scenarios"
RUBRICS = EVALS / "rubrics"
EXPECTED = EVALS / "expected"
CERTIFICATION = EVALS / "certification.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def validate(selected: list[str]) -> list[str]:
    errors: list[str] = []
    if not CERTIFICATION.exists():
        return ["missing evals/industries/certification.json"]
    try:
        cert = load_json(CERTIFICATION)
    except json.JSONDecodeError as exc:
        return [f"{CERTIFICATION}: invalid json: {exc}"]

    industries = cert.get("industries")
    if not isinstance(industries, dict) or not industries:
        return [f"{CERTIFICATION}: industries must be a non-empty object"]

    selected = selected or sorted(industries)
    for industry in selected:
        entry = industries.get(industry)
        if not isinstance(entry, dict):
            errors.append(f"{CERTIFICATION}: missing industry {industry}")
            continue
        agents = entry.get("agents")
        if not isinstance(agents, list) or not agents:
            errors.append(f"{CERTIFICATION}: {industry} agents must be non-empty list")
            continue
        expected_count = entry.get("agent_count")
        if expected_count != len(agents):
            errors.append(f"{CERTIFICATION}: {industry} agent_count must equal agents length")

        seen: set[str] = set()
        for agent in agents:
            sid = agent.get("scenario_id")
            agent_file = agent.get("agent_file")
            if not sid:
                errors.append(f"{CERTIFICATION}: {industry} agent missing scenario_id")
                continue
            if sid in seen:
                errors.append(f"{CERTIFICATION}: duplicate scenario_id {sid}")
            seen.add(sid)

            if not agent_file or not (ROOT / agent_file).exists():
                errors.append(f"{CERTIFICATION}: missing agent_file for {sid}")
            for field in [
                "trigger",
                "scope",
                "non_goals",
                "human_approval_gates",
                "evidence_requirements",
                "failure_modes",
                "domain_risk_rules",
            ]:
                value = agent.get(field)
                if isinstance(value, list):
                    if not value:
                        errors.append(f"{CERTIFICATION}: {sid} {field} must be non-empty")
                elif not value:
                    errors.append(f"{CERTIFICATION}: {sid} {field} must be non-empty")
            if agent.get("output_contract_required") is not True:
                errors.append(f"{CERTIFICATION}: {sid} output_contract_required must be true")

            scenario_path = SCENARIOS / f"{sid}.json"
            rubric_path = RUBRICS / f"{sid}.json"
            expected_path = EXPECTED / f"{sid}.md"
            for path in [scenario_path, rubric_path, expected_path]:
                if not path.exists():
                    errors.append(f"missing {path.relative_to(ROOT)}")

            if scenario_path.exists():
                scenario = load_json(scenario_path)
                for field in [
                    "id",
                    "title",
                    "industry",
                    "agent_file",
                    "risk",
                    "prompt",
                    "expected_agent",
                    "required_behaviors",
                    "forbidden_behaviors",
                    "expected_output",
                    "rubric",
                ]:
                    if field not in scenario:
                        errors.append(f"{scenario_path}: missing {field}")
                if scenario.get("id") != sid:
                    errors.append(f"{scenario_path}: id must match filename")
                if scenario.get("industry") != industry:
                    errors.append(f"{scenario_path}: industry must be {industry}")

            if rubric_path.exists():
                rubric = load_json(rubric_path)
                if rubric.get("id") != sid:
                    errors.append(f"{rubric_path}: id must match scenario")
                if rubric.get("agent_file") != agent_file:
                    errors.append(f"{rubric_path}: agent_file must match manifest")
                if not isinstance(rubric.get("minimum_score"), int) or rubric["minimum_score"] < 1:
                    errors.append(f"{rubric_path}: minimum_score must be positive integer")
                for field in [
                    "required_behaviors",
                    "forbidden_behaviors",
                    "evidence_quality",
                    "human_gate_compliance",
                    "criteria",
                    "forbidden_terms",
                ]:
                    if not isinstance(rubric.get(field), list) or not rubric[field]:
                        errors.append(f"{rubric_path}: {field} must be non-empty list")
                for criterion in rubric.get("criteria", []):
                    if not criterion.get("id") or not criterion.get("description"):
                        errors.append(f"{rubric_path}: criterion missing id or description")
                    if not isinstance(criterion.get("required_terms"), list) or not criterion["required_terms"]:
                        errors.append(f"{rubric_path}: criterion required_terms must be non-empty")
                    if not isinstance(criterion.get("weight"), int) or criterion["weight"] < 1:
                        errors.append(f"{rubric_path}: criterion weight must be positive integer")

            if expected_path.exists():
                expected_text = expected_path.read_text()
                if "# Expected Output Shape" not in expected_text:
                    errors.append(f"{expected_path}: missing expected output heading")
                if len(expected_text.split()) < 60:
                    errors.append(f"{expected_path}: expected output too short")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("industry", nargs="*", help="industry slug(s) to validate")
    args = parser.parse_args()

    errors = validate(args.industry)
    for error in errors:
        print(f"ERROR {error}")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
