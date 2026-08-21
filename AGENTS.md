# AGENTS.md — ProjectAmazonPH

> **Amazon PPC Coaching Brand** — Ryan's business training Filipino VAs to become Amazon PPC specialists. The operational hub for content, marketing, brand, and student acquisition.

## Identity

| Field | Value |
|-------|-------|
| **Owner** | Ryan Roland Dabao |
| **Experience** | 14-year VA industry veteran · 8-year Amazon PPC specialist · ₱50M+ managed ad spend |
| **Business** | Amazon PPC coaching (₱2,999 / ₱5,999 / ₱9,999 tiers) |
| **Social** | FB @projectamazonph · YT @RyanRolandDabao · LI @ryandabao |
| **FB Group** | fb.com/groups/3158233264458437 ("Project Amazon.PH") |
| **FB Page** | "Upskill Pilipinas — Freelancing Community" (@projectamazonph) |
| **Mission** | Filipino VAs: ₱15k → ₱80k+/month through PPC specialization |

## Directory Structure

```
ProjectAmazonPH/
├── amazon_ph_flow/        ← CrewAI workflow reference (8 research outputs, see amazon_ph_flow/README.md)
├── brand-kit/             ← Brand guidelines, logos, colors, voice (BRAND-KIT.md)
├── content-calendar/      ← Social media content scheduling (CONTENT-CALENDAR.md)
├── crewai/                ← Multi-agent AI workflow templates
├── docs/                  ← architecture.md + decisions.md (ADRs)
├── marketing/             ← Marketing collateral, ad copy, funnels (MARKETING-STRATEGY.md)
├── seo/                   ← SEO research and strategy (SEO-PLAN.md)
├── tool-audit/            ← Tool evaluations (TOOL-AUDIT.md)
├── facebook-content-engine.md  ← FB posting strategy (Page 9AM, Group 6PM daily)
├── README.md              ← Public profile (Lane 1 + Lane 2 portfolio)
├── PRD.md                 ← Product requirements (AMPH Academy = primary)
├── DEV-PLAN.md            ← 6-phase development plan
├── MASTER-PLAN.md         ← Overall campaign strategy
├── WORKLOG.md             ← Session log
├── AGENTS.md              ← This file
├── TODO.md / KANBAN.md    ← Task tracking (see GitHub Issues)
```

## Content Engine

| Channel | Schedule | Content |
|---------|----------|---------|
| **FB Page** | 9:00 AM daily | Educational posts, tips, case studies |
| **FB Group** | 6:00 PM daily | Community engagement, discussions, Q&A |
| **YouTube** | @RyanRolandDabao | Long-form training videos, testimonials |
| **LinkedIn** | ph.linkedin.com/in/ryandabao | Professional networking, thought leadership |

## Product Tiers

| Tier | Price | Target |
|------|-------|--------|
| PPC Foundations | ₱2,999 | Career shifters, complete beginners |
| Accelerated Mastery | ₱5,999 | VAs with some PPC experience |
| Ultimate Transformation | ₱9,999 | Advanced specialists, agency owners |

## Guardrails

### DO NOT
- ❌ Mix brand voice — ProjectAmazonPH is educational/aspirational, not corporate
- ❌ Post to Facebook without confirming content aligns with content calendar
- ❌ Share client data or PPC account credentials in these files
- ❌ Edit `facebook-content-engine.md` without understanding the 9AM/6PM posting cadence

### DO
- ✅ Write in first-person educational voice (Ryan's perspective)
- ✅ Reference real PPC results where possible (₱50M+ managed ad spend)
- ✅ Keep brand documents updated when positioning changes
- ✅ Check `MASTER-PLAN.md` before strategic decisions

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Public profile (Lane 1 PPC + Lane 2 AI Systems) |
| `PRD.md` | Product requirements — AMPH Academy is the live platform |
| `DEV-PLAN.md` | 6-phase development plan (phases 1-4 ✅, 5-6 active) |
| `MASTER-PLAN.md` | Overall campaign strategy (current phase: 3) |
| `facebook-content-engine.md` | Social media posting strategy (Page + Group) |
| `brand-kit/BRAND-KIT.md` | Visual identity, logos, brand guidelines |
| `content-calendar/CONTENT-CALENDAR.md` | Scheduled posts and campaigns |
| `seo/SEO-PLAN.md` | SEO keyword research and strategy |
| `marketing/MARKETING-STRATEGY.md` | Funnel, channels, KPIs |
| `docs/architecture.md` | Brand, content, funnel architecture |
| `docs/decisions.md` | Architecture Decision Records (ADRs) |
| `tool-audit/TOOL-AUDIT.md` | Tool inventory and gaps |
| `amazon_ph_flow/AGENTS.md` | CrewAI technical reference (auto-generated) |
| `amazon_ph_flow/README.md` | CrewAI flow usage (note: was template with `{{crew_name}}` placeholder — fixed) |

### Related Repos (live, in this org)

- **[amph-v2](https://github.com/projectamazonph/amph-v2)** — AMPH Academy v2 (live student platform)
- **[amph-v2-greenfield](https://github.com/projectamazonph/amph-v2-greenfield)** — Greenfield rebuild (production hardening)
- **[Interview-lab](https://github.com/projectamazonph/Interview-lab)** — AI-powered interview practice
- **[ppc-tools-for-va](https://github.com/projectamazonph/ppc-tools-for-va)** — Free browser-based tools
- **[Amazon-PPC-Student-Wiki](https://github.com/projectamazonph/Amazon-PPC-Student-Wiki)** — Community knowledge base

---

*Last refreshed: 2026-08-21 | Part of Ryan's Hermes Agent workspace*
