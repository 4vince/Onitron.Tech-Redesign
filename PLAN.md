# Omnitron.Tech Redesign - Plan (Prototype First)

> **Update (2026-10-14) — Theme revision.** The design direction moved from a **dark** canvas
> to a **warm off-white** editorial theme. The dark palette in §3 is superseded by the values
> in `app/src/app/globals.css`. Summary of the change:
> - **Canvas:** warm off-white `#f6f4f0`, white surfaces `#ffffff`, hairline borders `#e7e4dd`.
> - **Type:** off-black `#17181a` (primary), `#5b5e66` (secondary), `#8f9298` (tertiary).
> - **Accent:** single blue `#2b59e0` (`#1f47c6` hover), plus muted pastel tags.
> - **Fonts:** Geist (sans) + Geist Mono (terminal accents) — replaced Inter.
> - **Added:** brand logo + favicon (`src/app/icon.svg`), mobile nav, scroll reveals, custom 404,
>   per-page metadata, shared service data (`src/data/services.ts`), skip-to-content link.

**Status:** Detailed planning complete (wireframes + component spec). Ready to scaffold Next.js.  
**Approach:** Prototype scope first (homepage + 2 business areas + contact + careers), blend Databricks layout with minimal terminal accents, SME-focused outcomes.

## 1) Final Confirmed Decisions

- **Tech stack:** Next.js (App Router) + Tailwind CSS + TypeScript
- **Design direction:** Blend Databricks layout + minimal terminal accents (avoid CLI-heavy look)
- **Primary color:** Databricks-like blue (#1F77FF) (shifted from red #f24139)
- **Fonts:** Inter (body/headings, variable) + Geist Mono (terminal accents only) - 2 families
- **Hero:** Balanced outcome + technical credibility; CTA text: "Start the conversation"; SME-focused tone overall
- **Navigation:** Simplified - Home, AI Solutions, Intelligence & Advisory, Contact (no mega menus)
- **AI Solutions:** Simple `/ai-solutions` landing with key sub-items as cards + CTAs
- **Intelligence & Advisory:** Simple `/advisory` landing with key sub-items as cards + CTAs (more accessible for SMEs)
- **Contact:** Dedicated `/contact` page (clean, primary CTA). Remove "Ask Michelle" globally.
- **Careers:** `/careers` with hero + "We're not hiring right now, but always interested in talent" + CTA to contact
- **Proof:** "Trusted by" strip with geometric logo placeholders (squares/blocks). Minimal other proof for now
- **Performance:** All + LCP optimization (fonts < 3, WebP/AVIF, lazy load, defer non-critical JS, minimize motion)
- **i18n:** Skip for prototype (Phase 2)
- **Testing:** Informal SUS testing with 5 users (target ≥ 75)
- **Terminal accents:** Minimal (status badges only, very subtle)

## 2) Routes

| Route | Purpose | Notes |
|---|---|---|
| `/` | Homepage | Hero, trusted-by, business area previews, CTAs to contact |
| `/ai-solutions` | AI Solutions landing | Cards for key sub-items (Strategy & Consulting, Intelligent Automation, Agentic Solutions, Customer Experience, Data & Insights). Simple overview + CTAs. |
| `/advisory` | Intelligence & Advisory landing | Cards for key sub-items (Cyber Threat Intelligence, Attack Surface Cartography, Carrier Fraud Disruption, Telemetry Interception, Digital Artifact Forensics, PQC Architecture, HNDL Risk Modeling). SME-accessible language + CTAs. |
| `/contact` | Contact form | Name, email, subject, message. Dedicated page. |
| `/careers` | Careers | Minimal as specified. |

## 3) Design Tokens

Define in Tailwind config/CSS vars:

```css
/* Core */
--bg: #0B1026;           /* deep slate */
--bg-surface: #141B2D;  /* cards */
--bg-surface-2: #1A2438;/* elevated */
--border: #24304D;
--text-primary: #F5F7FA;
--text-secondary: #A3B3CC;
--text-tertiary: #7C8AA8;

/* Accent */
--primary: #1F77FF;     /* Databricks-like blue */
--primary-hover: #1C6EE5;

/* Status (minimal terminal) */
--status: #22C55E;      /* SYS.ONLINE style green */
```

Typography: `Inter, system-ui, sans-serif` for UI/headings; `Geist Mono, monospace` for terminal badges only.

## 4) Wireframe: Homepage (`/`)

1. **Header/Nav** - Logo (Omnitron), links: Home, AI Solutions, Intelligence & Advisory, Contact. Clean, no mega menus.
2. **Hero** - H1: balanced outcome + technical credibility (SME-focused). Subtext explaining value in plain language. CTA "Start the conversation" → `/contact`. 
3. **Trusted by** - Geometric logo placeholders (squares/blocks) in a subtle row. 
4. **AI Solutions Preview** - Section heading, brief intro, cards (5 key items: Strategy & Consulting, Intelligent Automation, Agentic Solutions, Customer Experience, Data & Insights). Link "Learn more" to `/ai-solutions`. CTA to contact.
5. **Intelligence & Advisory Preview** - Similar: heading, intro (SME-accessible), cards (7 items). Link to `/advisory`. CTA to contact.
6. **Final CTA** - "Ready to scale without adding headcount?" or similar SME-focused. CTA to `/contact`.
7. **Footer** - Links (AI Solutions, IA, Contact, Careers), email, social icons with proper aria labels + correct URLs. Remove any "Ask Michelle" references.

## 5) Wireframe: AI Solutions (`/ai-solutions`)

1. **Header/Nav** (same)
2. **Hero** - "AI Solutions that run your business autonomously" (SME-focused)
3. **Intro** - Plain language explanation
4. **Cards Grid** (5 cards):
- Strategy & Consulting
- Intelligent Automation  
- Agentic Solutions
- Customer Experience
- Data & Insights
5. **CTA Block** - "Talk to us about your automation goals" → `/contact`
6. **Footer**

## 6) Wireframe: Intelligence & Advisory (`/advisory`)

1. **Header/Nav**
2. **Hero** - Focus on practical security/advisory outcomes for businesses (without heavy jargon)
3. **Intro** - SME-accessible
4. **Cards Grid** (7 cards):
- Cyber Threat Intelligence
- Attack Surface Cartography
- Carrier Fraud Disruption
- Telemetry Interception Node
- Digital Artifact Forensics
- PQC Architecture
- HNDL Risk Modeling
5. **CTA Block** → `/contact`
6. **Footer**

## 7) Wireframe: Contact (`/contact`)

1. **Header/Nav**
2. **Hero** - "Start the conversation"
3. **Form** - Fields: Name, Email, Subject, Message (required as appropriate). Clean layout, primary submit button. 
4. **Info** (optional but clean): HQ (Singapore) + email
5. **Footer**

## 8) Wireframe: Careers (`/careers`)

1. **Header/Nav**
2. **Hero** - "Careers"
3. **Body** - "We're not hiring right now, but always interested in talent." 
4. **CTA** - "Get in touch" → `/contact`
5. **Footer**

## 9) Components (to create)

### UI
- `Button` - variants (primary, secondary, ghost). Primary uses `--primary` blue.
- `Card` - base card for business area items.
- `Section` - container with consistent padding/spacing.
- `StatusBadge` - minimal terminal badge (e.g., "SYS.ONLINE") using Geist Mono. Use sparingly.
- `Input/Textarea` - form elements with consistent styling.

### Layout
- `Header/Nav` - simplified nav, no mega menus, no Michelle.
- `Footer` - links, socials with a11y labels, correct URLs. Remove Michelle.

### Home
- `Hero` - balanced SME-focused hero + "Start the conversation" CTA.
- `TrustedBy` - geometric logo placeholders strip.
- `BusinessAreaPreview` - previews for both areas with cards + links.

### Pages/Feature
- `ContactForm` - form logic (prototype: just structure, no backend required? Or basic client-side validation). For prototype, structure + validation is fine.
- `BusinessAreaCards` - reusable card grid for sub-items.

## 10) Implementation Plan (Next Steps)

We'll do both in order as requested:
1. **Scaffold** - Create Next.js app with TypeScript, Tailwind v4 or v3? Check package.json style from examples - Marketing-Analytics-Template uses Tailwind (v3 style). Portfolio_Site uses Vite. For Next.js App Router, we can use Tailwind v4 or v3; but keep consistent. Let us set up modern Next.js with Tailwind.
2. **Config** - `tailwind.config.ts`, `tsconfig.json`, globals.css with design tokens.
3. **Layout** - Root layout, Header, Footer.
4. **Pages** - Home, AI Solutions, Advisory, Contact, Careers.
5. **Components** - Build UI components as specified.
6. **Styling** - Apply blend (Databricks layout + minimal terminal). SME-focused.
7. **Cleanup** - Remove Michelle references globally. Fix social link a11y. Performance pass (fonts, images, etc.)
8. **Test** - Quick visual check, prepare for informal SUS test.

Let us start scaffolding the Next.js app now.