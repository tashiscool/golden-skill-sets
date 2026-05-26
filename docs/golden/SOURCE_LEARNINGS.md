# Source Learnings

Golden Skill Sets combines lessons from Matt Pocock skills, Paperclip workflow habits, and the Agency agent roster. The result is not a merged pile of agents; it is a curated Workflow OS with a small core and scoped extensions.

## Matt Pocock Skills

Useful patterns:

- short skills with clear trigger language
- workflow control over broad persona claims
- concrete artifacts such as PRDs, issues, reviews, and handoffs
- local setup instructions that make behavior repeatable

Applied here:

- core skills stay under `skills/`
- installed copies are generated from the repo
- scenario fixtures validate expected behavior
- broad architecture skills remain advisory unless approved

## Paperclip

Useful patterns:

- decomposing plans into executable task graphs
- durable file-based memory for long-running work
- diagnosing stalled work instead of continuing blindly
- bounded iteration loops for benchmark or QA tasks

Applied here:

- four generalized Paperclip-derived workflow skills are part of the v1 core
- original Paperclip material remains reference material unless generalized
- runtime scenarios test whether the workflow gates appear in actual responses

## Agency Agents

Useful patterns:

- rich specialist coverage across engineering, product, marketing, support, media, games, spatial computing, and industries
- domain-specific deliverables and quality criteria
- evidence-oriented testing and reality-checking roles

Applied here:

- the specialist roster stays under `extended-agents/`
- industry packs stay under `extended-agents/industries/`
- specialists can be paired with core workflow skills inside approved scope
- specialist agents do not become core unless they control reusable workflow behavior

## Curation Principle

Core is for behavior that should shape almost every serious agentic coding session. Extended is for expertise that helps once the scope is clear. Archive is for provenance and learning.

Promotion requires static validation, runtime scenario evidence, and human review.

## Development Hats

The development system should not be only an implementation toolkit. It must deliberately switch between product, PM, BA, architecture, UX, UI, backend, QA, observability, security, reporting, marketing, and sales perspectives while keeping the same bounded workflow.

Applied here:

- hats are certified as capability lenses, not necessarily literal skills
- specialist agents advise inside approved scope
- workflow skills remain responsible for scope, evidence, tests, approval gates, and handoff
- claims about quality, security, reliability, accessibility, or business impact require artifacts
