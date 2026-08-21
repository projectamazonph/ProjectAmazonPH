# Development Plan — ProjectAmazonPH

**Version:** 1.1 | **Status:** Active | **Last Updated:** 2026-08-21

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ProjectAmazonPH                              │
├─────────────────────────────────────────────────────────────────────┤
│ Marketing Layer │ Community Layer │ Course Layer │ Platform Layer    │
│                 │                 │              │                   │
│ • Facebook      │ • FB Group      │ • PPC Found.  │ • PPC Companion  │
│ • YouTube       │ • Community     │ • Accelerated │ • Student Portal │
│ • LinkedIn      │ • Alumni Net.   │ • Ultimate    │ • LMS Features   │
│ • SEO/Website   │                 │ • Resources   │ • Job Board      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Brand Foundation

**Status:** ✅ COMPLETE

| Task | Details |
|------|---------|
| Brand identity | Colors, fonts, voice, tagline |
| Brand kit document | BRAND-KIT.md — complete guidelines |
| Positioning | "From Zero to ₱80k+/Month" |
| Social profiles | Facebook, YouTube, LinkedIn, Netlify |
| Logo & visual assets | Orange (#FF6B35) + Navy (#1A1A2E) |

---

## Phase 2: Content Engine

**Status:** ✅ COMPLETE

| Task | Details |
|------|---------|
| Content calendar | Month-by-month posting schedule |
| Facebook content engine | Automated daily posting (Page 9AM, Group 6PM) |
| Marketing strategy | Full funnel: Awareness → Interest → Decision → Action |
| Market research | CrewAI amazon_ph_flow (8 outputs) |
| Channel strategy | Facebook primary, YouTube secondary, LinkedIn tertiary |

---

## Phase 3: Marketing & SEO

**Status:** ✅ COMPLETE

| Task | Details |
|------|---------|
| Marketing strategy doc | MARKETING-STRATEGY.md |
| SEO plan | SEO-PLAN.md (keywords, on-page, technical) |
| Landing pages | 3 tier pages on Netlify |
| Tool audit | TOOL-AUDIT.md (existing assets + gaps) |
| Facebook Ads setup | Target audience, creatives, budget |

---

## Phase 4: Community Growth

**Status:** 🟡 ACTIVE

| Task | Details | Progress |
|------|---------|----------|
| Facebook Group growth | Target: 5,000 members | Active |
| Content engagement | Daily posts, polls, discussions | Active |
| Alumni network | Graduate mentorship program | Planned |
| Live events | Q&A sessions, webinars | Planned |
| Testimonial collection | Video + text testimonials | Active |

---

## Phase 5: Course Platform Development

**Status:** 🟢 LIKELY COMPLETE — verify against PRD.md

| Task | Details | Priority | Status |
|------|---------|----------|--------|
| AMPH Academy integration | Live platform — 8 modules, 31 MDX lessons | High | ✅ Live |
| Interactive exercises | Campaign Builder, Bid Elevator, STR Triage | High | ✅ Live |
| Quiz / gamification | 17 badges, XP, streaks, leaderboard | Medium | ✅ Live |
| Progress tracking | 11-tab student dashboard | Medium | ✅ Live |
| Admin dashboard | User, course, badge, settings management | Medium | ✅ Live |
| Live Classes | Admin CRUD, student registration, scheduling | Medium | ✅ Live |
| Certificate generation | Verifiable credentials | High | ✅ Live |
| Community platform | Forums, discussions | Medium | ⏳ Pending |
| Job board | Employer connections for graduates | Low | ⏳ Pending |

> **Note:** This phase was marked PLANNED on 2026-07-02, but PRD v2.1 (2026-08-21) reports the AMPH Academy platform as Live with all core features shipped. Recommend merging verified status back into this doc.

---

## Phase 6: Scale & Expansion

**Status:** 🟡 ACTIVE / PARTIAL

| Task | Priority | Status |
|------|----------|--------|
| Advanced course tiers (Agency track, Team Lead track) | Medium | 🔵 Design |
| amph-v2-greenfield rebuild (next-gen architecture) | High | 🟡 Production hardening |
| English Taglish localization | Low | ⏳ Pending |
| Mobile app for course access | Low | ⏳ Pending |
| Corporate training packages | Medium | ⏳ Pending |
| Affiliate program for alumni | High | ⏳ Pending |
| Franchise/license model for other coaches | Low | ⏳ Pending |

---

## Open Questions

1. **Platform:** ✅ Resolved — custom AMPH Academy (Next.js 16) instead of Teachable/Thinkific
2. **Payment processing:** PayMongo + Resend integrated in amph-v2-greenfield; verify live status
3. **Content production:** YouTube cadence still TBD — see content-calendar/
4. **Community moderation:** Volunteer alumni mods vs paid — still open
5. **Pricing review:** Tiers held at ₱2,999 / ₱5,999 / ₱9,999; revisit at 6-month mark
