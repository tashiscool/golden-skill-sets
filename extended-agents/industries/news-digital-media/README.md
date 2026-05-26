# News & Digital Media Agent Pack

## Scope
This pack defines a full operating model for News & Digital Media with one orchestrator and paired lead/operator agents for each division.

## Industry Context
- Objective: Publish trusted, high-velocity journalism that grows audience, subscription, and advertiser value.
- Risk Focus: fact errors, legal exposure, churn, and monetization volatility
- Compliance Focus: editorial standards, defamation/privacy controls, platform policy, and ad disclosure
- Outcome Focus: engagement depth, subscriber growth, retention, and revenue mix stability
- Human Approval Required: only for external writes, irreversible actions, or public-facing launches

## Division Map
| Division | Profile | Lead Agent | Operator Agent |
|---|---|---|---|
| Editorial | creative | News & Digital Media Editorial Lead | News & Digital Media Editorial Operator |
| Fact-Checking | governance | News & Digital Media Fact-Checking Lead | News & Digital Media Fact-Checking Operator |
| Multimedia Production | creative | News & Digital Media Multimedia Production Lead | News & Digital Media Multimedia Production Operator |
| Audience Growth | growth | News & Digital Media Audience Growth Lead | News & Digital Media Audience Growth Operator |
| Subscription | growth | News & Digital Media Subscription Lead | News & Digital Media Subscription Operator |
| Ad Sales | growth | News & Digital Media Ad Sales Lead | News & Digital Media Ad Sales Operator |
| Standards & Legal | governance | News & Digital Media Standards & Legal Lead | News & Digital Media Standards & Legal Operator |
| Analytics | analytics | News & Digital Media Analytics Lead | News & Digital Media Analytics Operator |

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
- Orchestrator: [agents/news-digital-media-orchestrator.md](agents/news-digital-media-orchestrator.md)
- [agents/news-digital-media-editorial-lead.md](agents/news-digital-media-editorial-lead.md)
- [agents/news-digital-media-editorial-operator.md](agents/news-digital-media-editorial-operator.md)
- [agents/news-digital-media-fact-checking-lead.md](agents/news-digital-media-fact-checking-lead.md)
- [agents/news-digital-media-fact-checking-operator.md](agents/news-digital-media-fact-checking-operator.md)
- [agents/news-digital-media-multimedia-production-lead.md](agents/news-digital-media-multimedia-production-lead.md)
- [agents/news-digital-media-multimedia-production-operator.md](agents/news-digital-media-multimedia-production-operator.md)
- [agents/news-digital-media-audience-growth-lead.md](agents/news-digital-media-audience-growth-lead.md)
- [agents/news-digital-media-audience-growth-operator.md](agents/news-digital-media-audience-growth-operator.md)
- [agents/news-digital-media-subscription-lead.md](agents/news-digital-media-subscription-lead.md)
- [agents/news-digital-media-subscription-operator.md](agents/news-digital-media-subscription-operator.md)
- [agents/news-digital-media-ad-sales-lead.md](agents/news-digital-media-ad-sales-lead.md)
- [agents/news-digital-media-ad-sales-operator.md](agents/news-digital-media-ad-sales-operator.md)
- [agents/news-digital-media-standards-legal-lead.md](agents/news-digital-media-standards-legal-lead.md)
- [agents/news-digital-media-standards-legal-operator.md](agents/news-digital-media-standards-legal-operator.md)
- [agents/news-digital-media-analytics-lead.md](agents/news-digital-media-analytics-lead.md)
- [agents/news-digital-media-analytics-operator.md](agents/news-digital-media-analytics-operator.md)

## Activation Prompt
```
Activate News & Digital Media Orchestrator.
Objective: Publish trusted, high-velocity journalism that grows audience, subscription, and advertiser value.
Run the stage-gate model end to end with evidence-backed pass/fail decisions.
Require structured outputs, explicit citations for policy claims, and human approval before consequential actions.
```
