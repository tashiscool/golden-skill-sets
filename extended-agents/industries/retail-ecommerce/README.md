# Retail & E-commerce Agent Pack

## Scope
This pack defines a full operating model for Retail & E-commerce with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Optimize assortment, inventory, and channel execution to maximize profitable growth online and in-store.
- Risk Focus: stockouts/overstock, pricing errors, fulfillment failures, and return-rate inflation
- Compliance Focus: consumer protection, payments/privacy controls, marketplace rules, and tax obligations
- Outcome Focus: gross margin return on inventory, conversion, AOV, and service-level attainment
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Merchandising | strategy | Retail & E-commerce Merchandising Lead | Retail & E-commerce Merchandising Operator |
| Inventory | operations | Retail & E-commerce Inventory Lead | Retail & E-commerce Inventory Operator |
| Pricing & Promotions | growth | Retail & E-commerce Pricing & Promotions Lead | Retail & E-commerce Pricing & Promotions Operator |
| Store Operations | operations | Retail & E-commerce Store Operations Lead | Retail & E-commerce Store Operations Operator |
| E-commerce Operations | operations | Retail & E-commerce E-commerce Operations Lead | Retail & E-commerce E-commerce Operations Operator |
| CRM & Loyalty | growth | Retail & E-commerce CRM & Loyalty Lead | Retail & E-commerce CRM & Loyalty Operator |
| Marketplace Operations | operations | Retail & E-commerce Marketplace Operations Lead | Retail & E-commerce Marketplace Operations Operator |
| Support | service | Retail & E-commerce Support Lead | Retail & E-commerce Support Operator |

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
- Orchestrator: [agents/retail-ecommerce-orchestrator.md](agents/retail-ecommerce-orchestrator.md)
- [agents/retail-ecommerce-merchandising-lead.md](agents/retail-ecommerce-merchandising-lead.md)
- [agents/retail-ecommerce-merchandising-operator.md](agents/retail-ecommerce-merchandising-operator.md)
- [agents/retail-ecommerce-inventory-lead.md](agents/retail-ecommerce-inventory-lead.md)
- [agents/retail-ecommerce-inventory-operator.md](agents/retail-ecommerce-inventory-operator.md)
- [agents/retail-ecommerce-pricing-promotions-lead.md](agents/retail-ecommerce-pricing-promotions-lead.md)
- [agents/retail-ecommerce-pricing-promotions-operator.md](agents/retail-ecommerce-pricing-promotions-operator.md)
- [agents/retail-ecommerce-store-operations-lead.md](agents/retail-ecommerce-store-operations-lead.md)
- [agents/retail-ecommerce-store-operations-operator.md](agents/retail-ecommerce-store-operations-operator.md)
- [agents/retail-ecommerce-e-commerce-operations-lead.md](agents/retail-ecommerce-e-commerce-operations-lead.md)
- [agents/retail-ecommerce-e-commerce-operations-operator.md](agents/retail-ecommerce-e-commerce-operations-operator.md)
- [agents/retail-ecommerce-crm-loyalty-lead.md](agents/retail-ecommerce-crm-loyalty-lead.md)
- [agents/retail-ecommerce-crm-loyalty-operator.md](agents/retail-ecommerce-crm-loyalty-operator.md)
- [agents/retail-ecommerce-marketplace-operations-lead.md](agents/retail-ecommerce-marketplace-operations-lead.md)
- [agents/retail-ecommerce-marketplace-operations-operator.md](agents/retail-ecommerce-marketplace-operations-operator.md)
- [agents/retail-ecommerce-support-lead.md](agents/retail-ecommerce-support-lead.md)
- [agents/retail-ecommerce-support-operator.md](agents/retail-ecommerce-support-operator.md)

## Activation Prompt
```
Activate Retail & E-commerce Orchestrator.
Objective: Optimize assortment, inventory, and channel execution to maximize profitable growth online and in-store.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
