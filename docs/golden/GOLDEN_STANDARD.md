# Golden Standard

Golden Skill Sets is a Workflow OS for bounded, human-accountable agentic coding. It is intentionally smaller than the full Agency roster: the core controls how work is planned, gated, tested, reviewed, and handed off; specialists stay available as scoped extensions.

## Tiers

| Tier | Path | Role | Release status |
| --- | --- | --- | --- |
| Core | `skills/` | Managed golden workflow skills that shape default agent behavior. | Installed and validated. |
| Extended | `extended-agents/` | Specialist agents, media pipelines, and industry packs used inside approved scope. | Preserved and linted, not installed as core. |
| Archive | `archive/` | Upstream/reference material and historical imports. | Reference only. |

The v1 core contains 19 skills. Broad specialist agents are not promoted into core unless they control reusable workflow behavior and pass the promotion process below.

Industry packs can become certified Golden Industry Packs while remaining under `extended-agents/industries/`. Certification requires every agent in the pack to have scenario, rubric, expected-output, and runtime evidence. See `docs/golden/INDUSTRY_CERTIFICATION.md`.

## Quality Bar

An agent or skill is golden only when it satisfies all five bars.

| Bar | Requirement |
| --- | --- |
| Scope | The agent states what it owns and what it must not decide alone. |
| Evidence | Claims are backed by tests, screenshots, logs, citations, or explicit assumptions. |
| Output | The expected deliverable shape is concrete enough to evaluate. |
| Safety | Destructive, architectural, broad, or external write actions require approval. |
| Composability | The agent can pair with workflow skills and specialist agents without taking over the whole process. |

## Golden Workflow Core

Use these workflow skills to control the work:

- `zoom-out` for unfamiliar code.
- `grill-with-docs` for unclear requirements, terminology, edge cases, or acceptance criteria.
- `to-prd` and `to-issues` for tracked work.
- `tdd` for behavior-first implementation.
- `diagnose` for bugs, regressions, and performance issues.
- `handoff` for continuity.
- `review` for Standards vs Spec review.
- `setup-pre-commit` and `git-guardrails-claude-code` for local safety rails.
- `write-a-skill` for new reusable skill authoring.
- `prototype` for throwaway exploration.
- `improve-codebase-architecture` as advisory architecture analysis.

The generalized Paperclip-derived workflow agents are promoted as canonical golden skills:

- `agency-workflow-task-decomposition-coach`
- `agency-persistent-memory-steward`
- `agency-stalled-work-diagnostician`
- `agency-bounded-iteration-driver`

Their extended-agent source material is preserved under `extended-agents/specialized/`.

## Extended Agents

Use Agency specialist agents only inside an approved scope:

- Engineering: frontend, backend, security, data, DevOps, code review.
- Testing: API, evidence, reality checking, performance, accessibility.
- Planning: project shepherd, sprint prioritizer, workflow task decomposition.
- Domain packs: marketing, media, games, spatial computing, and industries.

Industry pack extensions remain under `extended-agents/industries/`. They are valuable domain context, but they do not become core unless they generalize into reusable workflow control.

The first certified trust-heavy tranche is Banking & Fintech, Healthcare Providers, Cybersecurity Industry, Legal Services, and Government/Public Sector.

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

## Promotion Process

Promotion into `skills/` requires evidence, not taste.

1. Start the candidate in `extended-agents/` or `archive/`.
2. Generalize it into workflow behavior rather than domain-only expertise.
3. Add or update a fixture in `evals/scenarios/`.
4. Add a matching rubric in `evals/rubrics/`.
5. Add an expected output shape in `evals/expected/`.
6. Pass static validation with `./scripts/validate-golden.sh`.
7. Pass at least one runtime eval and save the run artifacts for review.
8. Move the skill into `skills/` only after the evidence supports promotion.

## Evaluation Strategy

Golden validation has two layers.

1. Static validation proves the repo has a coherent executable test specification.
2. Runtime validation proves the active agent setup follows that specification in real scenario responses.

Static validation is required for every release:

```bash
./scripts/validate-golden.sh
```

Runtime validation is required before claiming the setup is working well enough to publish as golden:

```bash
./scripts/run-runtime-evals.py --dry-run
./scripts/validate-runtime-runs.py --require-run
```

Use recorded or command-generated responses for real scoring. See `docs/golden/RUNTIME_EVALS.md`.

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

- `./scripts/validate-golden.sh` passes.
- Every scenario has a rubric.
- Runtime eval artifacts exist for the high-risk scenarios.
- No runtime response violates forbidden behaviors.
- Installed Codex skills can be regenerated from this repo with `./scripts/sync-installed-skills.sh`.
- Certified industry packs pass `./scripts/validate-industry-evals.py` and strict industry runtime validation for their release run.
