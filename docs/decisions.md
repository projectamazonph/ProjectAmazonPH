# Architecture Decision Records — ProjectAmazonPH

**Last updated:** 2026-08-21 (refresh — see `MASTER-PLAN.md` Phase 3 for current decision cadence)

---

## ADR-001: Orange + Navy Brand Colors

**Status:** ✅ ACCEPTED

**Context:** The brand needs colors that convey energy, trust, and premium positioning. Must be distinctive in the Amazon PPC coaching space.

**Decision:** Primary: Orange (#FF6B35) — energy, action, affordability. Secondary: Navy (#1A1A2E) — trust, professionalism, stability.

**Consequences:**
- ✅ Orange stands out on social media feeds
- ✅ Navy adds premium feel
- ⚠️ Orange can be overwhelming — used as accent, not background

---

## ADR-002: Taglish Bilingual Voice

**Status:** ✅ ACCEPTED

**Context:** Target audience is Filipino VAs who code-switch between Tagalog and English naturally. Pure English feels distant; pure Tagalog limits reach.

**Decision:** Use Taglish (Tagalog-English code-switching) as primary brand voice — direct, encouraging, specific. English for technical content; Taglish for community and marketing.

**Consequences:**
- ✅ Authentic connection with target audience
- ✅ Higher engagement on social media
- ⚠️ Some content needs pure English for broader reach
- ⚠️ Consistency requires clear voice guidelines

---

## ADR-003: Facebook-First Distribution Strategy

**Status:** ✅ ACCEPTED

**Context:** Target audience (Filipino VAs) is most active on Facebook. Other platforms (YouTube, LinkedIn) are secondary.

**Decision:** Primary distribution via Facebook (Page + Group), with content repurposed to YouTube and LinkedIn. Facebook posting schedule: Page 9AM daily (educational), Group 6PM daily (community engagement).

**Consequences:**
- ✅ Highest reach for target demographic
- ✅ Community building via Group
- ✅ Content repurposing across platforms reduces workload
- ⚠️ Over-reliance on single platform — algorithm changes risk
- ⚠️ Facebook organic reach declining — ads budget needed for scale

---

## ADR-004: Three-Tier Pricing Model

**Status:** ✅ ACCEPTED

**Context:** Students have varying budgets and commitment levels. One-size-fits-all pricing leaves money on the table and excludes price-sensitive prospects.

**Decision:** Three tiers:
- PPC Foundations (₱2,999) — Self-paced, low barrier to entry
- Accelerated Mastery (₱5,999) — Coaching, mid-range commitment
- Ultimate Transformation (₱9,999) — Premium 1-on-1, high-touch

**Consequences:**
- ✅ Captures multiple price points
- ✅ Upsell path from low to high tiers
- ✅ Clear differentiation
- ⚠️ Tier management complexity (content, support per tier)

---

## ADR-005: Custom PPC Companion as Learning Platform

**Status:** ✅ ACCEPTED

**Context:** Off-the-shelf LMS platforms (Teachable, Thinkific) charge recurring fees and limit customization. Building on Next.js gives full control and integrates with existing PPC tools.

**Decision:** Build custom training platform using Next.js 16 (AMPH Academy v2 — `amph-academy.vercel.app`) instead of using existing LMS platforms.

**Consequences:**
- ✅ Full control over features and pricing
- ✅ Integrated with PPC tools (Campaign Builder, Bid Elevator, STR Triage Arena)
- ✅ No recurring platform fees
- ✅ Live since 2026-Q2 with 8 modules, 31 lessons, 17 badges
- ⚠️ Development time and maintenance cost
- ⚠️ Must build features that exist out-of-the-box in LMS platforms
