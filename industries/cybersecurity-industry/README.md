# Cybersecurity Agent Pack

## Scope
This pack defines a full operating model for Cybersecurity with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Reduce threat exposure and response time through integrated prevention, detection, and recovery operations.
- Risk Focus: control gaps, alert fatigue, delayed containment, and policy drift
- Compliance Focus: security frameworks, audit requirements, incident reporting, and identity governance
- Outcome Focus: risk reduction, detection/response speed, control coverage, and audit pass rate

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Threat Intelligence | Cybersecurity Threat Intelligence Lead | Cybersecurity Threat Intelligence Operator |
| Security Engineering | Cybersecurity Security Engineering Lead | Cybersecurity Security Engineering Operator |
| SOC | Cybersecurity SOC Lead | Cybersecurity SOC Operator |
| Incident Response | Cybersecurity Incident Response Lead | Cybersecurity Incident Response Operator |
| GRC | Cybersecurity GRC Lead | Cybersecurity GRC Operator |
| IAM | Cybersecurity IAM Lead | Cybersecurity IAM Operator |
| AppSec | Cybersecurity AppSec Lead | Cybersecurity AppSec Operator |
| Security Education | Cybersecurity Security Education Lead | Cybersecurity Security Education Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/cybersecurity-industry-orchestrator.md](agents/cybersecurity-industry-orchestrator.md)
- [agents/cybersecurity-industry-threat-intelligence-lead.md](agents/cybersecurity-industry-threat-intelligence-lead.md)
- [agents/cybersecurity-industry-threat-intelligence-operator.md](agents/cybersecurity-industry-threat-intelligence-operator.md)
- [agents/cybersecurity-industry-security-engineering-lead.md](agents/cybersecurity-industry-security-engineering-lead.md)
- [agents/cybersecurity-industry-security-engineering-operator.md](agents/cybersecurity-industry-security-engineering-operator.md)
- [agents/cybersecurity-industry-soc-lead.md](agents/cybersecurity-industry-soc-lead.md)
- [agents/cybersecurity-industry-soc-operator.md](agents/cybersecurity-industry-soc-operator.md)
- [agents/cybersecurity-industry-incident-response-lead.md](agents/cybersecurity-industry-incident-response-lead.md)
- [agents/cybersecurity-industry-incident-response-operator.md](agents/cybersecurity-industry-incident-response-operator.md)
- [agents/cybersecurity-industry-grc-lead.md](agents/cybersecurity-industry-grc-lead.md)
- [agents/cybersecurity-industry-grc-operator.md](agents/cybersecurity-industry-grc-operator.md)
- [agents/cybersecurity-industry-iam-lead.md](agents/cybersecurity-industry-iam-lead.md)
- [agents/cybersecurity-industry-iam-operator.md](agents/cybersecurity-industry-iam-operator.md)
- [agents/cybersecurity-industry-appsec-lead.md](agents/cybersecurity-industry-appsec-lead.md)
- [agents/cybersecurity-industry-appsec-operator.md](agents/cybersecurity-industry-appsec-operator.md)
- [agents/cybersecurity-industry-security-education-lead.md](agents/cybersecurity-industry-security-education-lead.md)
- [agents/cybersecurity-industry-security-education-operator.md](agents/cybersecurity-industry-security-education-operator.md)

## Activation Prompt
```
Activate Cybersecurity Orchestrator.
Objective: Reduce threat exposure and response time through integrated prevention, detection, and recovery operations.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
