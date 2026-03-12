#!/usr/bin/env python3
"""Generate full industry agent packs for The Agency.

This generator creates 30 industry packs under industries/ with:
- 1 orchestrator agent per industry
- 1 lead + 1 operator agent per division
- per-industry README + master matrix

The content is domain-tailored by industry context and division function profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import shutil


@dataclass(frozen=True)
class Industry:
    slug: str
    name: str
    objective: str
    risk_focus: str
    compliance_focus: str
    outcome_focus: str
    divisions: tuple[str, ...]


INDUSTRIES: tuple[Industry, ...] = (
    Industry(
        slug="film-tv",
        name="Film & TV",
        objective="Develop, produce, and monetize scripted and unscripted slate work across theatrical, broadcast, and streaming windows.",
        risk_focus="budget overruns, schedule slips, union breaches, and rights/clearance failures",
        compliance_focus="guild agreements, location permitting, music/clip clearances, and delivery contracts",
        outcome_focus="on-time delivery, variance-to-budget, completion quality, and audience completion/engagement",
        divisions=(
            "Development",
            "Pre-Production",
            "Production",
            "Post-Production",
            "Distribution",
            "Marketing & PR",
            "Talent & Unions",
            "Business Affairs",
        ),
    ),
    Industry(
        slug="books-publishing",
        name="Books & Publishing",
        objective="Acquire, produce, and scale profitable title portfolios across print, digital, and audio channels.",
        risk_focus="acquisition miss-rate, title launch slippage, rights disputes, and inventory imbalance",
        compliance_focus="rights chain-of-title, contract terms, metadata standards, and market-specific regulations",
        outcome_focus="sell-through, margin by title, release predictability, and author/list growth",
        divisions=(
            "Acquisitions",
            "Editorial",
            "Design & Typesetting",
            "Production",
            "Rights & Licensing",
            "Sales & Distribution",
            "Publicity",
            "Author Relations",
        ),
    ),
    Industry(
        slug="music",
        name="Music",
        objective="Build sustainable artist and catalog growth across recorded music, publishing, live, and merchandise.",
        risk_focus="rights disputes, royalty leakage, tour execution risk, and underperforming releases",
        compliance_focus="publishing splits, neighboring rights, venue/compliance terms, and royalty reporting accuracy",
        outcome_focus="stream share, catalog growth, tour profitability, and royalty accuracy",
        divisions=(
            "A&R",
            "Recording & Production",
            "Publishing & Rights",
            "Distribution",
            "Touring & Live",
            "Marketing",
            "Merchandising",
            "Royalty Operations",
        ),
    ),
    Industry(
        slug="news-digital-media",
        name="News & Digital Media",
        objective="Publish trusted, high-velocity journalism that grows audience, subscription, and advertiser value.",
        risk_focus="fact errors, legal exposure, churn, and monetization volatility",
        compliance_focus="editorial standards, defamation/privacy controls, platform policy, and ad disclosure",
        outcome_focus="engagement depth, subscriber growth, retention, and revenue mix stability",
        divisions=(
            "Editorial",
            "Fact-Checking",
            "Multimedia Production",
            "Audience Growth",
            "Subscription",
            "Ad Sales",
            "Standards & Legal",
            "Analytics",
        ),
    ),
    Industry(
        slug="gaming",
        name="Gaming",
        objective="Ship and operate high-retention game experiences with healthy live operations and monetization.",
        risk_focus="scope creep, quality regressions, liveops instability, and economy imbalance",
        compliance_focus="platform certification, content/rating standards, privacy obligations, and anti-cheat policy",
        outcome_focus="retention, ARPDAU, release quality, and live-service stability",
        divisions=(
            "Game Design",
            "Engineering",
            "Art & Animation",
            "Narrative & Audio",
            "QA",
            "LiveOps",
            "Monetization",
            "Community",
        ),
    ),
    Industry(
        slug="advertising-creative-agency",
        name="Advertising & Creative Agency",
        objective="Deliver campaign outcomes across brand and performance work with predictable margin and client trust.",
        risk_focus="strategy-to-execution gaps, media inefficiency, creative misses, and client churn",
        compliance_focus="brand safety, disclosure requirements, data-usage constraints, and contract SLAs",
        outcome_focus="campaign ROI, client retention, utilization, and gross margin",
        divisions=(
            "Strategy",
            "Creative",
            "Copy",
            "Media Planning",
            "Media Buying",
            "Performance Marketing",
            "Production",
            "Client Services",
        ),
    ),
    Industry(
        slug="retail-ecommerce",
        name="Retail & E-commerce",
        objective="Optimize assortment, inventory, and channel execution to maximize profitable growth online and in-store.",
        risk_focus="stockouts/overstock, pricing errors, fulfillment failures, and return-rate inflation",
        compliance_focus="consumer protection, payments/privacy controls, marketplace rules, and tax obligations",
        outcome_focus="gross margin return on inventory, conversion, AOV, and service-level attainment",
        divisions=(
            "Merchandising",
            "Inventory",
            "Pricing & Promotions",
            "Store Operations",
            "E-commerce Operations",
            "CRM & Loyalty",
            "Marketplace Operations",
            "Support",
        ),
    ),
    Industry(
        slug="fashion-apparel",
        name="Fashion & Apparel",
        objective="Plan and execute seasonal assortments from concept to sell-through with brand consistency and margin control.",
        risk_focus="forecast misses, sourcing delays, quality defects, and markdown pressure",
        compliance_focus="supplier compliance, product safety, labeling, and sustainability disclosures",
        outcome_focus="full-price sell-through, margin, delivery adherence, and category growth",
        divisions=(
            "Trend Research",
            "Design",
            "Sourcing",
            "Sampling",
            "Manufacturing",
            "Merchandising",
            "Retail & E-commerce",
            "Brand & PR",
        ),
    ),
    Industry(
        slug="beauty-personal-care",
        name="Beauty & Personal Care",
        objective="Scale compliant product portfolios with strong launch execution across DTC, retail, and trade channels.",
        risk_focus="formula/regulatory delays, quality incidents, and weak launch conversion",
        compliance_focus="ingredient/claims compliance, labeling, stability requirements, and safety reporting",
        outcome_focus="velocity per SKU, repeat rate, gross margin, and safety incident rate",
        divisions=(
            "Product Development",
            "Regulatory",
            "Manufacturing",
            "Brand Marketing",
            "Trade Marketing",
            "DTC",
            "Education",
            "Quality & Safety",
        ),
    ),
    Industry(
        slug="food-beverage-cpg",
        name="Food & Beverage (CPG)",
        objective="Develop and scale profitable CPG portfolios while maintaining food safety and in-stock performance.",
        risk_focus="recall exposure, forecast error, shelf disruption, and promotional inefficiency",
        compliance_focus="food safety plans, labeling/claims controls, retailer standards, and traceability",
        outcome_focus="distribution breadth, velocity, margin, and safety performance",
        divisions=(
            "R&D",
            "Regulatory & Labeling",
            "Procurement",
            "Manufacturing",
            "Distribution",
            "Sales",
            "Trade Marketing",
            "QA & Food Safety",
        ),
    ),
    Industry(
        slug="restaurants-qsr",
        name="Restaurants & QSR",
        objective="Standardize high-throughput operations and guest experience across owned and franchised locations.",
        risk_focus="service inconsistency, food waste, labor imbalance, and guest satisfaction volatility",
        compliance_focus="food handling, labor rules, franchise standards, and local permitting",
        outcome_focus="same-store sales, ticket times, guest satisfaction, and waste reduction",
        divisions=(
            "Menu R&D",
            "Procurement",
            "Kitchen Operations",
            "Front-of-House",
            "Delivery Operations",
            "Local Marketing",
            "Franchising",
            "Training & QA",
        ),
    ),
    Industry(
        slug="travel-hospitality",
        name="Travel & Hospitality",
        objective="Maximize occupancy and revenue while protecting service quality across customer journeys.",
        risk_focus="demand volatility, service failures, overbooking/underutilization, and partner breakdowns",
        compliance_focus="consumer protections, local hospitality regulations, data/privacy, and payment security",
        outcome_focus="RevPAR/ADR optimization, occupancy, guest satisfaction, and repeat bookings",
        divisions=(
            "Revenue Management",
            "Reservations",
            "Property Operations",
            "Guest Experience",
            "Partnerships",
            "Marketing",
            "Events",
            "Compliance",
        ),
    ),
    Industry(
        slug="sports",
        name="Sports",
        objective="Optimize team and business performance across competition, fan growth, and commercial operations.",
        risk_focus="injury/availability risk, roster inefficiency, event-day failures, and sponsor underperformance",
        compliance_focus="league rules, medical standards, event safety, and sponsorship contract obligations",
        outcome_focus="competitive performance, attendance, fan engagement, and commercial yield",
        divisions=(
            "Team Operations",
            "Coaching & Performance",
            "Medical & Recovery",
            "Scouting & Recruiting",
            "Media & Content",
            "Sponsorship",
            "Ticketing",
            "Fan Engagement",
        ),
    ),
    Industry(
        slug="education-edtech",
        name="Education & EdTech",
        objective="Deliver measurable learner outcomes through robust curriculum, platform reliability, and student support.",
        risk_focus="outcome gaps, content quality drift, low completion, and support bottlenecks",
        compliance_focus="accreditation standards, privacy requirements, accessibility rules, and assessment integrity",
        outcome_focus="completion, mastery gains, retention, and satisfaction",
        divisions=(
            "Curriculum",
            "Instructional Design",
            "Assessment",
            "Student Success",
            "Admissions",
            "Platform & Product",
            "Compliance & Accreditation",
            "Outcomes Analytics",
        ),
    ),
    Industry(
        slug="healthcare-providers",
        name="Healthcare Providers",
        objective="Coordinate safe, efficient, patient-centered care operations with resilient reimbursement and compliance.",
        risk_focus="care delays, denials, coding defects, workforce strain, and patient safety incidents",
        compliance_focus="clinical quality standards, privacy/security, billing rules, and accreditation requirements",
        outcome_focus="quality measures, access metrics, denial reduction, and patient experience",
        divisions=(
            "Clinical Operations",
            "Care Coordination",
            "Revenue Cycle",
            "Coding & Billing",
            "Compliance",
            "Patient Experience",
            "Workforce Operations",
            "Quality Improvement",
        ),
    ),
    Industry(
        slug="pharma-biotech",
        name="Pharma & Biotech",
        objective="Advance assets from discovery through commercialization with scientific rigor and regulatory readiness.",
        risk_focus="trial delays, safety signal handling, CMC constraints, and access barriers",
        compliance_focus="GxP controls, trial governance, adverse event reporting, and submission standards",
        outcome_focus="milestone velocity, study quality, approval readiness, and launch uptake",
        divisions=(
            "Discovery",
            "Preclinical",
            "Clinical Trials",
            "Regulatory Affairs",
            "Pharmacovigilance",
            "Manufacturing",
            "Medical Affairs",
            "Market Access",
        ),
    ),
    Industry(
        slug="medical-devices",
        name="Medical Devices",
        objective="Design, validate, and scale device portfolios with strict quality systems and post-market reliability.",
        risk_focus="verification/validation delays, quality escapes, service failures, and submission risk",
        compliance_focus="QMS obligations, validation traceability, submission rigor, and complaint handling",
        outcome_focus="release readiness, defect rates, field reliability, and service compliance",
        divisions=(
            "Product Engineering",
            "Clinical Validation",
            "Quality Systems",
            "Regulatory Submissions",
            "Manufacturing",
            "Field Service",
            "Training",
            "Post-Market Surveillance",
        ),
    ),
    Industry(
        slug="banking-fintech",
        name="Banking & Fintech",
        objective="Grow compliant financial products while controlling fraud, credit, and operational risk.",
        risk_focus="fraud loss, underwriting drift, control gaps, and service failures",
        compliance_focus="AML/KYC controls, prudential requirements, consumer protections, and model governance",
        outcome_focus="risk-adjusted growth, loss rates, customer satisfaction, and control effectiveness",
        divisions=(
            "Product",
            "Risk",
            "Compliance & AML",
            "Underwriting",
            "Fraud",
            "Operations",
            "Customer Experience",
            "Data & Model Governance",
        ),
    ),
    Industry(
        slug="insurance",
        name="Insurance",
        objective="Optimize underwriting, claims, and servicing to improve combined ratio and policyholder outcomes.",
        risk_focus="pricing drift, claims leakage, fraud, and service latency",
        compliance_focus="state/market regulations, fair-pricing obligations, and audit traceability",
        outcome_focus="combined ratio improvement, cycle time reduction, and retention",
        divisions=(
            "Product & Actuarial",
            "Underwriting",
            "Claims",
            "Fraud & SIU",
            "Distribution",
            "Compliance",
            "Customer Service",
            "Portfolio Analytics",
        ),
    ),
    Industry(
        slug="legal-services",
        name="Legal Services",
        objective="Deliver high-quality legal work with predictable matter economics and defensible process controls.",
        risk_focus="missed deadlines, inconsistent drafting quality, discovery errors, and billing disputes",
        compliance_focus="ethics obligations, privilege/confidentiality controls, and jurisdictional requirements",
        outcome_focus="matter outcomes, cycle time, realization rate, and client satisfaction",
        divisions=(
            "Intake",
            "Matter Management",
            "Research",
            "Drafting & Review",
            "Litigation Support",
            "eDiscovery",
            "Billing",
            "Compliance",
        ),
    ),
    Industry(
        slug="real-estate",
        name="Real Estate",
        objective="Drive portfolio growth and asset performance across acquisition, development, leasing, and operations.",
        risk_focus="deal execution slippage, vacancy, capex overruns, and legal/title surprises",
        compliance_focus="zoning/permitting, lease obligations, financing covenants, and local regulations",
        outcome_focus="occupancy, NOI growth, project delivery predictability, and return on invested capital",
        divisions=(
            "Acquisitions",
            "Development",
            "Leasing",
            "Property Management",
            "Transactions",
            "Financing",
            "Legal & Title",
            "Market Intelligence",
        ),
    ),
    Industry(
        slug="construction-aec",
        name="Construction & AEC",
        objective="Plan and deliver projects safely, on schedule, and on budget with strong quality outcomes.",
        risk_focus="scope changes, safety incidents, procurement delays, and schedule/cost overrun",
        compliance_focus="building codes, safety requirements, contract terms, and inspection standards",
        outcome_focus="schedule adherence, cost variance, safety performance, and punchlist closure",
        divisions=(
            "Estimating",
            "Design",
            "BIM",
            "Procurement",
            "Site Operations",
            "Safety",
            "QA/QC",
            "Project Controls",
        ),
    ),
    Industry(
        slug="manufacturing",
        name="Manufacturing",
        objective="Improve throughput, quality, and reliability from planning through production and fulfillment.",
        risk_focus="line downtime, quality escapes, supply disruptions, and planning instability",
        compliance_focus="process controls, safety standards, traceability, and supplier conformance",
        outcome_focus="OEE, scrap reduction, on-time-in-full, and cost per unit",
        divisions=(
            "Product Engineering",
            "Planning & Scheduling",
            "Procurement",
            "Production",
            "Maintenance",
            "Quality",
            "Supply Chain",
            "Continuous Improvement",
        ),
    ),
    Industry(
        slug="logistics-supply-chain",
        name="Logistics & Supply Chain",
        objective="Deliver resilient, cost-efficient end-to-end logistics performance across global networks.",
        risk_focus="forecast misses, network bottlenecks, customs delays, and last-mile service failures",
        compliance_focus="trade compliance, carrier contracts, safety controls, and customer SLAs",
        outcome_focus="OTIF, total landed cost, cycle time, and exception reduction",
        divisions=(
            "Demand Planning",
            "Procurement",
            "Warehousing",
            "Transportation",
            "Customs & Trade",
            "Last-Mile",
            "Network Optimization",
            "Control Tower Analytics",
        ),
    ),
    Industry(
        slug="energy-utilities",
        name="Energy & Utilities",
        objective="Balance reliability, safety, and cost while modernizing generation, grid, and customer operations.",
        risk_focus="outage risk, asset failures, compliance penalties, and demand/supply volatility",
        compliance_focus="grid reliability standards, market rules, safety obligations, and ESG reporting",
        outcome_focus="service reliability, outage duration, operating cost, and compliance performance",
        divisions=(
            "Generation",
            "Grid Operations",
            "Field Service",
            "Asset Reliability",
            "Trading",
            "Customer Operations",
            "Regulatory Affairs",
            "Sustainability & ESG",
        ),
    ),
    Industry(
        slug="agriculture-agtech",
        name="Agriculture & AgTech",
        objective="Increase yield and profitability through better agronomy, operations, and market execution.",
        risk_focus="weather volatility, input inefficiency, harvest loss, and price risk",
        compliance_focus="input handling standards, food traceability, labor/safety rules, and export compliance",
        outcome_focus="yield per acre, cost per acre, harvest efficiency, and realized margin",
        divisions=(
            "Agronomy",
            "Farm Operations",
            "Inputs Procurement",
            "Irrigation",
            "Harvest Logistics",
            "Commodity Sales",
            "Traceability",
            "Yield Analytics",
        ),
    ),
    Industry(
        slug="government-public-sector",
        name="Government & Public Sector",
        objective="Deliver citizen services with transparency, policy alignment, and operational accountability.",
        risk_focus="service delays, procurement friction, budget variance, and audit findings",
        compliance_focus="public procurement rules, records requirements, accessibility standards, and policy mandates",
        outcome_focus="service-level attainment, budget adherence, audit closure, and constituent satisfaction",
        divisions=(
            "Policy",
            "Program Delivery",
            "Procurement",
            "Case Management",
            "Digital Services",
            "Finance",
            "Audit",
            "Public Communications",
        ),
    ),
    Industry(
        slug="nonprofit-ngo",
        name="Nonprofit & NGO",
        objective="Maximize mission impact while maintaining funding resilience and governance discipline.",
        risk_focus="program drift, grant non-compliance, donor churn, and operating instability",
        compliance_focus="grant reporting obligations, donor restrictions, safeguarding standards, and audit controls",
        outcome_focus="program outcomes, funding diversification, retention, and overhead efficiency",
        divisions=(
            "Program Design",
            "Grants",
            "Fundraising",
            "Donor Relations",
            "Volunteer Operations",
            "Monitoring & Evaluation",
            "Advocacy",
            "Finance & Compliance",
        ),
    ),
    Industry(
        slug="telecom",
        name="Telecom",
        objective="Expand network capacity and service quality while reducing churn and operational cost-to-serve.",
        risk_focus="network incidents, rollout delays, churn spikes, and support backlog",
        compliance_focus="spectrum/regulatory obligations, outage reporting, consumer protections, and security standards",
        outcome_focus="network availability, churn reduction, ARPU quality, and service productivity",
        divisions=(
            "Network Planning",
            "Build & Deploy",
            "NOC Operations",
            "BSS/OSS",
            "Customer Support",
            "Product Bundles",
            "Regulatory",
            "Churn & Retention Analytics",
        ),
    ),
    Industry(
        slug="cybersecurity-industry",
        name="Cybersecurity",
        objective="Reduce threat exposure and response time through integrated prevention, detection, and recovery operations.",
        risk_focus="control gaps, alert fatigue, delayed containment, and policy drift",
        compliance_focus="security frameworks, audit requirements, incident reporting, and identity governance",
        outcome_focus="risk reduction, detection/response speed, control coverage, and audit pass rate",
        divisions=(
            "Threat Intelligence",
            "Security Engineering",
            "SOC",
            "Incident Response",
            "GRC",
            "IAM",
            "AppSec",
            "Security Education",
        ),
    ),
)

COLORS: tuple[str, ...] = ("blue", "green", "orange", "purple", "red", "cyan", "indigo", "teal")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def division_profile(division: str) -> str:
    d = division.lower()
    governance_tokens = (
        "regulatory",
        "compliance",
        "legal",
        "audit",
        "quality",
        "safety",
        "aml",
        "grc",
        "title",
        "accreditation",
    )
    analytics_tokens = (
        "analytics",
        "research",
        "intelligence",
        "actuarial",
        "measurement",
        "evaluation",
        "control tower",
        "yield",
        "market intelligence",
    )
    growth_tokens = (
        "marketing",
        "publicity",
        "pr",
        "audience",
        "sales",
        "distribution",
        "fundraising",
        "donor",
        "sponsorship",
        "ticketing",
        "fan engagement",
        "subscription",
        "monetization",
        "merchandising",
        "commodity sales",
    )
    operations_tokens = (
        "operations",
        "production",
        "manufacturing",
        "site",
        "warehouse",
        "transportation",
        "delivery",
        "reservations",
        "guest",
        "service",
        "support",
        "claims",
        "field",
        "soc",
        "incident",
        "care coordination",
        "property",
        "kitchen",
        "front-of-house",
    )

    if any(t in d for t in governance_tokens):
        return "governance"
    if any(t in d for t in analytics_tokens):
        return "analytics"
    if any(t in d for t in growth_tokens):
        return "growth"
    if any(t in d for t in operations_tokens):
        return "operations"
    return "strategy"


def lead_deliverables(profile: str, division: str) -> tuple[str, str, str, str]:
    if profile == "governance":
        return (
            f"{division} policy and control matrix with ownership.",
            "Assurance plan with sampling cadence and exception handling.",
            "Risk register with severity scoring and mitigation actions.",
            "Quarterly compliance review memo with remediation status.",
        )
    if profile == "analytics":
        return (
            f"{division} KPI dictionary and metric governance rules.",
            "Measurement plan with data source lineage and refresh SLAs.",
            "Decision dashboard spec with thresholds and alert logic.",
            "Insight memo translating trend shifts into action items.",
        )
    if profile == "growth":
        return (
            f"{division} growth plan with segment/channel priorities.",
            "Experiment roadmap with hypotheses, budgets, and guardrails.",
            "Performance scorecard with efficiency and quality thresholds.",
            "Quarterly optimization plan tied to revenue and retention goals.",
        )
    if profile == "operations":
        return (
            f"{division} operating model with capacity and SLA targets.",
            "Runbook governance plan with checkpoint and escalation rules.",
            "Throughput/quality scorecard with bottleneck actions.",
            "Reliability improvement plan with root-cause prevention.",
        )
    return (
        f"{division} strategy brief and prioritized roadmap.",
        "Capability map and dependency plan across adjacent divisions.",
        "Milestone plan with acceptance criteria and owners.",
        "Tradeoff memo covering speed, quality, and cost options.",
    )


def operator_deliverables(profile: str, division: str) -> tuple[str, str, str, str]:
    if profile == "governance":
        return (
            f"{division} control execution log with evidence artifacts.",
            "Issue tracker for exceptions, owners, and due dates.",
            "Audit-ready packet with sampling and remediation records.",
            "Weekly control health summary with pass/fail status.",
        )
    if profile == "analytics":
        return (
            f"{division} reporting pack with validated metrics and notes.",
            "Data quality check results with corrective actions.",
            "Alert triage log with decisions and response times.",
            "Insight backlog prioritized by business impact.",
        )
    if profile == "growth":
        return (
            f"{division} campaign execution tracker with spend and outcomes.",
            "A/B test execution log with results and next actions.",
            "Creative/offer QA checklist with launch approvals.",
            "Performance pacing report with optimization recommendations.",
        )
    if profile == "operations":
        return (
            f"{division} shift/run execution report with SLA attainment.",
            "Exception log with root cause and corrective actions.",
            "Handoff checklist proving task completion and quality checks.",
            "Continuous improvement backlog with cycle-time savings estimates.",
        )
    return (
        f"{division} execution tracker with completed deliverables.",
        "Dependency and blocker log with escalation outcomes.",
        "Acceptance evidence pack for completed work items.",
        "Process-improvement recommendations with effort/impact scores.",
    )


def lead_metrics(profile: str) -> tuple[str, str, str, str]:
    if profile == "governance":
        return (
            "Control coverage >= 95% on critical obligations.",
            "Open high-severity findings reduced cycle over cycle.",
            "Remediation SLA attainment >= 90%.",
            "Audit readiness score trends upward each quarter.",
        )
    if profile == "analytics":
        return (
            "Data freshness SLA attainment >= 95%.",
            "Metric defect rate <= 2% per cycle.",
            "Decision-to-action conversion on insights >= 70%.",
            "Forecast error within agreed threshold bands.",
        )
    if profile == "growth":
        return (
            "Efficiency metrics improve each cycle (CAC/CPA/ROAS context).",
            "Conversion and retention targets hit or exceeded.",
            "Experiment velocity with statistically valid reads.",
            "Revenue or qualified pipeline contribution trend upward.",
        )
    if profile == "operations":
        return (
            "SLA adherence >= 95%.",
            "First-pass quality acceptance >= 85%.",
            "Rework rate <= 10%.",
            "Critical issue detection/escalation within agreed windows.",
        )
    return (
        "Priority initiative completion rate >= 85%.",
        "Forecast accuracy within +/- 10%.",
        "Milestone acceptance on first review >= 80%.",
        "Dependency-related delays trend downward.",
    )


def color_for_index(index: int) -> str:
    return COLORS[index % len(COLORS)]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_orchestrator(industry: Industry) -> str:
    division_list = ", ".join(industry.divisions)
    gate_lines = "\n".join(
        [
            "1. Discovery Gate: objective clarity, baseline data, risk framing.",
            "2. Planning Gate: scoped roadmap, owner assignment, dependency map.",
            "3. Execution Gate: division-level delivery against acceptance criteria.",
            "4. Validation Gate: quality/compliance checks with evidence artifacts.",
            "5. Launch/Ops Gate: handover completeness and operating dashboards live.",
        ]
    )

    return f"""---
name: "{industry.name} Orchestrator"
description: "Pipeline controller for {industry.name} coordinating division leads and operators through stage gates, risk controls, and measurable outcomes."
color: gold
---

# {industry.name} Orchestrator Agent Personality

## Your Identity & Memory
- Role: End-to-end operating controller for {industry.name} initiatives.
- Personality: Structured, evidence-first, risk-aware, execution-focused.
- Memory: Maintains decision logs, stage-gate outcomes, and recurring failure patterns.
- Experience: Prevents handoff failures and keeps delivery tied to measurable value.

## Your Core Mission
- Drive this industry objective: {industry.objective}
- Coordinate all divisions ({division_list}) with explicit owner-accountability.
- Enforce stage-gate progression with acceptance evidence at every boundary.
- Default requirement: no phase advance without validated outputs and risk disposition.

## Critical Rules You Must Follow
- Risk focus must remain visible in every status review: {industry.risk_focus}.
- Compliance focus is non-negotiable: {industry.compliance_focus}.
- Any blocked critical path must be escalated within one operating cycle.
- Retry failed work up to 3 times, then escalate with concrete options.

## Technical Deliverables
- Program operating plan with milestones, dependencies, and acceptance criteria.
- Weekly stage-gate dashboard with pass/fail status and blocker ownership.
- Cross-division handoff log containing expected input/output contracts.
- Executive summary with outcome trend tied to {industry.outcome_focus}.

## Workflow Process
{gate_lines}

## Communication Style
- Lead with decisions, risks, and next actions.
- Keep updates concise, auditable, and tied to metrics.
- Escalate with option A/B/C and projected impact.

## Learning & Memory
- Track root causes for misses and update handoff controls.
- Maintain a lessons-learned ledger by gate and division.
- Reuse successful sequencing patterns in future cycles.

## Success Metrics
- Stage-gate first-pass rate >= 80%.
- Milestone on-time rate >= 90%.
- High-severity blocker resolution within agreed SLA.
- Outcome trend aligned to: {industry.outcome_focus}.

## Advanced Capabilities
- Parallel workstream orchestration under dependency constraints.
- Rapid re-baselining when scope, budget, or timeline changes.
- Scenario planning with quantified risk/cost tradeoffs.
"""


def render_lead(industry: Industry, division: str, color: str) -> str:
    profile = division_profile(division)
    d1, d2, d3, d4 = lead_deliverables(profile, division)
    m1, m2, m3, m4 = lead_metrics(profile)

    return f"""---
name: "{industry.name} {division} Lead"
description: "Strategic lead for {industry.name} {division}, responsible for policy, roadmap, standards, and cross-division alignment."
color: {color}
---

# {industry.name} {division} Lead Agent Personality

## Your Identity & Memory
- Role: Strategic owner for the {division} division.
- Personality: Analytical, accountable, systems-oriented.
- Memory: Keeps assumptions, decisions, and tradeoffs explicit and reviewable.
- Experience: Converts business goals into executable division plans.

## Your Core Mission
- Define division strategy aligned to the industry objective.
- Set standards, controls, and operating cadence for {division}.
- Coordinate dependencies with adjacent divisions through clear handoffs.
- Default requirement: every initiative must map to measurable business value.

## Critical Rules You Must Follow
- Reject ambiguous asks without acceptance criteria.
- Surface material risks and dependency constraints early.
- Keep all standards operational, testable, and auditable.
- Ensure plans account for {industry.compliance_focus}.

## Technical Deliverables
- {d1}
- {d2}
- {d3}
- {d4}

## Workflow Process
1. Assess current-state performance and constraint boundaries.
2. Prioritize initiatives by impact, effort, and risk-adjusted value.
3. Publish roadmap, acceptance criteria, and handoff contracts.
4. Monitor execution quality, then recalibrate each planning cycle.

## Communication Style
- Communicate priorities, tradeoffs, and outcomes in plain language.
- Provide decision-ready briefs with quantified implications.
- Keep escalation paths explicit and time-bounded.

## Learning & Memory
- Capture forecast vs actual variance each cycle.
- Track recurring bottlenecks and harden planning controls.
- Retire low-yield activities based on measurable performance.

## Success Metrics
- {m1}
- {m2}
- {m3}
- {m4}

## Advanced Capabilities
- Portfolio re-prioritization under constraints.
- Policy-to-execution translation with quality safeguards.
- Multi-quarter planning linked to real operating signals.
"""


def render_operator(industry: Industry, division: str, color: str) -> str:
    profile = division_profile(division)
    d1, d2, d3, d4 = operator_deliverables(profile, division)
    m1, m2, m3, m4 = lead_metrics("operations" if profile == "strategy" else profile)

    return f"""---
name: "{industry.name} {division} Operator"
description: "Execution specialist for {industry.name} {division}, responsible for day-to-day delivery, quality checks, and reliable handoffs."
color: {color}
---

# {industry.name} {division} Operator Agent Personality

## Your Identity & Memory
- Role: Daily execution owner for {division} operations.
- Personality: Practical, disciplined, detail-oriented.
- Memory: Tracks runbook quality, exceptions, and recurring defect patterns.
- Experience: Delivers consistent outputs under real-world constraints.

## Your Core Mission
- Execute planned work to spec, on schedule, and with proof.
- Maintain controls and checkpoints that protect quality and compliance.
- Escalate blockers with clear options before deadlines are at risk.
- Default requirement: no task closes without validation evidence.

## Critical Rules You Must Follow
- Follow approved standards and escalation policies exactly.
- Record defects, cycle times, and quality outcomes each run.
- Stop and escalate when safety/legal/quality thresholds are breached.
- Never expand scope without lead approval.

## Technical Deliverables
- {d1}
- {d2}
- {d3}
- {d4}

## Workflow Process
1. Intake prioritized tasks with acceptance criteria.
2. Execute using runbooks and control checkpoints.
3. Validate outputs and attach evidence artifacts.
4. Handoff completion status, open risks, and recommendations.
5. Log lessons learned and propose process improvements.

## Communication Style
- Report concise, factual status with clear ownership.
- Escalate with impact statement plus recommended action.
- Keep updates operational, not narrative.

## Learning & Memory
- Identify repeat failure modes and patch runbooks.
- Improve first-pass quality through checklist refinement.
- Track throughput and error trends for continuous improvement.

## Success Metrics
- {m1}
- {m2}
- {m3}
- {m4}

## Advanced Capabilities
- Throughput optimization without quality regression.
- Early-warning detection of failure conditions.
- Stable execution during demand surges or incident windows.
"""


def render_pack_readme(industry: Industry) -> str:
    lines = [
        f"# {industry.name} Agent Pack",
        "",
        "## Scope",
        f"This pack defines a full operating model for {industry.name} with one orchestrator and paired lead/operator agents for each division.",
        "",
        "## Industry Context",
        f"- Objective: {industry.objective}",
        f"- Risk Focus: {industry.risk_focus}",
        f"- Compliance Focus: {industry.compliance_focus}",
        f"- Outcome Focus: {industry.outcome_focus}",
        "",
        "## Division Map",
        "| Division | Lead Agent | Operator Agent |",
        "|---|---|---|",
    ]

    for d in industry.divisions:
        lines.append(f"| {d} | {industry.name} {d} Lead | {industry.name} {d} Operator |")

    lines.extend(
        [
            "",
            "## Stage-Gate Model",
            "1. Discovery: baseline metrics, risk framing, and scope boundaries.",
            "2. Planning: roadmap, owners, dependencies, and acceptance criteria.",
            "3. Execution: lead/operator delivery loops by division.",
            "4. Validation: QA/compliance checks with evidence artifacts.",
            "5. Launch/Ops: handover completeness and operating review cadence.",
            "",
            "## Agent Files",
            f"- Orchestrator: [agents/{industry.slug}-orchestrator.md](agents/{industry.slug}-orchestrator.md)",
        ]
    )

    for d in industry.divisions:
        d_slug = slugify(d)
        lines.append(f"- [agents/{industry.slug}-{d_slug}-lead.md](agents/{industry.slug}-{d_slug}-lead.md)")
        lines.append(f"- [agents/{industry.slug}-{d_slug}-operator.md](agents/{industry.slug}-{d_slug}-operator.md)")

    lines.extend(
        [
            "",
            "## Activation Prompt",
            "```",
            f"Activate {industry.name} Orchestrator.",
            f"Objective: {industry.objective}",
            "Run the stage-gate model end to end with evidence-backed pass/fail decisions.",
            "Require lead/operator handoffs in every division and escalate critical blockers within one cycle.",
            "```",
        ]
    )

    return "\n".join(lines)


def generate(repo_root: Path) -> None:
    out_dir = repo_root / "industries"

    if out_dir.exists():
        # Remove old generated industry packs cleanly and recreate.
        # Preserve directory root for stable path references.
        for child in out_dir.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    readme = """# Industry Agent Packs

This directory contains fully built industry packs that extend The Agency model beyond software-only workflows.

Each industry pack contains:
- 1 orchestrator agent
- 1 lead + 1 operator agent for each division
- an industry README with context, stage-gates, and activation prompt

Generation source:
- script: `scripts/generate-industry-packs.py`
- wrapper: `scripts/generate-industry-packs.sh`
"""
    write_text(out_dir / "README.md", readme)

    matrix_lines = [
        "# Industry Division Matrix",
        "",
        "| Industry | Divisions | Agent Files | Pack |",
        "|---|---:|---:|---|",
    ]

    total_agents = 0

    for industry in INDUSTRIES:
        pack_dir = out_dir / industry.slug
        agents_dir = pack_dir / "agents"
        agents_dir.mkdir(parents=True, exist_ok=True)

        # Pack README
        write_text(pack_dir / "README.md", render_pack_readme(industry))

        # Orchestrator
        write_text(agents_dir / f"{industry.slug}-orchestrator.md", render_orchestrator(industry))

        # Division agents
        for i, division in enumerate(industry.divisions):
            color = color_for_index(i)
            d_slug = slugify(division)
            write_text(
                agents_dir / f"{industry.slug}-{d_slug}-lead.md",
                render_lead(industry, division, color),
            )
            write_text(
                agents_dir / f"{industry.slug}-{d_slug}-operator.md",
                render_operator(industry, division, color),
            )

        count = 1 + (len(industry.divisions) * 2)
        total_agents += count
        matrix_lines.append(
            f"| {industry.name} | {len(industry.divisions)} | {count} | [{industry.slug}]({industry.slug}/README.md) |"
        )

    write_text(out_dir / "MASTER-DIVISION-MATRIX.md", "\n".join(matrix_lines))

    summary = (out_dir / "README.md").read_text(encoding="utf-8").rstrip() + (
        f"\n\nGenerated packs: {len(INDUSTRIES)}\nGenerated agent files: {total_agents}\n"
    )
    write_text(out_dir / "README.md", summary)

    print(f"Generated {len(INDUSTRIES)} industry packs and {total_agents} agent files in {out_dir}")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    generate(repo_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
