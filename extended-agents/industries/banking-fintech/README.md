# Banking & Fintech Agent Pack

## Scope
This pack defines a full operating model for Banking & Fintech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Grow compliant financial products while controlling fraud, credit, and operational risk.
- Risk Focus: fraud loss, underwriting drift, control gaps, and service failures
- Compliance Focus: AML/KYC controls, prudential requirements, consumer protections, and model governance
- Outcome Focus: risk-adjusted growth, loss rates, customer satisfaction, and control effectiveness
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Product | strategy | Banking & Fintech Product Lead | Banking & Fintech Product Operator |
| Risk | governance | Banking & Fintech Risk Lead | Banking & Fintech Risk Operator |
| Compliance & AML | governance | Banking & Fintech Compliance & AML Lead | Banking & Fintech Compliance & AML Operator |
| Underwriting | adjudication | Banking & Fintech Underwriting Lead | Banking & Fintech Underwriting Operator |
| Fraud | adjudication | Banking & Fintech Fraud Lead | Banking & Fintech Fraud Operator |
| Operations | operations | Banking & Fintech Operations Lead | Banking & Fintech Operations Operator |
| Customer Experience | service | Banking & Fintech Customer Experience Lead | Banking & Fintech Customer Experience Operator |
| Data & Model Governance | governance | Banking & Fintech Data & Model Governance Lead | Banking & Fintech Data & Model Governance Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
