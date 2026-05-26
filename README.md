# Golden Skill Sets

A bounded, human-accountable skill system for agentic coding.

This repository is the canonical source for the golden workflow skills under `skills/`, plus the extended Agency specialist roster under `extended-agents/`.

The point is not to automate as much as possible. The point is to shorten feedback loops while keeping humans accountable for design, correctness, security, maintainability, and failure modes.

## What Is Canonical

| Path | Purpose |
| --- | --- |
| `skills/` | The curated golden workflow skills. This is the install source. |
| `docs/golden/` | The quality standard for what counts as golden. |
| `evals/scenarios/` | Complex scenario fixtures used to validate expected behavior. |
| `evals/expected/` | Expected output shapes and rubrics for each scenario. |
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

## Validate

The authoritative validation command is:

```bash
./scripts/validate-golden.sh
```

It runs:

```bash
./scripts/validate-skills.py
./scripts/validate-golden-evals.py
./scripts/lint-agents.sh
```

Current expected baseline:

- 19 canonical skills validate.
- 6 complex scenarios validate.
- Extended Agency agents lint with warnings allowed and errors forbidden.

## Runtime Smoke Test

After syncing and restarting Codex, run:

```text
Use zoom-out on this repo and summarize how the agent skill setup fits together. Do not edit files.
```

Expected behavior:

- `zoom-out` loads.
- The agent reads the repo policy/docs.
- The agent summarizes the system.
- No files are edited.

## Extended Agents

The original Agency roster is preserved under `extended-agents/`. These agents are useful specialist material, but they are not the install source for the golden workflow core.

Use them as specialist pairings inside approved scope:

- engineering and architecture
- testing and evidence collection
- product and project management
- marketing and industry workflows
- film, TV, music video, game, and spatial computing pipelines

The industry pack expansion is preserved under `extended-agents/industries/`. The generator now targets that path.

## Provenance

The golden workflow skills are derived from Matt Pocock's [`mattpocock/skills`](https://github.com/mattpocock/skills), with bounded-workflow adaptations.

The extended agent roster descends from the Agency agent collection and is preserved here as specialist material.

See `NOTICE.md` for upstream license notices.

## License

MIT. See `LICENSE`.
