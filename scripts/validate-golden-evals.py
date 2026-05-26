#!/usr/bin/env python3
"""Validate golden skill scenario fixtures and expected outputs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evals" / "scenarios"

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
