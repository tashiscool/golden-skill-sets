# Insurance Agent Pack

## Scope
This pack defines a full operating model for Insurance with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Optimize underwriting, claims, and servicing to improve combined ratio and policyholder outcomes.
- Risk Focus: pricing drift, claims leakage, fraud, and service latency
- Compliance Focus: state/market regulations, fair-pricing obligations, and audit traceability
- Outcome Focus: combined ratio improvement, cycle time reduction, and retention

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Product & Actuarial | Insurance Product & Actuarial Lead | Insurance Product & Actuarial Operator |
| Underwriting | Insurance Underwriting Lead | Insurance Underwriting Operator |
| Claims | Insurance Claims Lead | Insurance Claims Operator |
| Fraud & SIU | Insurance Fraud & SIU Lead | Insurance Fraud & SIU Operator |
| Distribution | Insurance Distribution Lead | Insurance Distribution Operator |
| Compliance | Insurance Compliance Lead | Insurance Compliance Operator |
| Customer Service | Insurance Customer Service Lead | Insurance Customer Service Operator |
| Portfolio Analytics | Insurance Portfolio Analytics Lead | Insurance Portfolio Analytics Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

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
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
