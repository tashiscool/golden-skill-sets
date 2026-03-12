# Manufacturing Agent Pack

## Scope
This pack defines a full operating model for Manufacturing with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Improve throughput, quality, and reliability from planning through production and fulfillment.
- Risk Focus: line downtime, quality escapes, supply disruptions, and planning instability
- Compliance Focus: process controls, safety standards, traceability, and supplier conformance
- Outcome Focus: OEE, scrap reduction, on-time-in-full, and cost per unit

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Product Engineering | Manufacturing Product Engineering Lead | Manufacturing Product Engineering Operator |
| Planning & Scheduling | Manufacturing Planning & Scheduling Lead | Manufacturing Planning & Scheduling Operator |
| Procurement | Manufacturing Procurement Lead | Manufacturing Procurement Operator |
| Production | Manufacturing Production Lead | Manufacturing Production Operator |
| Maintenance | Manufacturing Maintenance Lead | Manufacturing Maintenance Operator |
| Quality | Manufacturing Quality Lead | Manufacturing Quality Operator |
| Supply Chain | Manufacturing Supply Chain Lead | Manufacturing Supply Chain Operator |
| Continuous Improvement | Manufacturing Continuous Improvement Lead | Manufacturing Continuous Improvement Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/manufacturing-orchestrator.md](agents/manufacturing-orchestrator.md)
- [agents/manufacturing-product-engineering-lead.md](agents/manufacturing-product-engineering-lead.md)
- [agents/manufacturing-product-engineering-operator.md](agents/manufacturing-product-engineering-operator.md)
- [agents/manufacturing-planning-scheduling-lead.md](agents/manufacturing-planning-scheduling-lead.md)
- [agents/manufacturing-planning-scheduling-operator.md](agents/manufacturing-planning-scheduling-operator.md)
- [agents/manufacturing-procurement-lead.md](agents/manufacturing-procurement-lead.md)
- [agents/manufacturing-procurement-operator.md](agents/manufacturing-procurement-operator.md)
- [agents/manufacturing-production-lead.md](agents/manufacturing-production-lead.md)
- [agents/manufacturing-production-operator.md](agents/manufacturing-production-operator.md)
- [agents/manufacturing-maintenance-lead.md](agents/manufacturing-maintenance-lead.md)
- [agents/manufacturing-maintenance-operator.md](agents/manufacturing-maintenance-operator.md)
- [agents/manufacturing-quality-lead.md](agents/manufacturing-quality-lead.md)
- [agents/manufacturing-quality-operator.md](agents/manufacturing-quality-operator.md)
- [agents/manufacturing-supply-chain-lead.md](agents/manufacturing-supply-chain-lead.md)
- [agents/manufacturing-supply-chain-operator.md](agents/manufacturing-supply-chain-operator.md)
- [agents/manufacturing-continuous-improvement-lead.md](agents/manufacturing-continuous-improvement-lead.md)
- [agents/manufacturing-continuous-improvement-operator.md](agents/manufacturing-continuous-improvement-operator.md)

## Activation Prompt
```
Activate Manufacturing Orchestrator.
Objective: Improve throughput, quality, and reliability from planning through production and fulfillment.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
