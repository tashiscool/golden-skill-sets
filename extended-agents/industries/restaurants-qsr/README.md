# Restaurants & QSR Agent Pack

## Scope
This pack defines a full operating model for Restaurants & QSR with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Standardize high-throughput operations and guest experience across owned and franchised locations.
- Risk Focus: service inconsistency, food waste, labor imbalance, and guest satisfaction volatility
- Compliance Focus: food handling, labor rules, franchise standards, and local permitting
- Outcome Focus: same-store sales, ticket times, guest satisfaction, and waste reduction
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Menu R&D | knowledge | Restaurants & QSR Menu R&D Lead | Restaurants & QSR Menu R&D Operator |
| Procurement | operations | Restaurants & QSR Procurement Lead | Restaurants & QSR Procurement Operator |
| Kitchen Operations | operations | Restaurants & QSR Kitchen Operations Lead | Restaurants & QSR Kitchen Operations Operator |
| Front-of-House | operations | Restaurants & QSR Front-of-House Lead | Restaurants & QSR Front-of-House Operator |
| Delivery Operations | operations | Restaurants & QSR Delivery Operations Lead | Restaurants & QSR Delivery Operations Operator |
| Local Marketing | growth | Restaurants & QSR Local Marketing Lead | Restaurants & QSR Local Marketing Operator |
| Franchising | governance | Restaurants & QSR Franchising Lead | Restaurants & QSR Franchising Operator |
| Training & QA | governance | Restaurants & QSR Training & QA Lead | Restaurants & QSR Training & QA Operator |

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
- Orchestrator: [agents/restaurants-qsr-orchestrator.md](agents/restaurants-qsr-orchestrator.md)
- [agents/restaurants-qsr-menu-r-d-lead.md](agents/restaurants-qsr-menu-r-d-lead.md)
- [agents/restaurants-qsr-menu-r-d-operator.md](agents/restaurants-qsr-menu-r-d-operator.md)
- [agents/restaurants-qsr-procurement-lead.md](agents/restaurants-qsr-procurement-lead.md)
- [agents/restaurants-qsr-procurement-operator.md](agents/restaurants-qsr-procurement-operator.md)
- [agents/restaurants-qsr-kitchen-operations-lead.md](agents/restaurants-qsr-kitchen-operations-lead.md)
- [agents/restaurants-qsr-kitchen-operations-operator.md](agents/restaurants-qsr-kitchen-operations-operator.md)
- [agents/restaurants-qsr-front-of-house-lead.md](agents/restaurants-qsr-front-of-house-lead.md)
- [agents/restaurants-qsr-front-of-house-operator.md](agents/restaurants-qsr-front-of-house-operator.md)
- [agents/restaurants-qsr-delivery-operations-lead.md](agents/restaurants-qsr-delivery-operations-lead.md)
- [agents/restaurants-qsr-delivery-operations-operator.md](agents/restaurants-qsr-delivery-operations-operator.md)
- [agents/restaurants-qsr-local-marketing-lead.md](agents/restaurants-qsr-local-marketing-lead.md)
- [agents/restaurants-qsr-local-marketing-operator.md](agents/restaurants-qsr-local-marketing-operator.md)
- [agents/restaurants-qsr-franchising-lead.md](agents/restaurants-qsr-franchising-lead.md)
- [agents/restaurants-qsr-franchising-operator.md](agents/restaurants-qsr-franchising-operator.md)
- [agents/restaurants-qsr-training-qa-lead.md](agents/restaurants-qsr-training-qa-lead.md)
- [agents/restaurants-qsr-training-qa-operator.md](agents/restaurants-qsr-training-qa-operator.md)

## Activation Prompt
```
Activate Restaurants & QSR Orchestrator.
Objective: Standardize high-throughput operations and guest experience across owned and franchised locations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
