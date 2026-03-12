# Pharma & Biotech Agent Pack

## Scope
This pack defines a full operating model for Pharma & Biotech with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Advance assets from discovery through commercialization with scientific rigor and regulatory readiness.
- Risk Focus: trial delays, safety signal handling, CMC constraints, and access barriers
- Compliance Focus: GxP controls, trial governance, adverse event reporting, and submission standards
- Outcome Focus: milestone velocity, study quality, approval readiness, and launch uptake

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Discovery | Pharma & Biotech Discovery Lead | Pharma & Biotech Discovery Operator |
| Preclinical | Pharma & Biotech Preclinical Lead | Pharma & Biotech Preclinical Operator |
| Clinical Trials | Pharma & Biotech Clinical Trials Lead | Pharma & Biotech Clinical Trials Operator |
| Regulatory Affairs | Pharma & Biotech Regulatory Affairs Lead | Pharma & Biotech Regulatory Affairs Operator |
| Pharmacovigilance | Pharma & Biotech Pharmacovigilance Lead | Pharma & Biotech Pharmacovigilance Operator |
| Manufacturing | Pharma & Biotech Manufacturing Lead | Pharma & Biotech Manufacturing Operator |
| Medical Affairs | Pharma & Biotech Medical Affairs Lead | Pharma & Biotech Medical Affairs Operator |
| Market Access | Pharma & Biotech Market Access Lead | Pharma & Biotech Market Access Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/pharma-biotech-orchestrator.md](agents/pharma-biotech-orchestrator.md)
- [agents/pharma-biotech-discovery-lead.md](agents/pharma-biotech-discovery-lead.md)
- [agents/pharma-biotech-discovery-operator.md](agents/pharma-biotech-discovery-operator.md)
- [agents/pharma-biotech-preclinical-lead.md](agents/pharma-biotech-preclinical-lead.md)
- [agents/pharma-biotech-preclinical-operator.md](agents/pharma-biotech-preclinical-operator.md)
- [agents/pharma-biotech-clinical-trials-lead.md](agents/pharma-biotech-clinical-trials-lead.md)
- [agents/pharma-biotech-clinical-trials-operator.md](agents/pharma-biotech-clinical-trials-operator.md)
- [agents/pharma-biotech-regulatory-affairs-lead.md](agents/pharma-biotech-regulatory-affairs-lead.md)
- [agents/pharma-biotech-regulatory-affairs-operator.md](agents/pharma-biotech-regulatory-affairs-operator.md)
- [agents/pharma-biotech-pharmacovigilance-lead.md](agents/pharma-biotech-pharmacovigilance-lead.md)
- [agents/pharma-biotech-pharmacovigilance-operator.md](agents/pharma-biotech-pharmacovigilance-operator.md)
- [agents/pharma-biotech-manufacturing-lead.md](agents/pharma-biotech-manufacturing-lead.md)
- [agents/pharma-biotech-manufacturing-operator.md](agents/pharma-biotech-manufacturing-operator.md)
- [agents/pharma-biotech-medical-affairs-lead.md](agents/pharma-biotech-medical-affairs-lead.md)
- [agents/pharma-biotech-medical-affairs-operator.md](agents/pharma-biotech-medical-affairs-operator.md)
- [agents/pharma-biotech-market-access-lead.md](agents/pharma-biotech-market-access-lead.md)
- [agents/pharma-biotech-market-access-operator.md](agents/pharma-biotech-market-access-operator.md)

## Activation Prompt
```
Activate Pharma & Biotech Orchestrator.
Objective: Advance assets from discovery through commercialization with scientific rigor and regulatory readiness.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
