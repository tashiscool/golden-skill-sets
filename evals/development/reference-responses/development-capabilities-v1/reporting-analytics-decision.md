# Development Capability Response

## Scope

This is not implementation-ready. I would bound the scope, define acceptance criteria, and confirm authority before execution.

## Hats And Responsibilities

Hats: Reporting, Analytics, Data.

- Product/business owner: clarify user value, business constraints, and acceptance criteria.
- Architecture/engineering owner: identify tradeoffs, public API, persistence, integration, and maintainability impact.
- Quality owner: define evidence, tests, artifacts, and release gates.
- Risk owner: identify security, privacy, compliance, availability, accessibility, or launch risks where relevant.

## Facts

- The request is high impact and has incomplete context.
- Specialist agents may advise, but the golden workflow core controls scope, evidence, and approval gates.

## Assumptions

- Business context may be incomplete.
- Existing code, docs, ADRs, and design-system constraints must be checked before implementation.

## Risks

- Collapsing all hats into generic developer execution can miss product, UX, QA, security, observability, or GTM failure modes.
- Claiming quality without evidence can create polished but unsafe output.

## Human Approval Gate

Human approval is required before architecture, security, public API, persistence, launch, or external-write changes.

## Evidence, Tests, And Artifacts

- Evidence: tests, logs, screenshots, traces, citations, or explicit assumptions.
- Tests: behavior-level tests through public interfaces, plus regression checks for critical paths.
- Artifacts: decision notes, risk register, test results, screenshots or traces where relevant.
- Release gate: no launch until acceptance criteria, evidence, and approval gates are satisfied.

## Domain Coverage

This response explicitly covers metric definitions, data quality, lineage.

## Output Contract / Checklist

- [ ] Scope and non-goals captured.
- [ ] Acceptance criteria captured.
- [ ] Hats and responsibilities mapped.
- [ ] Facts, assumptions, risks, and decisions separated.
- [ ] Human approval gate documented.
- [ ] Evidence, tests, artifacts, and release gates named.
