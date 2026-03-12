# Banking & Fintech Agent Pack

## Scope
This pack defines a full operating model for Banking & Fintech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Grow compliant financial products while controlling fraud, credit, and operational risk.
- Risk Focus: fraud loss, underwriting drift, control gaps, and service failures
- Compliance Focus: AML/KYC controls, prudential requirements, consumer protections, and model governance
- Outcome Focus: risk-adjusted growth, loss rates, customer satisfaction, and control effectiveness

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Product | Banking & Fintech Product Lead | Banking & Fintech Product Operator |
| Risk | Banking & Fintech Risk Lead | Banking & Fintech Risk Operator |
| Compliance & AML | Banking & Fintech Compliance & AML Lead | Banking & Fintech Compliance & AML Operator |
| Underwriting | Banking & Fintech Underwriting Lead | Banking & Fintech Underwriting Operator |
| Fraud | Banking & Fintech Fraud Lead | Banking & Fintech Fraud Operator |
| Operations | Banking & Fintech Operations Lead | Banking & Fintech Operations Operator |
| Customer Experience | Banking & Fintech Customer Experience Lead | Banking & Fintech Customer Experience Operator |
| Data & Model Governance | Banking & Fintech Data & Model Governance Lead | Banking & Fintech Data & Model Governance Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/banking-fintech-orchestrator.md](agents/banking-fintech-orchestrator.md)
- [agents/banking-fintech-product-lead.md](agents/banking-fintech-product-lead.md)
- [agents/banking-fintech-product-operator.md](agents/banking-fintech-product-operator.md)
- [agents/banking-fintech-risk-lead.md](agents/banking-fintech-risk-lead.md)
- [agents/banking-fintech-risk-operator.md](agents/banking-fintech-risk-operator.md)
- [agents/banking-fintech-compliance-aml-lead.md](agents/banking-fintech-compliance-aml-lead.md)
- [agents/banking-fintech-compliance-aml-operator.md](agents/banking-fintech-compliance-aml-operator.md)
- [agents/banking-fintech-underwriting-lead.md](agents/banking-fintech-underwriting-lead.md)
- [agents/banking-fintech-underwriting-operator.md](agents/banking-fintech-underwriting-operator.md)
- [agents/banking-fintech-fraud-lead.md](agents/banking-fintech-fraud-lead.md)
- [agents/banking-fintech-fraud-operator.md](agents/banking-fintech-fraud-operator.md)
- [agents/banking-fintech-operations-lead.md](agents/banking-fintech-operations-lead.md)
- [agents/banking-fintech-operations-operator.md](agents/banking-fintech-operations-operator.md)
- [agents/banking-fintech-customer-experience-lead.md](agents/banking-fintech-customer-experience-lead.md)
- [agents/banking-fintech-customer-experience-operator.md](agents/banking-fintech-customer-experience-operator.md)
- [agents/banking-fintech-data-model-governance-lead.md](agents/banking-fintech-data-model-governance-lead.md)
- [agents/banking-fintech-data-model-governance-operator.md](agents/banking-fintech-data-model-governance-operator.md)

## Activation Prompt
```
Activate Banking & Fintech Orchestrator.
Objective: Grow compliant financial products while controlling fraud, credit, and operational risk.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
