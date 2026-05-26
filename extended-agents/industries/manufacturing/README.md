# Manufacturing Agent Pack

## Scope
This pack defines a full operating model for Manufacturing with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Improve throughput, quality, and reliability from planning through production and fulfillment.
- Risk Focus: line downtime, quality escapes, supply disruptions, and planning instability
- Compliance Focus: process controls, safety standards, traceability, and supplier conformance
- Outcome Focus: OEE, scrap reduction, on-time-in-full, and cost per unit
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Product Engineering | technical | Manufacturing Product Engineering Lead | Manufacturing Product Engineering Operator |
| Planning & Scheduling | operations | Manufacturing Planning & Scheduling Lead | Manufacturing Planning & Scheduling Operator |
| Procurement | operations | Manufacturing Procurement Lead | Manufacturing Procurement Operator |
| Production | operations | Manufacturing Production Lead | Manufacturing Production Operator |
| Maintenance | operations | Manufacturing Maintenance Lead | Manufacturing Maintenance Operator |
| Quality | governance | Manufacturing Quality Lead | Manufacturing Quality Operator |
| Supply Chain | operations | Manufacturing Supply Chain Lead | Manufacturing Supply Chain Operator |
| Continuous Improvement | analytics | Manufacturing Continuous Improvement Lead | Manufacturing Continuous Improvement Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
