# Travel & Hospitality Agent Pack

## Scope
This pack defines a full operating model for Travel & Hospitality with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Maximize occupancy and revenue while protecting service quality across customer journeys.
- Risk Focus: demand volatility, service failures, overbooking/underutilization, and partner breakdowns
- Compliance Focus: consumer protections, local hospitality regulations, data/privacy, and payment security
- Outcome Focus: RevPAR/ADR optimization, occupancy, guest satisfaction, and repeat bookings
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Revenue Management | analytics | Travel & Hospitality Revenue Management Lead | Travel & Hospitality Revenue Management Operator |
| Reservations | operations | Travel & Hospitality Reservations Lead | Travel & Hospitality Reservations Operator |
| Property Operations | operations | Travel & Hospitality Property Operations Lead | Travel & Hospitality Property Operations Operator |
| Guest Experience | service | Travel & Hospitality Guest Experience Lead | Travel & Hospitality Guest Experience Operator |
| Partnerships | strategy | Travel & Hospitality Partnerships Lead | Travel & Hospitality Partnerships Operator |
| Marketing | growth | Travel & Hospitality Marketing Lead | Travel & Hospitality Marketing Operator |
| Events | operations | Travel & Hospitality Events Lead | Travel & Hospitality Events Operator |
| Compliance | governance | Travel & Hospitality Compliance Lead | Travel & Hospitality Compliance Operator |

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
- Orchestrator: [agents/travel-hospitality-orchestrator.md](agents/travel-hospitality-orchestrator.md)
- [agents/travel-hospitality-revenue-management-lead.md](agents/travel-hospitality-revenue-management-lead.md)
- [agents/travel-hospitality-revenue-management-operator.md](agents/travel-hospitality-revenue-management-operator.md)
- [agents/travel-hospitality-reservations-lead.md](agents/travel-hospitality-reservations-lead.md)
- [agents/travel-hospitality-reservations-operator.md](agents/travel-hospitality-reservations-operator.md)
- [agents/travel-hospitality-property-operations-lead.md](agents/travel-hospitality-property-operations-lead.md)
- [agents/travel-hospitality-property-operations-operator.md](agents/travel-hospitality-property-operations-operator.md)
- [agents/travel-hospitality-guest-experience-lead.md](agents/travel-hospitality-guest-experience-lead.md)
- [agents/travel-hospitality-guest-experience-operator.md](agents/travel-hospitality-guest-experience-operator.md)
- [agents/travel-hospitality-partnerships-lead.md](agents/travel-hospitality-partnerships-lead.md)
- [agents/travel-hospitality-partnerships-operator.md](agents/travel-hospitality-partnerships-operator.md)
- [agents/travel-hospitality-marketing-lead.md](agents/travel-hospitality-marketing-lead.md)
- [agents/travel-hospitality-marketing-operator.md](agents/travel-hospitality-marketing-operator.md)
- [agents/travel-hospitality-events-lead.md](agents/travel-hospitality-events-lead.md)
- [agents/travel-hospitality-events-operator.md](agents/travel-hospitality-events-operator.md)
- [agents/travel-hospitality-compliance-lead.md](agents/travel-hospitality-compliance-lead.md)
- [agents/travel-hospitality-compliance-operator.md](agents/travel-hospitality-compliance-operator.md)

## Activation Prompt
```
Activate Travel & Hospitality Orchestrator.
Objective: Maximize occupancy and revenue while protecting service quality across customer journeys.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
