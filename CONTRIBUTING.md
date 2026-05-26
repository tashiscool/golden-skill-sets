# Contributing

Thanks for helping improve Golden Skill Sets.

This repo has two contribution lanes:

1. **Golden workflow skills** under `skills/`
2. **Extended specialist agents** under `extended-agents/`

Golden workflow changes have a higher bar because they affect the default operating model.

## Before Opening A PR

Run:

```bash
./scripts/validate-golden.sh
```

For golden workflow changes, also update scenario coverage when behavior changes:

- `evals/scenarios/`
- `evals/rubrics/`
- `evals/expected/`

## Golden Skill Requirements

Read `docs/golden/GOLDEN_STANDARD.md` before changing `skills/`.

A golden skill must:

- state when it should be used
- preserve human approval gates
- avoid broad autonomous architecture decisions
- produce concrete, reviewable outputs
- include enough structure to be validated
- work with the bounded workflow in `AGENTS.md`

Do not edit installed copies in `~/.codex/skills` directly. Change this repo, validate, then run:

```bash
./scripts/sync-installed-skills.sh
```

## Extended Agent Requirements

Extended agents should live under `extended-agents/<category>/`.

Agent files should include YAML frontmatter:

```markdown
---
name: Agent Name
description: One-line description of the agent's specialty and focus
color: colorname or "#hexcode"
---
```

Recommended sections:

- Identity
- Core Mission
- Critical Rules
- Deliverables
- Workflow
- Success Metrics

The linter allows warnings for legacy extended agents, but new or upgraded agents should aim to remove warnings.

## Promotion Into Core

New core skills should not start directly in `skills/` unless they are already proven workflow controls. Most candidates start in `extended-agents/` or `archive/`.

Promotion requires:

- a clear workflow-control reason for being core
- a scenario fixture in `evals/scenarios/`
- a rubric in `evals/rubrics/`
- an expected output shape in `evals/expected/`
- passing `./scripts/validate-golden.sh`
- at least one runtime eval artifact for review

Industry packs remain under `extended-agents/industries/` unless they generalize into reusable workflow behavior.

## Scenario Tests

Scenario fixtures are JSON files with:

- `id`
- `title`
- `risk`
- `prompt`
- `expected_skills`
- `required_behaviors`
- `forbidden_behaviors`
- `expected_output`
- `rubric`

Expected output files should describe the shape of a good answer, not a brittle exact transcript.

Rubric files should define required behaviors, forbidden terms, expected skills, evidence quality, and human-gate compliance through criteria that can be scored deterministically.

## Pull Request Checklist

- [ ] `./scripts/validate-golden.sh` passes.
- [ ] Golden behavior changes include scenario, rubric, or expected-output updates.
- [ ] Runtime eval evidence exists when promoting a skill into core.
- [ ] New skills or agents have clear trigger/use language.
- [ ] Human gates are preserved for risky actions.
- [ ] No local paths, secrets, tokens, or private workspace assumptions are introduced.
