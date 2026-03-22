---
name: lead-gen-local
description: Build repeatable B2B lead lists for local service businesses using smart targeting and probability scoring. Use when: (1) Building a prospect list for a specific geographic area, (2) Targeting local service businesses (salons, trades, wellness, fitness, retail), (3) Creating smart qualification criteria to avoid wasting time on low-probability leads, (4) Setting up a repeatable process for lead generation that can be deployed across multiple regions. Outputs: consolidated prospect list organized by conversion probability, email templates, pricing reference, outreach tracking system, and industry-specific targeting strategy.
---

# Lead Generation for Local Service Businesses

Build targeted, probability-scored lead lists for B2B outreach to local service businesses. This skill provides a repeatable methodology to identify high-probability prospects, qualify them intelligently, and create an efficient outreach system.

---

## CORE PRINCIPLE

Not all "no website" businesses are equal. A salon with no website is losing customers. A busy plumber with no website is overbooked. The system distinguishes between these using **probability scoring** based on industry, market dynamics, and customer research behavior.

**Expected ROI:** 5-6x more efficient than untargeted outreach (fewer leads, higher conversion).

---

## PROCESS OVERVIEW

1. **Define the target geography** (city/region)
2. **Identify high-probability industries** (see INDUSTRIES.md)
3. **Research & compile prospects** using directory sources
4. **Score by conversion probability** (not just "no website")
5. **Consolidate & organize** into tiers
6. **Create templates** (email, pricing, tracking)
7. **Set up outreach system** with response tracking

**Timeline:** 2-3 days for a region (5,000-20,000 people)

---

## DEFINITIONS

**High Probability Industry:** Customers research online before buying/booking. Being invisible online directly costs the business money. (Hair salons, massage, fitness, restaurants)

**Medium Probability Industry:** Some customer research happens online, or the business offers specialty work. Website helps but isn't critical. (Specialty retail, custom trades)

**Low Probability Industry:** Customers find them by referral/reputation. Website won't materially change their business model. (Busy plumbers, HVAC, commodity retail)

**Prospect Score:** 1-10 rating based on: (1) industry type, (2) website status (none/outdated/good), (3) signs of growth/ambition

---

## STEP-BY-STEP WORKFLOW

### STEP 1: Define Geography & Business Type

**Input:** User provides target city/region and service offering

Examples:
- "Web design services in Koksijde, Belgium"
- "SEO consulting in Portland, Oregon"
- "Social media management in Austin, Texas"

**Output:** Clear definition of who you're selling to and where

---

### STEP 2: Identify High-Probability Industries

**Reference:** See `references/INDUSTRIES.md` for industry classification

**Quick assessment:**
- What industries have customers who research online first?
- What industries have high visual/trust component?
- What industries are growing (more young/ambitious businesses)?

**Example for web design:**
- 🟢 HIGH: Hair salons, massage, fitness, restaurants (customers research online)
- 🟡 MEDIUM: Retail, custom trades, specialized electricians (conditional benefit)
- 🔴 LOW: Busy plumbers, HVAC, commodity retail (don't need websites)

---

### STEP 3: Research & Compile Prospects

**Directories to use:**
- Google Maps (location search + type + ratings)
- Industry-specific directories (salon lists, plumbing guides, etc.)
- Yellow Pages equivalent (varies by country)
- Chamber of commerce listings
- LinkedIn (for B2B services)
- Instagram/Facebook (for image-conscious businesses)

**Data to collect per prospect:**
- Business name
- Address
- Category/industry
- Phone (if public)
- Email (if public)
- Website (yes/no/outdated)
- Social presence (Instagram, Facebook, Google Maps reviews)
- Rating/reviews (if available)
- Visual assessment (professional signage, foot traffic indicators)

**Compilation approach:** Spreadsheet with one row per prospect, sortable by category

**Expected volume:** 100-500 prospects for small-to-medium region

---

### STEP 4: Score by Conversion Probability

**DO NOT score on "no website" alone.**

**Scoring criteria (1-10):**

- **10:** High-probability industry + no website + active business signals (Google Maps reviews, Instagram, high ratings)
- **9:** High-probability industry + outdated website + active reviews
- **8:** High-probability industry + outdated website
- **7:** Medium-probability industry + no website + active business
- **6:** Medium-probability industry + outdated website
- **5:** Low-probability industry + no website (unlikely to convert)
- **4:** No clear business signals
- **1-3:** Commodity/low-intent indicators

**Business signals (shows active customer base):**
- Google Maps with recent reviews
- Instagram/Facebook with recent posts
- High ratings (4.5+)
- Clear hours/contact info
- Professional appearance

**Scoring logic:**
```
Score = (Industry_Probability × 0.5) + (Website_Status × 0.3) + (Business_Signals × 0.2)

High industry (0.5) + No website (0.3) + Strong signals (0.2) = 1.0 = Score 10
High industry (0.5) + No website (0.3) + Weak signals (0.1) = 0.9 = Score 9
Medium industry (0.35) + No website (0.3) + Strong signals (0.2) = 0.85 = Score 8.5
Low industry (0.2) + No website (0.3) + Strong signals (0.2) = 0.7 = Score 7
```

---

### STEP 5: Organize Into Tiers

**Tier 1 (Score 9-10):**
- Highest conversion probability (35-60%)
- Email first (primary outreach wave)
- Expected: 15-35 leads per region

**Tier 2 (Score 6-8):**
- Medium conversion probability (15-40%)
- Email after Tier 1 if you want secondary wave
- Expected: 25-50 leads per region

**Tier 3 (Score 1-5):**
- Low conversion probability (<20%)
- Skip initially; only email if time permits
- Expected: 100+ leads (not worth initial effort)

**Consolidate:** Single spreadsheet with all prospects, sorted by score descending.

---

### STEP 6: Create Templates (See references/)

**Email templates:**
- Template A: No website angle ("You're invisible online")
- Template B: Outdated website angle ("Your site looks old")
- Template C: Good website angle ("Let's upgrade what you have")
- Template D: Translated versions (if multilingual market)

**Customize per template:**
- Industry-specific language
- Value prop specific to their business type
- Social proof relevant to them

**Example for salons vs. plumbers:**
- Salon: "Show your work, build trust, book clients"
- Plumber: "Take bookings online, scale without answering calls"

**Pricing reference:**
- 3 tiers (Starter, Professional, Custom)
- Clear feature breakdown per tier
- Timeline per tier
- No hidden fees

**Tracking sheet:**
- Prospect name | Contact | Date sent | Template used | Response | Follow-up | Status

---

### STEP 7: Set Up Outreach System

**Sequence:**
1. Email Tier 1 first (20+ leads in first week)
2. Track responses (date, contact method, type of response)
3. Follow-up after 1 week on non-responses
4. Only move to Tier 2 after Tier 1 is substantially worked

**Metrics to track:**
- Emails sent (per day/week)
- Response rate (% of emails that get reply)
- Conversation booking rate (% of responses that turn into calls)
- Close rate (% of calls that turn into projects)

**Expected performance (first month):**
- 30 emails sent (Tier 1 only)
- 6-12 responses (20-40% response rate)
- 3-6 conversations booked (25-50% of responses)
- 1-2 projects closed (33-50% of conversations, if sales skills are good)

---

## PROBABILITY SCORING REFERENCE

**See `references/INDUSTRIES.md` for full industry breakdown.**

**Quick lookup:**

| Industry | Probability | Reasoning |
|----------|-------------|-----------|
| Hair salons | 80%+ | Clients research online, Instagram-driven |
| Massage/wellness | 70%+ | Need trust + reviews before booking |
| Fitness studios | 60%+ | Class schedules, trainer profiles matter |
| Restaurants/cafes | 60%+ | Google before visiting |
| Specialty retail | 40% | Conditional; depends on type |
| Custom carpenters | 40% | Portfolio helps for custom work |
| Specialized trades | 30% | Niche need, not broad market |
| General plumbers | 10% | Overbooked, don't need website |
| HVAC/heating | <5% | B2B relationships, not consumer |

---

## MESSAGING ANGLES BY TIER

**Tier 1 (High probability):**
> "You're doing great work but people don't know about you online. Let's show your work and book more clients."

**Tier 2 (Medium probability):**
> "Your specialty is unique. Let's make sure the right customers find you."

**Tier 3 (Low probability):**
> "Most customers find you locally. Let's make sure they find you fast." (Only use if Tier 1/2 working well)

---

## COMMON MISTAKES TO AVOID

❌ **Emailing based on "no website" alone**
- A busy plumber with no website doesn't want one
- A salon with no website is losing customers
- Different situations = different response rates

✅ **Instead:** Score by probability using industry + signals

---

❌ **Assuming all trades are equal**
- General plumbing/HVAC = low probability (overbooked)
- Custom/specialized trades = medium probability (portfolio matters)
- Young/new trades = higher probability (building reputation)

✅ **Instead:** Segment by specialization and business stage

---

❌ **Sending generic emails**
- "You need a website" → low response
- "Let's show your salon work online" → higher response

✅ **Instead:** Customize to their industry + situation

---

❌ **Wasting time on Tier 3**
- 100 emails to busy plumbers = 5-10 conversations, 1 project
- 30 emails to salons = 6-12 conversations, 2-4 projects
- Same outcome, 3x the effort

✅ **Instead:** Focus Tier 1 → move to Tier 2 only after success

---

## OUTPUT DELIVERABLES

When you run this process, you'll produce:

1. **CONSOLIDATED_PROSPECTS.md** — Master list, 100-500 leads, organized by tier
2. **EMAIL_TEMPLATES.md** — 3-4 customizable templates per industry
3. **PRICING_REFERENCE.md** — Clear pricing + timeline per tier
4. **PROSPECT_TRACKING.md** — Spreadsheet format for response tracking
5. **INDUSTRY_ANALYSIS.md** — Why Tier 1 is Tier 1 (competitive analysis)
6. **OUTREACH_PLAYBOOK.md** — Week-by-week execution guide

**All outputs are:**
- Repeatable (same process for any region)
- Modular (use piece independently)
- Data-driven (based on probability, not guessing)
- Focused (prioritize high-probability leads)

---

## FOR YOUR NEXT REGION

To repeat this process for a new city/area:

1. **Same geography definition** (define area, population, service type)
2. **Same industry classification** (use INDUSTRIES.md as reference)
3. **Same research approach** (Google Maps + directories)
4. **Same scoring system** (probability-based, not arbitrary)
5. **Same templates** (adapt existing ones to new market)
6. **Same tracking** (same spreadsheet format)

The entire process is data-driven and portable. Adapt the specific directories (different countries have different Yellow Pages), but the methodology is universal.

---

## SEE ALSO

- `references/INDUSTRIES.md` — Full industry breakdown, probability ratings, messaging angles
- `references/RESEARCH_DIRECTORIES.md` — Directory sources by country/region
- `references/TEMPLATE_FRAMEWORK.md` — How to write email templates that convert
- `references/SCORING_METHODOLOGY.md` — Detailed probability scoring logic
- `scripts/lead_scorer.py` — Python script to automate scoring if you have data in CSV

