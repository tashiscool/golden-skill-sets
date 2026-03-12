# Telecom Agent Pack

## Scope
This pack defines a full operating model for Telecom with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Expand network capacity and service quality while reducing churn and operational cost-to-serve.
- Risk Focus: network incidents, rollout delays, churn spikes, and support backlog
- Compliance Focus: spectrum/regulatory obligations, outage reporting, consumer protections, and security standards
- Outcome Focus: network availability, churn reduction, ARPU quality, and service productivity

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Network Planning | Telecom Network Planning Lead | Telecom Network Planning Operator |
| Build & Deploy | Telecom Build & Deploy Lead | Telecom Build & Deploy Operator |
| NOC Operations | Telecom NOC Operations Lead | Telecom NOC Operations Operator |
| BSS/OSS | Telecom BSS/OSS Lead | Telecom BSS/OSS Operator |
| Customer Support | Telecom Customer Support Lead | Telecom Customer Support Operator |
| Product Bundles | Telecom Product Bundles Lead | Telecom Product Bundles Operator |
| Regulatory | Telecom Regulatory Lead | Telecom Regulatory Operator |
| Churn & Retention Analytics | Telecom Churn & Retention Analytics Lead | Telecom Churn & Retention Analytics Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/telecom-orchestrator.md](agents/telecom-orchestrator.md)
- [agents/telecom-network-planning-lead.md](agents/telecom-network-planning-lead.md)
- [agents/telecom-network-planning-operator.md](agents/telecom-network-planning-operator.md)
- [agents/telecom-build-deploy-lead.md](agents/telecom-build-deploy-lead.md)
- [agents/telecom-build-deploy-operator.md](agents/telecom-build-deploy-operator.md)
- [agents/telecom-noc-operations-lead.md](agents/telecom-noc-operations-lead.md)
- [agents/telecom-noc-operations-operator.md](agents/telecom-noc-operations-operator.md)
- [agents/telecom-bss-oss-lead.md](agents/telecom-bss-oss-lead.md)
- [agents/telecom-bss-oss-operator.md](agents/telecom-bss-oss-operator.md)
- [agents/telecom-customer-support-lead.md](agents/telecom-customer-support-lead.md)
- [agents/telecom-customer-support-operator.md](agents/telecom-customer-support-operator.md)
- [agents/telecom-product-bundles-lead.md](agents/telecom-product-bundles-lead.md)
- [agents/telecom-product-bundles-operator.md](agents/telecom-product-bundles-operator.md)
- [agents/telecom-regulatory-lead.md](agents/telecom-regulatory-lead.md)
- [agents/telecom-regulatory-operator.md](agents/telecom-regulatory-operator.md)
- [agents/telecom-churn-retention-analytics-lead.md](agents/telecom-churn-retention-analytics-lead.md)
- [agents/telecom-churn-retention-analytics-operator.md](agents/telecom-churn-retention-analytics-operator.md)

## Activation Prompt
```
Activate Telecom Orchestrator.
Objective: Expand network capacity and service quality while reducing churn and operational cost-to-serve.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
