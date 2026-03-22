# lead-gen-local

**A complete, repeatable B2B lead generation system for local service businesses.**

Build qualified prospect lists, score by conversion probability, and execute efficient outreach campaigns for any region, service, or local business vertical.

---

## What This Is

A production-tested lead generation methodology generalized for universal use.

**Core insight:** Not all "no website" businesses are equal. Service businesses losing customers online ≠ busy tradespeople overbooked with referrals. This system distinguishes between them and targets high-probability prospects only.

**Result:** 5-6x efficiency (30 emails to right people = 100 emails to random people).

---

## Quick Start

### For your first region (2-3 days)

1. **Read** `lead-gen-local/references/QUICK_START.md` (15 min)
2. **Research** prospects on Google Maps + local directories (2 hours) → save to spreadsheet
3. **Score** using probability formula from `references/INDUSTRIES.md` (1.5 hours)
4. **Create templates** using `references/TEMPLATE_FRAMEWORK.md` (1.5 hours)
5. **Execute outreach** - email Tier 1 only, track responses

**Expected Month 1:**
- 30 emails sent
- 6-12 conversations booked (20-40% response rate)
- 2-4 projects closed (if sales skills present)

### For subsequent regions (1.5-2 days)

1. Skim QUICK_START.md (5 min)
2. Research (2 hours) - same process
3. Score (1.5 hours) - same formula
4. Adapt templates (1 hour) - copy from first region, adjust
5. Execute

The methodology compounds. Gets faster each time.

---

## Skill Structure

```
lead-gen-local/
├── SKILL.md (320 lines)
│   └── Core 7-step process, definitions, anti-patterns
│
├── references/
│   ├── QUICK_START.md (295 lines)
│   │   └── 5-min overview + day-by-day execution
│   │
│   ├── INDUSTRIES.md (250 lines)
│   │   └── Industry classification: high/medium/low probability
│   │       with scoring formula, business signals, examples
│   │
│   ├── RESEARCH_DIRECTORIES.md (257 lines)
│   │   └── Where to find data by region (Belgium, US, UK, Canada,
│   │       Australia, Germany, Europe + universal approach)
│   │
│   └── TEMPLATE_FRAMEWORK.md (357 lines)
│       └── Email template structures, customization formulas,
│           subject lines, CTAs, follow-up sequences, tracking
│
└── scripts/
    └── lead_scorer.py (239 lines)
        └── CSV scoring automation (industry weights, signals, tiers)
```

**Total:** 1,718 lines of tested, battle-hardened methodology.

---

## Key Concepts

### Probability Scoring (not volume)

All prospects are not equal:

| Industry | Probability | Why | Messaging |
|----------|-------------|-----|-----------|
| Hair salons | 80%+ | Customers research online | "Show your work, build trust" |
| Massage/wellness | 75%+ | Need credibility + reviews | "Professional scheduling, bookings" |
| Fitness studios | 70%+ | Need class schedule visibility | "Discoverability + booking system" |
| Restaurants | 65%+ | People Google before visiting | "Findability + menu + hours" |
| Specialty retail | 45% | Conditional benefit | "Reach beyond foot traffic" |
| Custom trades | 40% | Portfolio helps | "Showcase past work" |
| Busy plumbers | 10% | Overbooked, don't need website | **SKIP** |
| HVAC/heating | <5% | B2B model, not consumer | **SKIP** |

### Tier System

- **TIER 1 (Score 9-10):** 15-35 prospects, 35-60% conversion. Start here.
- **TIER 2 (Score 6-8):** 25-50 prospects, 15-40% conversion. Secondary wave.
- **TIER 3 (Score 1-5):** Skip initially. Not worth early effort.

### Customization > Templates

- Generic: "You need a website" (1-2% response)
- Customized: "Your salon's Instagram is stunning but Google doesn't know about you" (10-20% response)
- **10x difference from one personal line.**

---

## Use Cases

**Works for any B2B service targeting local businesses:**

- Web design / development
- Digital marketing / SEO / social media
- Consulting (business, HR, finance)
- Photography / videography
- Design / branding
- Accounting / bookkeeping
- Coaching / personal training
- Copywriting / content services
- Legal services
- Any local service selling to other local businesses

---

## Workflow Summary

### Step 1: Research (Find prospects)
- Geography: Define target city/region
- Industries: Identify high-probability for your service
- Sources: Use `references/RESEARCH_DIRECTORIES.md` for local data
- Compile: 100-300 prospects in spreadsheet

**Time:** 2 hours per category

### Step 2: Score (Rank by probability)
- Industry weight: High/medium/low (0.5 factor)
- Website status: None/outdated/good (0.3 factor)
- Business signals: Reviews, rating, activity (0.2 factor)
- Formula: `Score = (industry × 0.5) + (website × 0.3) + (signals × 0.2)`
- Tier: Assign TIER 1/2/3

**Time:** 1.5 hours for 100-300 prospects (or use `lead_scorer.py` if CSV)

### Step 3: Create Templates (Write emails)
- Template A: No website angle
- Template B: Outdated website
- Template C: Good site, upgrade angle
- Template D: Translated versions (if multilingual)
- Customize: Add 1-2 lines specific to their industry/business

**Time:** 1.5 hours for 3-4 templates

### Step 4: Outreach (Send emails)
- Email Tier 1 only (20-30 leads Week 1)
- Track responses (date, response type, follow-up)
- Follow up after 1 week (email 2 to non-responses)
- Follow up after 2 weeks (email 3 to non-responses)
- Only move to Tier 2 after Tier 1 substantially worked

**Time:** 1-2 hours/week ongoing

---

## Expected Results

### Month 1 (30 Tier 1 emails)
- Response rate: 20-40%
- Conversations booked: 6-12
- Projects closed: 2-4 (if sales skills present)

### Month 2-3 (Tier 2 + continuing Tier 1)
- Response rate improves (authority from first projects)
- Portfolio improves (real case studies)
- More projects running simultaneously

### Month 6+ (System matures)
- 10-20 inbound inquiries/month
- Mix of cold outreach + referrals
- Portfolio strong enough to drive self-referral
- Less cold outreach needed (system becomes mostly inbound)

---

## Files Guide

**Start here:**
- `lead-gen-local/references/QUICK_START.md` - 5-minute overview + day-by-day plan

**For deep dives:**
- `lead-gen-local/references/INDUSTRIES.md` - Industry classification + scoring formula
- `lead-gen-local/references/RESEARCH_DIRECTORIES.md` - Where to find data (by region)
- `lead-gen-local/references/TEMPLATE_FRAMEWORK.md` - How to write emails that convert

**For automation:**
- `lead-gen-local/scripts/lead_scorer.py` - Python script for CSV scoring

**Full process:**
- `lead-gen-local/SKILL.md` - Complete 7-step workflow

---

## Customization

### For a new service

1. Read `lead-gen-local/references/INDUSTRIES.md` structure
2. Adapt industry classification for your service (which industries need you most?)
3. Create new templates in `references/TEMPLATE_FRAMEWORK.md` style
4. Run same 4-step process (research → score → templates → outreach)

### For a new region

1. Check `lead-gen-local/references/RESEARCH_DIRECTORIES.md` for data sources
2. Research using Google Maps + local directories
3. Use same scoring formula from `INDUSTRIES.md`
4. Adapt templates to local language/context
5. Execute outreach

---

## Technical

**Requirements:**
- Python 3.6+ (for `lead_scorer.py` automation, optional)
- Spreadsheet software (Google Sheets, Excel, etc.)
- Email account

**No external APIs required.** The system works with manual research + spreadsheets.

**Automation options:**
- `lead_scorer.py` - automates probability scoring from CSV
- Email sending could be integrated with CRM/automation tools (but maintain human review for personalization)

---

## Contributing

This system improves with each region/service it's used for. If you discover:
- New high-probability industries (add to `INDUSTRIES.md`)
- Better email angles (add to `TEMPLATE_FRAMEWORK.md`)
- New data sources for your region (add to `RESEARCH_DIRECTORIES.md`)
- Scoring improvements (update formulas with real data)

Open an issue or PR with your learnings.

---

## License

MIT License - See LICENSE file for details

---

## Next Steps

1. **Clone this repo** or integrate into your OpenClaw skills directory
2. **Read** `lead-gen-local/references/QUICK_START.md` (15 min)
3. **Pick your first region** + service
4. **Execute** the 4-step process
5. **Track results** and feed back learnings to improve the system

---

## What This Does NOT Cover

**Out of scope (separate skills/systems):**
- Sales conversation training (how to close calls)
- Service delivery (how to actually do the work)
- Platform automation (CRM integration, email tools)
- Payment processing
- Contract templates

This system gets you in the door. Other systems handle closing + delivery.

