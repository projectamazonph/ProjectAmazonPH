# ProjectAmazonPH — Tool Audit

**Version:** 1.1  
**Date:** 2026-08-21 (refresh)  
**Originally authored:** June 25, 2026  
**Purpose:** Inventory existing tools, identify gaps, map what's needed for marketing/SEO/content.

---

## 1. Existing Assets (What You Have)

### AMPH Academy (formerly PPC Companion) — Next.js App
**Repo:** https://github.com/projectamazonph/amph-v2
**Status:** ✅ Live (PRD v2.1, 2026-08-21) — 8 modules, 31 MDX lessons, 17 badges, certificate generation
**Architecture:** Next.js 16, Prisma 7, SQLite, JWT auth (jose, HttpOnly cookies), Tailwind, shadcn/ui, Framer Motion, Zustand
**Deployment:** Vercel — amph-academy.vercel.app

**Marketing Use:** Core delivery platform. Replaces PDF-based training with interactive experience. Premium positioning vs competitors.

### Interview Lab (Next.js App)
**Repo:** https://github.com/projectamazonph/Interview-lab
**Status:** ✅ Deployed on Vercel
**Features:**
- AI-powered mock interviews (Puter.js)
- Resume coaching
- Cover letter generation
- Practice tests
- 26 downloadable assets

**Marketing Use:** Lead magnet (free tier) + upsell to paid coaching. Email capture vehicle.

### Downloadable Assets (26 Files)
**Path:** `Interview-lab/public/downloads/` (in the Interview-lab repo)

| Asset | Type | Marketing Use |
|-------|------|---------------|
| 30-day-upskilling-roadmap.pdf | PDF | Lead magnet |
| 7-day-prep-plan.pdf | PDF | Lead magnet |
| acos-roas-cpc-calculator.xlsx | Excel | Free tool |
| campaign-launch-checklist.pdf | PDF | Lead magnet |
| campaign-naming-worksheet.xlsx | Excel | Free tool |
| client-update-emails.docx | Word | Template |
| interview-cheat-sheet.pdf | PDF | Lead magnet |
| keyword-harvesting-decision-tree.pdf | PDF | Content upgrade |
| listing-readiness-checklist.pdf | PDF | Lead magnet |
| mock-interview-scorecard.pdf | PDF | Free tool |
| negative-keyword-checklist.pdf | PDF | Content upgrade |
| ppc-acronym-glossary.pdf | PDF | Lead magnet |
| ppc-case-study-workbook.xlsx | Excel | Case study |
| ppc-va-cover-letter.docx | Word | Template |
| ppc-va-resume-template.docx | Word | Template |
| practical-test-answers.pdf | PDF | Premium content |
| remote-work-checklist.pdf | PDF | Lead magnet |
| search-term-practice.xlsx | Excel | Exercise |
| sop-checklist.pdf | PDF | Lead magnet |
| star-worksheet.pdf | PDF | Exercise |
| tools-familiarity-checklist.pdf | PDF | Lead magnet |
| upwork-proposal-template.docx | Word | Template |
| weekly-ppc-report-template.pdf | PDF | Template |

**Marketing Use:** Lead magnets (email capture), content upgrades (blog post bonuses), free tools (SEO + trust).

### AMPH Academy Curriculum (Adcraft Academy — now AMPH Academy v2)
**Repo:** https://github.com/projectamazonph/amph-v2  
**Status:** ✅ Live with 8 modules, 31 MDX lessons  
**Modules:**
- 0-onboarding (3 lessons)
- 1-foundations (5 lessons)
- 2-keyword-research (4 lessons)
- 3-listing-optimization (3 lessons)
- 4-campaign-architecture (4 lessons)
- 5-portfolio-strategy (3 lessons)
- 6-bidding-lab (3 lessons)
- 7-search-term-triage (3 lessons)
- 8-competitive-intelligence (3 lessons)

**Marketing Use:** Blog content source, YouTube script source, course material.

### Two Blog Posts (Drafted)
**Status:** Verify if published — these were first drafts from June 2026
**Marketing Use:** Publish as first blog posts. Journey post = trust building. Technical post = authority.

### Second Brain (Knowledge Base)
**Content:** Amazon PPC fundamentals, ADCP protocol, MCP server landscape, workflow patterns  
**Marketing Use:** Content source, research foundation, industry expertise proof.

---

## 2. Tools Needed (What's Missing)

### Marketing Infrastructure
| Tool | Purpose | Cost | Priority | Status |
|------|---------|------|----------|--------|
| Custom domain | Professional URL | ₱500/yr | 🔴 Must | ❌ Not registered |
| Email marketing | Nurture leads | Free tier | 🔴 Must | ❌ Not set up |
| Landing page builder | Better conversion | Netlify/Vercel | 🟡 Nice | ✅ Exists |
| Payment gateway | Accept payments | % per txn | 🔴 Must | ❌ Not set up |
| CRM | Track leads | Free tier | 🟡 Nice | ❌ Not set up |

### Content Production
| Tool | Purpose | Cost | Priority | Status |
|------|---------|------|----------|--------|
| Canva Pro | Graphics, thumbnails | ₱500/mo | 🟡 Nice | ❌ Not subscribed |
| CapCut | Video editing | Free | 🔴 Must | ✅ Available |
| OBS Studio | Screen recording | Free | 🔴 Must | ✅ Available |
| Descript | Video/audio editing | Free tier | 🟡 Nice | ❌ Not set up |
| Loom | Quick video share | Free tier | 🟡 Nice | ❌ Not set up |

### SEO
| Tool | Purpose | Cost | Priority | Status |
|------|---------|------|----------|--------|
| Google Search Console | Performance tracking | Free | 🔴 Must | ❌ Not set up |
| Google Analytics 4 | Traffic analytics | Free | 🔴 Must | ❌ Not set up |
| Ubersuggest | Keyword research | Free tier | 🟡 Nice | ❌ Not set up |
| Yoast/RankMath | On-page SEO | Free | 🟡 Nice | ❌ Not applicable (not WordPress) |
| Schema markup | Rich results | Free | 🟡 Nice | ❌ Not implemented |

### Social Media
| Tool | Purpose | Cost | Priority | Status |
|------|---------|------|----------|--------|
| Facebook Business Page | Brand presence | Free | 🔴 Must | ✅ Exists (Upskill Pilipinas @projectamazonph) |
| Facebook Group | Community | Free | 🔴 Must | ✅ Exists (Project Amazon.PH, needs activation) |
| YouTube Channel | Long-form content | Free | 🔴 Must | ✅ Exists (@RyanRolandDabao, needs content) |
| TikTok Account | Short-form content | Free | 🟡 Nice | ❌ Not created |
| LinkedIn Profile | Professional brand | Free | 🟡 Nice | ✅ Exists (Ryan Roland Dabao, needs optimization) |
| Buffer/Later | Social scheduling | Free tier | 🟡 Nice | ❌ Not set up |

### Analytics & Tracking
| Tool | Purpose | Cost | Priority | Status |
|------|---------|------|----------|--------|
| Google Analytics 4 | Website traffic | Free | 🔴 Must | ❌ Not set up |
| Hotjar | User behavior | Free tier | 🟡 Nice | ❌ Not set up |
| ConvertKit | Email + landing pages | Free tier | 🟡 Nice | ❌ Not set up |
| Stripe/PayPal | Payments | % per txn | 🔴 Must | ❌ Not set up |

---

## 3. Tool Gaps Analysis

### Critical Path (Must Complete Before Launch)
1. **Custom domain** — Register projectamazonph.com
2. **Payment gateway** — Stripe or PayPal for enrollment
3. **Email marketing** — Mailchimp or Mailerlite free tier
4. **Google Analytics + Search Console** — Track everything
5. **Facebook Business Page** — Brand presence
6. **Fix testimonials** — Get real, specific stories

### Quick Wins (Do This Week)
1. Register domain (15 minutes)
2. Set up Mailchimp free tier (30 minutes)
3. Create Facebook page (15 minutes)
4. Install Google Analytics on Netlify site (15 minutes)
5. Publish first blog post (4 hours)

### Growth Phase (Month 2-3)
1. YouTube channel + first 4 videos
2. Facebook group launch
3. TikTok/Reels content
4. SEO optimization on all pages
5. Lead magnet creation (already have assets)

---

## 4. Existing Tool → Marketing Map

```
AMPH Academy ────────→ Course delivery platform (premium positioning)
                       └─→ Interactive learning vs PDF competitors

Interview Lab ───────→ Lead magnet (free tier)
                       └─→ Email capture → nurture → upsell

26 Downloadables ────→ Lead magnets (email capture)
                       └─→ Content upgrades (blog bonuses)
                       └─→ Free tools (SEO + trust)

AMPH Academy Content ─→ Blog posts (source material)
                       └─→ YouTube scripts
                       └─→ Course material

Second Brain ────────→ Research foundation
                       └─→ Content source
                       └─→ Industry expertise proof

Blog Posts (drafted) ─→ Publish immediately
                       └─→ SEO foundation
                       └─→ Trust building
```

---

## 5. Recommended Tech Stack (Final)

### Free Tier Stack (Month 1-3)
| Layer | Tool | Cost |
|-------|------|------|
| Hosting | Netlify (current) | Free |
| Domain | Namecheap/Cloudflare | ₱500/yr |
| Email | Mailchimp free | Free |
| Analytics | Google Analytics 4 | Free |
| SEO | Google Search Console | Free |
| Social | Facebook, YouTube, TikTok | Free |
| Video | CapCut + OBS | Free |
| Graphics | Canva free tier | Free |
| Payments | PayPal.me | Free (txn fees only) |
| **Total** | | **₱500/year + txn fees** |

### Paid Stack (Month 4-6)
| Layer | Tool | Cost |
|-------|------|------|
| Email | Mailerlite paid | ₱500/mo |
| Graphics | Canva Pro | ₱500/mo |
| Social scheduling | Buffer | ₱500/mo |
| Ads | Facebook + Google | ₱1,000/day |
| Webinar | Zoom/Luma | Free-₱1k/mo |
| **Total** | | **₱1,500/mo + ads** |

---

*Audit complete. You have more than you think. The gap is distribution, not product.*
