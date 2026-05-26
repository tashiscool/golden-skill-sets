# Agent Instructions

This repo uses a bounded, human-accountable agentic coding workflow.

## Operating Mode

- For non-trivial coding work, start with planning and codebase orientation before editing.
- Keep implementation scope narrow and tied to explicit acceptance criteria.
- Do not make architectural decisions independently.
- Do not add dependencies, change public APIs, alter persistence behavior, or refactor broad areas without explicit approval.
- Prefer tests, repro scripts, documentation, mechanical refactors, migration drafts, and small well-specified implementation tasks.
- Call out uncertainty, implicit domain behavior, and assumptions instead of filling gaps silently.
- After implementation, summarize the diff, tests run, and remaining risk.

## Agent Skills

### Issue Tracker

Issues and PRDs for this repo live in GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage Labels

Use the default five-role triage vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`. See `docs/agents/triage-labels.md`.

### Domain Docs

This is a single-context repo. Read root `CONTEXT.md` if present, plus relevant ADRs under `docs/adr/`. See `docs/agents/domain.md`.

## Golden Workflow

For ordinary production coding, prefer:

1. `zoom-out` when entering unfamiliar code.
2. `grill-with-docs` when requirements, terminology, edge cases, or acceptance criteria are unclear.
3. `to-prd` or `to-issues` when work should be tracked before execution.
4. `tdd` when behavior can be specified through tests.
5. `diagnose` for bugs, regressions, and performance issues.
6. Agency specialist skills only inside the approved scope.
7. Architecture skills as advisory unless the user explicitly approves a change.

## Human Gates

- Broad refactors require explicit written scope.
- Architecture changes require human approval before implementation.
- Issue closure, `wontfix`, and `ready-for-agent` transitions require confirmation unless the user directly requested them.
- Generated code should be explainable in PR review and debuggable in production by the human owner.
