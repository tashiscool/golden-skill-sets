# Golden Skill Sets

This repository is now the canonical `golden-skill-sets` source.

## Canonical Layout

| Path | Role |
| --- | --- |
| `skills/` | Active golden workflow skills and the only source used for local installs. |
| `extended-agents/` | Preserved Agency specialist roster and domain packs. |
| `evals/` | Complex scenarios and expected output shapes. |
| `docs/golden/` | The quality bar for golden skills and agents. |
| `archive/` | Historical/reference material that should not drive installs. |

## Installed Status

The current local Codex install should be generated from this repo with:

```sh
./scripts/sync-installed-skills.sh
```

Do not hand-edit `/Users/tkhan/.codex/skills` for managed golden skills. Edit `skills/`, validate, then sync.

## Golden Core

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

## Validation

Authoritative validation:

```sh
./scripts/validate-golden.sh
```

This checks:

- canonical skill structure
- bounded-workflow policy snippets
- complex scenario fixtures
- expected output rubrics
- extended-agent frontmatter and structure

## Provenance

The workflow skills are derived from Matt Pocock's `mattpocock/skills`, with bounded-workflow adaptations. The extended specialist roster preserves the useful Agency material under `extended-agents/`.
