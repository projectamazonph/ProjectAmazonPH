# 🪖 Interview Lab — UI Production Fix Plan

> **Note (2026-08-21):** This file is a UI production fix plan for the `Interview-lab` app. It belongs in the [Interview-lab repo](https://github.com/projectamazonph/Interview-lab) as `docs/ui-fix-plan.md`, not in the org profile repo. Keeping it here as a redirect pointer for the Aug 2026 docs refresh.
>
> **Action item:** Move this file to `projectamazonph/Interview-lab/docs/ui-fix-plan.md` in a follow-up PR.

---

# 🪖 Interview Lab — UI Production Fix Plan

**Issue:** Overlapping/overflowing text inside text boxes and cards.
**Root Cause:** Two design systems fighting each other:
1. **Glass design system** (custom: GlassCard, GlassButton, GlassInput) — uses `rounded-[2rem]`, `backdrop-blur-xl`, `bg-glass/80`, glass borders
2. **shadcn/ui components** (Card, CardHeader, CardContent, Textarea, Button, Badge) — uses different border-radius, padding, and the CSS `overflow` behaviors conflict

The shadcn `Card` has `rounded-[1.5rem]` with `px-0` on the outer div and `px-8` on header/content. When nested inside GlassCard or used alongside glass components, the inner padding collapses on mobile. The `Card` also lacks `overflow-hidden` so text can bleed out on small viewports.

Additionally, the `Textarea` and inner form elements have no `break-words` or `overflow-wrap` — long text (interview answers, URLs, email addresses) overflows the container.

---

## FIX PLAN

### Priority 1: Fix Card Component (overflow + text wrapping)
- Add `overflow-hidden` to Card root
- Add `break-words` to CardDescription and CardTitle
- Fix padding: ensure `px-6` minimum on mobile

### Priority 2: Fix Textarea Component
- Add `break-words` and `overflow-wrap: anywhere`
- Add `overflow-auto` for scroll on long content
- Ensure max-width respects container

### Priority 3: Fix Inner Page Components
The pages using shadcn `Card` inside the glass system:
- MockInterview.tsx — interview setup card, question card, results card
- ResumeLab.tsx — resume upload/results
- CoverLetterStudio.tsx — letter generation
- QuestionBank.tsx — question cards
- PracticeTests.tsx — test interface
- LearningPaths.tsx — guide cards
- DownloadCenter.tsx — download cards
- AdminPanel.tsx — tables and cards

### Priority 4: Fix LandingPage Mobile
- Nav links overflow on small screens
- Hero text size needs `clamp()` or smaller mobile breakpoints
- Pricing cards need `overflow-hidden`

### Priority 5: Global Text Wrapping
- Add global `overflow-wrap: break-word` for all text content areas
- Ensure no `whitespace-nowrap` on text containers (only on buttons/labels)

---

## EXECUTION ORDER

1. **Global CSS fix** — Add wrap rules to globals.css
2. **Card component** — Fix overflow + wrapping
3. **Textarea component** — Fix overflow + wrapping
4. **Badge component** — Ensure badges wrap properly in cards
5. **LandingPage** — Fix mobile overflow
6. **MockInterview** — Fix interview card overflow
7. **ResumeLab** — Fix text-heavy result cards
8. **CoverLetterStudio** — Fix generated text overflow
9. **QuestionBank** — Fix question card text overflow
10. **PracticeTests** — Fix test answer overflow
11. **Build + Deploy** — Verify all fixes on Vercel

---

## DESIGN PRINCIPLES APPLIED (Stitch Taste + Claude Design)

- **No overlapping elements** — every element occupies its own clean spatial zone
- **Text must never overflow containers** — `break-words` on all text content
- **Cards must contain their content** — `overflow-hidden` on card root
- **Mobile-first** — all fixes tested at 375px minimum
- **Preserve glass aesthetic** — fixes don't change the visual language, just contain it
