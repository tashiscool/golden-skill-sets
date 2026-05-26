# Telecom Agent Pack

## Scope
This pack defines a full operating model for Telecom with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Expand network capacity and service quality while reducing churn and operational cost-to-serve.
- Risk Focus: network incidents, rollout delays, churn spikes, and support backlog
- Compliance Focus: spectrum/regulatory obligations, outage reporting, consumer protections, and security standards
- Outcome Focus: network availability, churn reduction, ARPU quality, and service productivity
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Network Planning | technical | Telecom Network Planning Lead | Telecom Network Planning Operator |
| Build & Deploy | operations | Telecom Build & Deploy Lead | Telecom Build & Deploy Operator |
| NOC Operations | technical | Telecom NOC Operations Lead | Telecom NOC Operations Operator |
| BSS/OSS | technical | Telecom BSS/OSS Lead | Telecom BSS/OSS Operator |
| Customer Support | service | Telecom Customer Support Lead | Telecom Customer Support Operator |
| Product Bundles | growth | Telecom Product Bundles Lead | Telecom Product Bundles Operator |
| Regulatory | governance | Telecom Regulatory Lead | Telecom Regulatory Operator |
| Churn & Retention Analytics | analytics | Telecom Churn & Retention Analytics Lead | Telecom Churn & Retention Analytics Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
