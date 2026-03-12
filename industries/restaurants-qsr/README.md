# Restaurants & QSR Agent Pack

## Scope
This pack defines a full operating model for Restaurants & QSR with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Standardize high-throughput operations and guest experience across owned and franchised locations.
- Risk Focus: service inconsistency, food waste, labor imbalance, and guest satisfaction volatility
- Compliance Focus: food handling, labor rules, franchise standards, and local permitting
- Outcome Focus: same-store sales, ticket times, guest satisfaction, and waste reduction

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Menu R&D | Restaurants & QSR Menu R&D Lead | Restaurants & QSR Menu R&D Operator |
| Procurement | Restaurants & QSR Procurement Lead | Restaurants & QSR Procurement Operator |
| Kitchen Operations | Restaurants & QSR Kitchen Operations Lead | Restaurants & QSR Kitchen Operations Operator |
| Front-of-House | Restaurants & QSR Front-of-House Lead | Restaurants & QSR Front-of-House Operator |
| Delivery Operations | Restaurants & QSR Delivery Operations Lead | Restaurants & QSR Delivery Operations Operator |
| Local Marketing | Restaurants & QSR Local Marketing Lead | Restaurants & QSR Local Marketing Operator |
| Franchising | Restaurants & QSR Franchising Lead | Restaurants & QSR Franchising Operator |
| Training & QA | Restaurants & QSR Training & QA Lead | Restaurants & QSR Training & QA Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

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
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
