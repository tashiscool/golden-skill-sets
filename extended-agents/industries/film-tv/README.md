# Film & TV Agent Pack

## Scope
This pack defines a full operating model for Film & TV with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Develop, produce, and monetize scripted and unscripted slate work across theatrical, broadcast, and streaming windows.
- Risk Focus: budget overruns, schedule slips, union breaches, and rights/clearance failures
- Compliance Focus: guild agreements, location permitting, music/clip clearances, and delivery contracts
- Outcome Focus: on-time delivery, variance-to-budget, completion quality, and audience completion/engagement
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Development | creative | Film & TV Development Lead | Film & TV Development Operator |
| Pre-Production | operations | Film & TV Pre-Production Lead | Film & TV Pre-Production Operator |
| Production | operations | Film & TV Production Lead | Film & TV Production Operator |
| Post-Production | operations | Film & TV Post-Production Lead | Film & TV Post-Production Operator |
| Distribution | growth | Film & TV Distribution Lead | Film & TV Distribution Operator |
| Marketing & PR | growth | Film & TV Marketing & PR Lead | Film & TV Marketing & PR Operator |
| Talent & Unions | governance | Film & TV Talent & Unions Lead | Film & TV Talent & Unions Operator |
| Business Affairs | governance | Film & TV Business Affairs Lead | Film & TV Business Affairs Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, source map, and scope boundaries.
2. Planning: roadmap, owners, dependencies, acceptance criteria, and eval set definition.
3. Execution: lead/operator delivery loops by division using structured handoffs.
4. Validation: QA, approval, citation, and policy checks with evidence artifacts.
5. Launch/Ops: handover completeness, live monitoring, and rollback or escalation readiness.

## Reliability Rules
- Consequential actions require human approval according to the agent prompt.
- Policy, regulatory, legal, medical, or contractual claims require source, jurisdiction, and effective date when applicable.
- Final outputs should follow the structured contracts embedded in each agent file.
- Every prompt, model, tool, or policy change should trigger reevaluation before rollout.

## Agent Files
- Orchestrator: [agents/film-tv-orchestrator.md](agents/film-tv-orchestrator.md)
- [agents/film-tv-development-lead.md](agents/film-tv-development-lead.md)
- [agents/film-tv-development-operator.md](agents/film-tv-development-operator.md)
- [agents/film-tv-pre-production-lead.md](agents/film-tv-pre-production-lead.md)
- [agents/film-tv-pre-production-operator.md](agents/film-tv-pre-production-operator.md)
- [agents/film-tv-production-lead.md](agents/film-tv-production-lead.md)
- [agents/film-tv-production-operator.md](agents/film-tv-production-operator.md)
- [agents/film-tv-post-production-lead.md](agents/film-tv-post-production-lead.md)
- [agents/film-tv-post-production-operator.md](agents/film-tv-post-production-operator.md)
- [agents/film-tv-distribution-lead.md](agents/film-tv-distribution-lead.md)
- [agents/film-tv-distribution-operator.md](agents/film-tv-distribution-operator.md)
- [agents/film-tv-marketing-pr-lead.md](agents/film-tv-marketing-pr-lead.md)
- [agents/film-tv-marketing-pr-operator.md](agents/film-tv-marketing-pr-operator.md)
- [agents/film-tv-talent-unions-lead.md](agents/film-tv-talent-unions-lead.md)
- [agents/film-tv-talent-unions-operator.md](agents/film-tv-talent-unions-operator.md)
- [agents/film-tv-business-affairs-lead.md](agents/film-tv-business-affairs-lead.md)
- [agents/film-tv-business-affairs-operator.md](agents/film-tv-business-affairs-operator.md)

## Activation Prompt
```
Activate Film & TV Orchestrator.
Objective: Develop, produce, and monetize scripted and unscripted slate work across theatrical, broadcast, and streaming windows.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
