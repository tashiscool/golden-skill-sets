# Legal Services Agent Pack

## Scope
This pack defines a full operating model for Legal Services with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Deliver high-quality legal work with predictable matter economics and defensible process controls.
- Risk Focus: missed deadlines, inconsistent drafting quality, discovery errors, and billing disputes
- Compliance Focus: ethics obligations, privilege/confidentiality controls, and jurisdictional requirements
- Outcome Focus: matter outcomes, cycle time, realization rate, and client satisfaction
- Human Approval Required: yes

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Intake | adjudication | Legal Services Intake Lead | Legal Services Intake Operator |
| Matter Management | operations | Legal Services Matter Management Lead | Legal Services Matter Management Operator |
| Research | knowledge | Legal Services Research Lead | Legal Services Research Operator |
| Drafting & Review | knowledge | Legal Services Drafting & Review Lead | Legal Services Drafting & Review Operator |
| Litigation Support | operations | Legal Services Litigation Support Lead | Legal Services Litigation Support Operator |
| eDiscovery | knowledge | Legal Services eDiscovery Lead | Legal Services eDiscovery Operator |
| Billing | adjudication | Legal Services Billing Lead | Legal Services Billing Operator |
| Compliance | governance | Legal Services Compliance Lead | Legal Services Compliance Operator |

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
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
