# Beauty & Personal Care Agent Pack

## Scope
This pack defines a full operating model for Beauty & Personal Care with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Scale compliant product portfolios with strong launch execution across DTC, retail, and trade channels.
- Risk Focus: formula/regulatory delays, quality incidents, and weak launch conversion
- Compliance Focus: ingredient/claims compliance, labeling, stability requirements, and safety reporting
- Outcome Focus: velocity per SKU, repeat rate, gross margin, and safety incident rate
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Product Development | knowledge | Beauty & Personal Care Product Development Lead | Beauty & Personal Care Product Development Operator |
| Regulatory | governance | Beauty & Personal Care Regulatory Lead | Beauty & Personal Care Regulatory Operator |
| Manufacturing | operations | Beauty & Personal Care Manufacturing Lead | Beauty & Personal Care Manufacturing Operator |
| Brand Marketing | growth | Beauty & Personal Care Brand Marketing Lead | Beauty & Personal Care Brand Marketing Operator |
| Trade Marketing | growth | Beauty & Personal Care Trade Marketing Lead | Beauty & Personal Care Trade Marketing Operator |
| DTC | growth | Beauty & Personal Care DTC Lead | Beauty & Personal Care DTC Operator |
| Education | service | Beauty & Personal Care Education Lead | Beauty & Personal Care Education Operator |
| Quality & Safety | governance | Beauty & Personal Care Quality & Safety Lead | Beauty & Personal Care Quality & Safety Operator |

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
- Orchestrator: [agents/beauty-personal-care-orchestrator.md](agents/beauty-personal-care-orchestrator.md)
- [agents/beauty-personal-care-product-development-lead.md](agents/beauty-personal-care-product-development-lead.md)
- [agents/beauty-personal-care-product-development-operator.md](agents/beauty-personal-care-product-development-operator.md)
- [agents/beauty-personal-care-regulatory-lead.md](agents/beauty-personal-care-regulatory-lead.md)
- [agents/beauty-personal-care-regulatory-operator.md](agents/beauty-personal-care-regulatory-operator.md)
- [agents/beauty-personal-care-manufacturing-lead.md](agents/beauty-personal-care-manufacturing-lead.md)
- [agents/beauty-personal-care-manufacturing-operator.md](agents/beauty-personal-care-manufacturing-operator.md)
- [agents/beauty-personal-care-brand-marketing-lead.md](agents/beauty-personal-care-brand-marketing-lead.md)
- [agents/beauty-personal-care-brand-marketing-operator.md](agents/beauty-personal-care-brand-marketing-operator.md)
- [agents/beauty-personal-care-trade-marketing-lead.md](agents/beauty-personal-care-trade-marketing-lead.md)
- [agents/beauty-personal-care-trade-marketing-operator.md](agents/beauty-personal-care-trade-marketing-operator.md)
- [agents/beauty-personal-care-dtc-lead.md](agents/beauty-personal-care-dtc-lead.md)
- [agents/beauty-personal-care-dtc-operator.md](agents/beauty-personal-care-dtc-operator.md)
- [agents/beauty-personal-care-education-lead.md](agents/beauty-personal-care-education-lead.md)
- [agents/beauty-personal-care-education-operator.md](agents/beauty-personal-care-education-operator.md)
- [agents/beauty-personal-care-quality-safety-lead.md](agents/beauty-personal-care-quality-safety-lead.md)
- [agents/beauty-personal-care-quality-safety-operator.md](agents/beauty-personal-care-quality-safety-operator.md)

## Activation Prompt
```
Activate Beauty & Personal Care Orchestrator.
Objective: Scale compliant product portfolios with strong launch execution across DTC, retail, and trade channels.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
