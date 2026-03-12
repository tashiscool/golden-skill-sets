# Logistics & Supply Chain Agent Pack

## Scope
This pack defines a full operating model for Logistics & Supply Chain with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver resilient, cost-efficient end-to-end logistics performance across global networks.
- Risk Focus: forecast misses, network bottlenecks, customs delays, and last-mile service failures
- Compliance Focus: trade compliance, carrier contracts, safety controls, and customer SLAs
- Outcome Focus: OTIF, total landed cost, cycle time, and exception reduction

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Demand Planning | Logistics & Supply Chain Demand Planning Lead | Logistics & Supply Chain Demand Planning Operator |
| Procurement | Logistics & Supply Chain Procurement Lead | Logistics & Supply Chain Procurement Operator |
| Warehousing | Logistics & Supply Chain Warehousing Lead | Logistics & Supply Chain Warehousing Operator |
| Transportation | Logistics & Supply Chain Transportation Lead | Logistics & Supply Chain Transportation Operator |
| Customs & Trade | Logistics & Supply Chain Customs & Trade Lead | Logistics & Supply Chain Customs & Trade Operator |
| Last-Mile | Logistics & Supply Chain Last-Mile Lead | Logistics & Supply Chain Last-Mile Operator |
| Network Optimization | Logistics & Supply Chain Network Optimization Lead | Logistics & Supply Chain Network Optimization Operator |
| Control Tower Analytics | Logistics & Supply Chain Control Tower Analytics Lead | Logistics & Supply Chain Control Tower Analytics Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/logistics-supply-chain-orchestrator.md](agents/logistics-supply-chain-orchestrator.md)
- [agents/logistics-supply-chain-demand-planning-lead.md](agents/logistics-supply-chain-demand-planning-lead.md)
- [agents/logistics-supply-chain-demand-planning-operator.md](agents/logistics-supply-chain-demand-planning-operator.md)
- [agents/logistics-supply-chain-procurement-lead.md](agents/logistics-supply-chain-procurement-lead.md)
- [agents/logistics-supply-chain-procurement-operator.md](agents/logistics-supply-chain-procurement-operator.md)
- [agents/logistics-supply-chain-warehousing-lead.md](agents/logistics-supply-chain-warehousing-lead.md)
- [agents/logistics-supply-chain-warehousing-operator.md](agents/logistics-supply-chain-warehousing-operator.md)
- [agents/logistics-supply-chain-transportation-lead.md](agents/logistics-supply-chain-transportation-lead.md)
- [agents/logistics-supply-chain-transportation-operator.md](agents/logistics-supply-chain-transportation-operator.md)
- [agents/logistics-supply-chain-customs-trade-lead.md](agents/logistics-supply-chain-customs-trade-lead.md)
- [agents/logistics-supply-chain-customs-trade-operator.md](agents/logistics-supply-chain-customs-trade-operator.md)
- [agents/logistics-supply-chain-last-mile-lead.md](agents/logistics-supply-chain-last-mile-lead.md)
- [agents/logistics-supply-chain-last-mile-operator.md](agents/logistics-supply-chain-last-mile-operator.md)
- [agents/logistics-supply-chain-network-optimization-lead.md](agents/logistics-supply-chain-network-optimization-lead.md)
- [agents/logistics-supply-chain-network-optimization-operator.md](agents/logistics-supply-chain-network-optimization-operator.md)
- [agents/logistics-supply-chain-control-tower-analytics-lead.md](agents/logistics-supply-chain-control-tower-analytics-lead.md)
- [agents/logistics-supply-chain-control-tower-analytics-operator.md](agents/logistics-supply-chain-control-tower-analytics-operator.md)

## Activation Prompt
```
Activate Logistics & Supply Chain Orchestrator.
Objective: Deliver resilient, cost-efficient end-to-end logistics performance across global networks.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
