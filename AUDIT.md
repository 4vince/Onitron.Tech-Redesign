# Omnitron.Tech Current Site Audit (from live fetch)

**Date:** 2026-10-13  
**Source:** https://www.omnitron.tech/, /services, /advisory, /contact

## Proposal Issues vs Current Site

From proposal:
- Mobile Lighthouse Performance 76 (homepage), hero ~4.1s to appear
- Accessibility: social media links hard to use for assistive tech; wrong profiles
- Design inconsistencies (layout/readability) on desktop
- No proof assets (case studies/logos/testimonials)
- "Michelle" live website agent consumes compute/tokens - needs replacing with contact form
- 11 font files currently loaded (keep small for i18n/multi-language)

## Current Site Observations

### Homepage (https://omnitron.tech)
- **Tech feel**: Terminal/command-line aesthetic ("SYS.ONLINE", "NODES: 250 ACTIVE", "MODE: AGENTIC", "LOC: SG_APAC"). Very technical/ops-oriented.
- **Hero**: "WE BUILD SYSTEMS THAT RUN YOUR BUSINESS. AUTONOMOUSLY." + "Talk to Live Consultant" CTA
- **Sections**: "What We Build" (6 modules), stats (0 hours saved etc - placeholder-ish), "From Labor-Intensive to AI-NATIVE" journey (4 stages), "Operational Diagnosis" (6 issues), "Get a straight answer now" with "Talk to Live Consultant"
- **Footer**: Terms/Privacy, email, social icons (X/LinkedIn) - accessibility unclear; need to check if proper labels/URLs correct
- **Navigation**: Mega-style dropdowns for AI Solutions (5 items) and Intelligence & Advisory (7 items - heavy on security/PQC topics)
- **"Ask Michelle"** - this is the live agent mentioned in proposal (Railway). Proposal says retire it, replace with contact form page.

### Services (/services)
- Focuses on "AI Solutions" bucket: Strategy & Consulting, Intelligent Automation, Agentic Solutions, Customer Experience, Data & Insights. Clean section layout.

### Advisory (/advisory)
- Heavy security-focused content (CTI, Attack Surface Cartography, Fraud Disruption, Telemetry Interception, Digital Forensics, PQC Architecture, HNDL Risk). Different tone from "AI agency for SMEs" homepage. This is the "Intelligence & Advisory" business area mentioned in proposal.

### Contact (/contact)
- Has contact form (name, email, subject, message) + HQ info. So contact form exists; proposal says "build just a contact form page" and "replace live website agent with one contact form page". The live agent "Ask Michelle" is separate.

## Key Takeaways for Redesign

1. **Two business areas clearly exist**: "AI Solutions" (services) and "Intelligence & Advisory" (advisory). The proposal's prototype needs to cover these two business-area sections. 
2. **Strong technical identity** already - command-line aesthetic. Proposal wants Databricks-inspired but also "not traditional SaaS". Need to balance - keep some technical edge but make more approachable for SME owners/managers (per audience).
3. **"Michelle" agent** is present ("Ask Michelle" button) - needs to be retired as per proposal (compute/tokens). Contact form exists at /contact; but proposal says "one contact form page" - maybe consolidate? Or just ensure it's clean and primary.
4. **Navigation is complex** (mega menus). For prototype (homepage + 2 sections + contact), maybe simplify nav.
5. **Social links**: X/LinkedIn icons in footer - likely accessibility issues (no aria labels? wrong URLs?) as noted.
6. **Performance**: Heavy visual/animation feel? Terminal aesthetic with lots of text/sections. Hero timing issue (4.1s) on mobile.
7. **Proof assets missing** - currently shows "0 hours saved" etc as placeholders; also no client logos/case studies. Proposal says add proof slots.

## Next Steps (Planning)
Based on user choice: audit current site + redesign, prototype scope first. Need to decide on design direction - how much of terminal aesthetic to keep vs Databricks-inspired polish? Also need to address performance budget. 

Let me ask key questions to move planning forward.
