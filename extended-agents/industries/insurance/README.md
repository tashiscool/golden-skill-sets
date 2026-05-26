# Insurance Agent Pack

## Scope
This pack defines a full operating model for Insurance with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Optimize underwriting, claims, and servicing to improve combined ratio and policyholder outcomes.
- Risk Focus: pricing drift, claims leakage, fraud, and service latency
- Compliance Focus: state/market regulations, fair-pricing obligations, and audit traceability
- Outcome Focus: combined ratio improvement, cycle time reduction, and retention
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Product & Actuarial | analytics | Insurance Product & Actuarial Lead | Insurance Product & Actuarial Operator |
| Underwriting | adjudication | Insurance Underwriting Lead | Insurance Underwriting Operator |
| Claims | adjudication | Insurance Claims Lead | Insurance Claims Operator |
| Fraud & SIU | adjudication | Insurance Fraud & SIU Lead | Insurance Fraud & SIU Operator |
| Distribution | growth | Insurance Distribution Lead | Insurance Distribution Operator |
| Compliance | governance | Insurance Compliance Lead | Insurance Compliance Operator |
| Customer Service | service | Insurance Customer Service Lead | Insurance Customer Service Operator |
| Portfolio Analytics | analytics | Insurance Portfolio Analytics Lead | Insurance Portfolio Analytics Operator |

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
- Orchestrator: [agents/insurance-orchestrator.md](agents/insurance-orchestrator.md)
- [agents/insurance-product-actuarial-lead.md](agents/insurance-product-actuarial-lead.md)
- [agents/insurance-product-actuarial-operator.md](agents/insurance-product-actuarial-operator.md)
- [agents/insurance-underwriting-lead.md](agents/insurance-underwriting-lead.md)
- [agents/insurance-underwriting-operator.md](agents/insurance-underwriting-operator.md)
- [agents/insurance-claims-lead.md](agents/insurance-claims-lead.md)
- [agents/insurance-claims-operator.md](agents/insurance-claims-operator.md)
- [agents/insurance-fraud-siu-lead.md](agents/insurance-fraud-siu-lead.md)
- [agents/insurance-fraud-siu-operator.md](agents/insurance-fraud-siu-operator.md)
- [agents/insurance-distribution-lead.md](agents/insurance-distribution-lead.md)
- [agents/insurance-distribution-operator.md](agents/insurance-distribution-operator.md)
- [agents/insurance-compliance-lead.md](agents/insurance-compliance-lead.md)
- [agents/insurance-compliance-operator.md](agents/insurance-compliance-operator.md)
- [agents/insurance-customer-service-lead.md](agents/insurance-customer-service-lead.md)
- [agents/insurance-customer-service-operator.md](agents/insurance-customer-service-operator.md)
- [agents/insurance-portfolio-analytics-lead.md](agents/insurance-portfolio-analytics-lead.md)
- [agents/insurance-portfolio-analytics-operator.md](agents/insurance-portfolio-analytics-operator.md)

## Activation Prompt
```
Activate Insurance Orchestrator.
Objective: Optimize underwriting, claims, and servicing to improve combined ratio and policyholder outcomes.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
