# Logistics & Supply Chain Agent Pack

## Scope
This pack defines a full operating model for Logistics & Supply Chain with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver resilient, cost-efficient end-to-end logistics performance across global networks.
- Risk Focus: forecast misses, network bottlenecks, customs delays, and last-mile service failures
- Compliance Focus: trade compliance, carrier contracts, safety controls, and customer SLAs
- Outcome Focus: OTIF, total landed cost, cycle time, and exception reduction
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Demand Planning | analytics | Logistics & Supply Chain Demand Planning Lead | Logistics & Supply Chain Demand Planning Operator |
| Procurement | operations | Logistics & Supply Chain Procurement Lead | Logistics & Supply Chain Procurement Operator |
| Warehousing | operations | Logistics & Supply Chain Warehousing Lead | Logistics & Supply Chain Warehousing Operator |
| Transportation | operations | Logistics & Supply Chain Transportation Lead | Logistics & Supply Chain Transportation Operator |
| Customs & Trade | governance | Logistics & Supply Chain Customs & Trade Lead | Logistics & Supply Chain Customs & Trade Operator |
| Last-Mile | operations | Logistics & Supply Chain Last-Mile Lead | Logistics & Supply Chain Last-Mile Operator |
| Network Optimization | analytics | Logistics & Supply Chain Network Optimization Lead | Logistics & Supply Chain Network Optimization Operator |
| Control Tower Analytics | analytics | Logistics & Supply Chain Control Tower Analytics Lead | Logistics & Supply Chain Control Tower Analytics Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
