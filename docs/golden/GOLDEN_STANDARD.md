# Golden Standard

Golden Skill Sets is not just a large roster of agents. The golden version is a curated system with:

- a bounded engineering workflow
- specialist agents used inside explicit scope
- human approval gates for architecture, issue-tracker, dependency, and git-history changes
- scenario tests with expected outputs
- validation scripts that catch drift

## Quality Bar

An agent or skill is golden only when it satisfies all five bars.

| Bar | Requirement |
| --- | --- |
| Scope | The agent states what it owns and what it must not decide alone. |
| Evidence | Claims are backed by tests, screenshots, logs, citations, or explicit assumptions. |
| Output | The expected deliverable shape is concrete enough to evaluate. |
| Safety | Destructive, architectural, broad, or external write actions require approval. |
| Composability | The agent can be paired with workflow skills and specialist agents without taking over the whole process. |

## Golden Workflow Core

Use these workflow skills to control the work:

- `zoom-out` for unfamiliar code.
- `grill-with-docs` for unclear requirements, terminology, edge cases, or acceptance criteria.
- `to-prd` and `to-issues` for tracked work.
- `tdd` for behavior-first implementation.
- `diagnose` for bugs, regressions, and performance issues.
- `handoff` for continuity.
- `review` for Standards vs Spec review.

Use Agency specialist agents for domain execution:

- Engineering: frontend, backend, security, data, DevOps, code review.
- Testing: API, evidence, reality checking, performance, accessibility.
- Planning: project shepherd, sprint prioritizer, workflow task decomposition.
- Domain packs: marketing, media, games, spatial computing, industry packs.

The generalized Paperclip-derived workflow agents are promoted as canonical golden skills:

- `agency-workflow-task-decomposition-coach`
- `agency-persistent-memory-steward`
- `agency-stalled-work-diagnostician`
- `agency-bounded-iteration-driver`

Their extended-agent source material is also preserved under `extended-agents/specialized/`.

## Human Gates

The following actions require explicit approval unless the user directly requested the exact action:

- broad refactors
- architecture decisions
- new dependencies
- public API changes
- persistence/schema behavior changes
- issue closure, `wontfix`, or `ready-for-agent`
- staging, committing, pushing, or opening PRs
- destructive git or filesystem commands

## Evaluation Strategy

Golden validation has two layers.

1. **Static validation**: scenario fixtures, expected outputs, required headings, forbidden behavior, and skill references are checked by `scripts/validate-golden-evals.py`.
2. **Runtime validation**: after restarting Codex, run the prompts in `evals/scenarios/` and compare responses to `evals/expected/`.

Static validation does not prove model behavior. It proves the repo has an executable test specification. Runtime validation proves the active agent setup follows it.

## Current Scenario Suite

| Scenario | Purpose |
| --- | --- |
| `ambiguous-legacy-refactor` | Ensures broad ambiguous work becomes a scoped plan, not immediate edits. |
| `production-regression-diagnosis` | Ensures debugging starts with a feedback loop, hypotheses, and regression tests. |
| `frontend-visual-qa` | Ensures frontend work uses implementation plus visual/evidence validation. |
| `issue-triage-human-gate` | Ensures issue tracker mutations are proposed before applied. |
| `standards-vs-spec-review` | Ensures review findings separate documented standards from spec mismatches. |
| `skill-authoring` | Ensures new skills are scoped, structured, validated, and documented. |

## Release Rule

Do not call a set of agents "golden" unless:

```sh
./scripts/validate-golden.sh
```

passes, and at least the high-risk runtime scenarios have been manually smoke-tested:

- `ambiguous-legacy-refactor`
- `production-regression-diagnosis`
- `issue-triage-human-gate`
