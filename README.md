# Golden Skill Sets

[![Validate Golden Skill Sets](https://github.com/tashiscool/golden-skill-sets/actions/workflows/lint-agents.yml/badge.svg)](https://github.com/tashiscool/golden-skill-sets/actions/workflows/lint-agents.yml)

A bounded, human-accountable Workflow OS for agentic coding.

This repository is the canonical source for the golden workflow skills under `skills/`, plus the extended Agency specialist roster under `extended-agents/`.

The point is not to automate as much as possible. The point is to shorten feedback loops while keeping humans accountable for design, correctness, security, maintainability, and failure modes.

## What This Is

Golden Skill Sets is a small operating layer for agentic coding sessions. It gives agents repeatable workflow habits: orient first, clarify scope, preserve human gates, test behavior, diagnose with evidence, review against standards and specs, and hand off cleanly.

It is designed for people using tools such as Codex, Cursor, Claude Code, and Copilot who want speed without giving up accountability.

## What Is Canonical

| Path | Purpose |
| --- | --- |
| `skills/` | The curated golden workflow skills. This is the install source. |
| `docs/golden/` | The quality standard for what counts as golden. |
| `evals/scenarios/` | Complex scenario fixtures used to validate expected behavior. |
| `evals/rubrics/` | Deterministic rubric metadata for each scenario. |
| `evals/expected/` | Expected output shapes for each scenario. |
| `evals/runs/` | Generated runtime eval artifacts. |
| `evals/industries/` | Certification fixtures for golden industry packs. |
| `extended-agents/` | Preserved Agency specialist roster and domain packs. |
| `archive/` | Historical/reference material that is not part of the active install source. |

## Golden Core

The golden workflow skills are:

- `setup-matt-pocock-skills`
- `grill-with-docs`
- `zoom-out`
- `diagnose`
- `tdd`
- `prototype`
- `to-prd`
- `to-issues`
- `handoff`
- `write-a-skill`
- `improve-codebase-architecture`
- `triage`
- `review`
- `setup-pre-commit`
- `git-guardrails-claude-code`
- `agency-workflow-task-decomposition-coach`
- `agency-persistent-memory-steward`
- `agency-stalled-work-diagnostician`
- `agency-bounded-iteration-driver`

Use them with the policy in `AGENTS.md`.

## Install Into Codex

Do not hand-edit installed copies in `~/.codex/skills`. Sync from this repo:

```bash
./scripts/sync-installed-skills.sh
```

Then restart Codex.

Check local install drift with:

```bash
./scripts/check-installed-skills.sh
```

## Validate

The authoritative validation command is:

```bash
./scripts/validate-golden.sh
```

It runs:

```bash
./scripts/validate-skills.py
./scripts/validate-golden-evals.py
./scripts/validate-runtime-runs.py
./scripts/lint-agents.sh
```

Current expected baseline:

- 19 canonical skills validate.
- 6 complex scenarios and rubrics validate.
- 30 industry packs validate with every-agent certification fixtures.
- Extended Agency agents lint with warnings allowed and errors forbidden.

## Runtime Evals

Generate pending artifacts to verify the harness:

```bash
./scripts/run-runtime-evals.py --dry-run
./scripts/validate-runtime-runs.py --require-run
```

For real evidence, run the high-risk scenarios with recorded or command-generated responses:

```bash
./scripts/run-runtime-evals.py --responses tmp/runtime-responses \
  --run-id high-risk-recorded \
  ambiguous-legacy-refactor \
  production-regression-diagnosis \
  issue-triage-human-gate

./scripts/validate-runtime-runs.py --run-id high-risk-recorded --require-run --strict
```

See `docs/golden/RUNTIME_EVALS.md`.

Runtime evals prove that saved responses match the current rubrics for the scenario prompts. They do not prove correctness for every production codebase, and they do not replace human review.

## Extended Agents

The original Agency roster is preserved under `extended-agents/`. These agents are useful specialist material, but they are not the install source for the golden workflow core.

Use them as specialist pairings inside approved scope:

- engineering and architecture
- testing and evidence collection
- product and project management
- marketing and industry workflows
- film, TV, music video, game, and spatial computing pipelines

The industry pack expansion is preserved under `extended-agents/industries/`. The generator now targets that path.

Industry packs are certified as Golden Industry Packs without being promoted into the workflow core. See `docs/golden/INDUSTRY_CERTIFICATION.md` and `docs/golden/industry-scorecards/`.

## Promotion

Candidates start in `extended-agents/` or `archive/`. Promotion into `skills/` requires a scenario fixture, rubric, expected output shape, static validation, at least one runtime eval, and human review.

See `docs/golden/GOLDEN_STANDARD.md`.

## Evidence V1

The first public credibility milestone is documented in `docs/golden/V1_RELEASE.md`. Reviewed runtime evidence is published as a GitHub Release artifact instead of being committed under `evals/runs/`.

## Provenance

The golden workflow skills are derived from Matt Pocock's [`mattpocock/skills`](https://github.com/mattpocock/skills), with bounded-workflow adaptations.

The extended agent roster descends from the Agency agent collection and is preserved here as specialist material.

See `NOTICE.md` for upstream license notices.

## License

MIT. See `LICENSE`.
