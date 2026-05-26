# Music Agent Pack

## Scope
This pack defines a full operating model for Music with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Build sustainable artist and catalog growth across recorded music, publishing, live, and merchandise.
- Risk Focus: rights disputes, royalty leakage, tour execution risk, and underperforming releases
- Compliance Focus: publishing splits, neighboring rights, venue/compliance terms, and royalty reporting accuracy
- Outcome Focus: stream share, catalog growth, tour profitability, and royalty accuracy
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| A&R | creative | Music A&R Lead | Music A&R Operator |
| Recording & Production | creative | Music Recording & Production Lead | Music Recording & Production Operator |
| Publishing & Rights | governance | Music Publishing & Rights Lead | Music Publishing & Rights Operator |
| Distribution | growth | Music Distribution Lead | Music Distribution Operator |
| Touring & Live | operations | Music Touring & Live Lead | Music Touring & Live Operator |
| Marketing | growth | Music Marketing Lead | Music Marketing Operator |
| Merchandising | growth | Music Merchandising Lead | Music Merchandising Operator |
| Royalty Operations | governance | Music Royalty Operations Lead | Music Royalty Operations Operator |

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
- Orchestrator: [agents/music-orchestrator.md](agents/music-orchestrator.md)
- [agents/music-a-r-lead.md](agents/music-a-r-lead.md)
- [agents/music-a-r-operator.md](agents/music-a-r-operator.md)
- [agents/music-recording-production-lead.md](agents/music-recording-production-lead.md)
- [agents/music-recording-production-operator.md](agents/music-recording-production-operator.md)
- [agents/music-publishing-rights-lead.md](agents/music-publishing-rights-lead.md)
- [agents/music-publishing-rights-operator.md](agents/music-publishing-rights-operator.md)
- [agents/music-distribution-lead.md](agents/music-distribution-lead.md)
- [agents/music-distribution-operator.md](agents/music-distribution-operator.md)
- [agents/music-touring-live-lead.md](agents/music-touring-live-lead.md)
- [agents/music-touring-live-operator.md](agents/music-touring-live-operator.md)
- [agents/music-marketing-lead.md](agents/music-marketing-lead.md)
- [agents/music-marketing-operator.md](agents/music-marketing-operator.md)
- [agents/music-merchandising-lead.md](agents/music-merchandising-lead.md)
- [agents/music-merchandising-operator.md](agents/music-merchandising-operator.md)
- [agents/music-royalty-operations-lead.md](agents/music-royalty-operations-lead.md)
- [agents/music-royalty-operations-operator.md](agents/music-royalty-operations-operator.md)

## Activation Prompt
```
Activate Music Orchestrator.
Objective: Build sustainable artist and catalog growth across recorded music, publishing, live, and merchandise.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
