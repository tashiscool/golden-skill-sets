# Legal Services Agent Pack

## Scope
This pack defines a full operating model for Legal Services with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver high-quality legal work with predictable matter economics and defensible process controls.
- Risk Focus: missed deadlines, inconsistent drafting quality, discovery errors, and billing disputes
- Compliance Focus: ethics obligations, privilege/confidentiality controls, and jurisdictional requirements
- Outcome Focus: matter outcomes, cycle time, realization rate, and client satisfaction

## Division Map
| Division | Lead Agent | Operator Agent |
|---|---|---|
| Intake | Legal Services Intake Lead | Legal Services Intake Operator |
| Matter Management | Legal Services Matter Management Lead | Legal Services Matter Management Operator |
| Research | Legal Services Research Lead | Legal Services Research Operator |
| Drafting & Review | Legal Services Drafting & Review Lead | Legal Services Drafting & Review Operator |
| Litigation Support | Legal Services Litigation Support Lead | Legal Services Litigation Support Operator |
| eDiscovery | Legal Services eDiscovery Lead | Legal Services eDiscovery Operator |
| Billing | Legal Services Billing Lead | Legal Services Billing Operator |
| Compliance | Legal Services Compliance Lead | Legal Services Compliance Operator |

## Stage-Gate Model
1. Discovery: baseline metrics, risk framing, and scope boundaries.
2. Planning: roadmap, owners, dependencies, and acceptance criteria.
3. Execution: lead/operator delivery loops by division.
4. Validation: QA/compliance checks with evidence artifacts.
5. Launch/Ops: handover completeness and operating review cadence.

## Agent Files
- Orchestrator: [agents/legal-services-orchestrator.md](agents/legal-services-orchestrator.md)
- [agents/legal-services-intake-lead.md](agents/legal-services-intake-lead.md)
- [agents/legal-services-intake-operator.md](agents/legal-services-intake-operator.md)
- [agents/legal-services-matter-management-lead.md](agents/legal-services-matter-management-lead.md)
- [agents/legal-services-matter-management-operator.md](agents/legal-services-matter-management-operator.md)
- [agents/legal-services-research-lead.md](agents/legal-services-research-lead.md)
- [agents/legal-services-research-operator.md](agents/legal-services-research-operator.md)
- [agents/legal-services-drafting-review-lead.md](agents/legal-services-drafting-review-lead.md)
- [agents/legal-services-drafting-review-operator.md](agents/legal-services-drafting-review-operator.md)
- [agents/legal-services-litigation-support-lead.md](agents/legal-services-litigation-support-lead.md)
- [agents/legal-services-litigation-support-operator.md](agents/legal-services-litigation-support-operator.md)
- [agents/legal-services-ediscovery-lead.md](agents/legal-services-ediscovery-lead.md)
- [agents/legal-services-ediscovery-operator.md](agents/legal-services-ediscovery-operator.md)
- [agents/legal-services-billing-lead.md](agents/legal-services-billing-lead.md)
- [agents/legal-services-billing-operator.md](agents/legal-services-billing-operator.md)
- [agents/legal-services-compliance-lead.md](agents/legal-services-compliance-lead.md)
- [agents/legal-services-compliance-operator.md](agents/legal-services-compliance-operator.md)

## Activation Prompt
```
Activate Legal Services Orchestrator.
Objective: Deliver high-quality legal work with predictable matter economics and defensible process controls.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require lead/operator handoffs in every division and escalate critical blockers within one cycle.
```
