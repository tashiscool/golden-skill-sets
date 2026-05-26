#!/usr/bin/env python3
"""Validate golden skill scenario fixtures and expected outputs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evals" / "scenarios"
RUBRICS = ROOT / "evals" / "rubrics"

AGENT_DIRS = [
    "extended-agents/design",
    "extended-agents/engineering",
    "extended-agents/game-development",
    "extended-agents/marketing",
    "extended-agents/paid-media",
    "extended-agents/product",
    "extended-agents/project-management",
    "extended-agents/testing",
    "extended-agents/support",
    "extended-agents/spatial-computing",
    "extended-agents/specialized",
    "extended-agents/film-tv-ai",
    "extended-agents/music-video-ai",
]

WORKFLOW_SKILL_DIRS = [
    ROOT / "skills",
]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def workflow_skill_names() -> set[str]:
    names: set[str] = set()
    for base in WORKFLOW_SKILL_DIRS:
        if not base.exists():
            continue
        for skill in base.glob("*/SKILL.md"):
            names.add(skill.parent.name)
    return names


def agency_skill_names() -> set[str]:
    names: set[str] = set()
    for dirname in AGENT_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.name.upper() == "README.MD":
                continue
            text = path.read_text(errors="ignore")
            match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            if not match:
                continue
            name_match = re.search(r"^name:\s*(.+)$", match.group(1), re.M)
            if not name_match:
                continue
            names.add(f"agency-{slugify(name_match.group(1))}")
    return names


def validate() -> list[str]:
    errors: list[str] = []
    known_skills = workflow_skill_names() | agency_skill_names()

    if not SCENARIOS.exists():
        return ["missing evals/scenarios directory"]

    scenario_files = sorted(SCENARIOS.glob("*.json"))
    if not scenario_files:
        return ["no scenario fixtures found"]

    seen_ids: set[str] = set()

    for path in scenario_files:
        try:
            scenario = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid json: {exc}")
            continue

        for field in [
            "id",
            "title",
            "risk",
            "prompt",
            "expected_skills",
            "required_behaviors",
            "forbidden_behaviors",
            "expected_output",
            "rubric",
        ]:
            if field not in scenario:
                errors.append(f"{path}: missing {field}")

        scenario_id = scenario.get("id")
        if scenario_id:
            if scenario_id in seen_ids:
                errors.append(f"{path}: duplicate id {scenario_id}")
            seen_ids.add(scenario_id)
            if path.stem != scenario_id:
                errors.append(f"{path}: filename must match id {scenario_id}")

        for list_field in ["expected_skills", "required_behaviors", "forbidden_behaviors"]:
            value = scenario.get(list_field)
            if not isinstance(value, list) or not value:
                errors.append(f"{path}: {list_field} must be a non-empty list")

        for skill in scenario.get("expected_skills", []):
            if skill not in known_skills:
                errors.append(f"{path}: unknown expected skill {skill}")

        expected_rel = scenario.get("expected_output")
        if expected_rel:
            expected_path = (path.parent / expected_rel).resolve()
            try:
                expected_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path}: expected_output escapes repo")
                continue
            if not expected_path.exists():
                errors.append(f"{path}: missing expected output {expected_rel}")
            else:
                expected_text = expected_path.read_text(errors="ignore")
                if len(expected_text.split()) < 40:
                    errors.append(f"{expected_path}: expected output too short")
                for heading in ["# Expected Output Shape"]:
                    if heading not in expected_text:
                        errors.append(f"{expected_path}: missing heading {heading}")

        rubric_rel = scenario.get("rubric")
        if rubric_rel:
            rubric_path = (path.parent / rubric_rel).resolve()
        elif scenario_id:
            rubric_path = RUBRICS / f"{scenario_id}.json"
            errors.append(f"{path}: missing rubric field; expected ../rubrics/{scenario_id}.json")
        else:
            rubric_path = None

        if rubric_path:
            try:
                rubric_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path}: rubric escapes repo")
                continue
            if not rubric_path.exists():
                errors.append(f"{path}: missing rubric {rubric_path.relative_to(ROOT)}")
            else:
                try:
                    rubric = json.loads(rubric_path.read_text())
                except json.JSONDecodeError as exc:
                    errors.append(f"{rubric_path}: invalid json: {exc}")
                    continue
                if rubric.get("id") != scenario_id:
                    errors.append(f"{rubric_path}: id must match scenario id {scenario_id}")
                if not isinstance(rubric.get("minimum_score"), int) or rubric["minimum_score"] < 1:
                    errors.append(f"{rubric_path}: minimum_score must be a positive integer")
                for list_field in [
                    "expected_skills",
                    "required_behaviors",
                    "forbidden_behaviors",
                    "evidence_quality",
                    "human_gate_compliance",
                ]:
                    value = rubric.get(list_field)
                    if not isinstance(value, list) or not value:
                        errors.append(f"{rubric_path}: {list_field} must be a non-empty list")
                if isinstance(rubric.get("expected_skills"), list):
                    for skill in rubric["expected_skills"]:
                        if skill not in scenario.get("expected_skills", []):
                            errors.append(f"{rubric_path}: unexpected rubric skill {skill}")
                criteria = rubric.get("criteria")
                if not isinstance(criteria, list) or not criteria:
                    errors.append(f"{rubric_path}: criteria must be a non-empty list")
                else:
                    seen_criteria: set[str] = set()
                    for criterion in criteria:
                        if not isinstance(criterion, dict):
                            errors.append(f"{rubric_path}: each criterion must be an object")
                            continue
                        cid = criterion.get("id")
                        if not cid:
                            errors.append(f"{rubric_path}: criterion missing id")
                        elif cid in seen_criteria:
                            errors.append(f"{rubric_path}: duplicate criterion id {cid}")
                        else:
                            seen_criteria.add(cid)
                        if not criterion.get("description"):
                            errors.append(f"{rubric_path}: criterion {cid} missing description")
                        terms = criterion.get("required_terms")
                        if not isinstance(terms, list) or not terms:
                            errors.append(f"{rubric_path}: criterion {cid} requires non-empty required_terms")
                        if not isinstance(criterion.get("weight"), int) or criterion["weight"] < 1:
                            errors.append(f"{rubric_path}: criterion {cid} weight must be positive integer")
                forbidden_terms = rubric.get("forbidden_terms")
                if not isinstance(forbidden_terms, list):
                    errors.append(f"{rubric_path}: forbidden_terms must be a list")

    required_scenarios = {
        "ambiguous-legacy-refactor",
        "production-regression-diagnosis",
        "frontend-visual-qa",
        "issue-triage-human-gate",
        "standards-vs-spec-review",
        "skill-authoring",
    }
    missing = required_scenarios - seen_ids
    for scenario_id in sorted(missing):
        errors.append(f"missing required scenario {scenario_id}")

    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"ERROR {error}")
    print(f"checked {len(list(SCENARIOS.glob('*.json'))) if SCENARIOS.exists() else 0} scenarios")
    print("status", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
