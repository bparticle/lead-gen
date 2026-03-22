# Quick Start Guide

---

## 5-MINUTE OVERVIEW

**What this skill does:** Builds repeatable B2B lead lists for local service businesses.

**When to use it:** You're selling to local businesses (web design, marketing, services, etc.) and want a repeatable system to find + qualify + reach them.

**Expected output:** 
- Consolidated prospect list (100-500 leads per region)
- Organized by conversion probability (Tier 1/2/3)
- Email templates ready to customize
- Tracking system for responses

**Time investment:** 2-3 days initial work, then 1-2 hours/week to execute outreach

---

## 3-STEP PROCESS

### Step 1: Research (1 day)
**Input:** City/region + business type you're targeting

**Tools:** Google Maps, Yellow Pages equivalent, industry directories

**Output:** Spreadsheet with 100-500 prospects (name, address, phone, website status, ratings)

**See:** `references/RESEARCH_DIRECTORIES.md` for where to find data by region

### Step 2: Score (2-3 hours)
**Input:** Your prospect spreadsheet

**Scoring logic:** Not all "no website" = same probability
- Hair salons = 80%+ conversion (customers research online)
- Busy plumbers = 10% conversion (overbooked, don't need websites)

**Output:** Same spreadsheet, now with score (1-10) + tier assignment

**See:** `references/INDUSTRIES.md` for probability breakdown + scoring formula

**Automation:** Use `scripts/lead_scorer.py` if you have CSV data

### Step 3: Outreach (ongoing, 1-2 hours/week)
**Input:** Your Tier 1 leads + templates

**Output:** Customized emails + response tracking

**See:** `references/TEMPLATE_FRAMEWORK.md` for how to write high-conversion emails

---

## CORE CONCEPT: PROBABILITY SCORING

Not all "no website" businesses are equal.

**Hair Salon with no website:**
- Customers research on Instagram/Google before booking
- Being invisible online = losing revenue
- Website would directly help their business
- **Conversion probability: 80%+**

**Plumber with no website:**
- Customers find them via referrals or emergency searches
- Already booked via word-of-mouth
- Website wouldn't meaningfully change their business
- **Conversion probability: 10%**

**This system identifies which is which.**

Using probability scoring:
- **30 emails to high-probability leads = 6-12 conversations, 2-4 projects**
- **100 emails to all leads = 15-20 conversations, 2-4 projects**

**Same result, 3x more efficient.**

---

## YOUR FIRST REGION (STEP BY STEP)

### Day 1: Research

**Morning (2 hours):**
1. Open Google Maps
2. Search "[Your service] [City name]" (e.g., "website design Koksijde")
3. Compile 3-4 high-probability industries first
4. For each business: note name, address, phone, website (Y/N), rating, recent reviews

**Example industries (adjust based on your service):**
- Hair salons
- Massage/wellness
- Fitness studios
- Restaurants/cafes
- Retail (upscale/boutique only)

**Output:** Spreadsheet with ~100-200 prospects

**Tips:**
- Google Maps is your primary source (fastest, most complete)
- Don't visit websites (too slow) — just note Y/N
- Focus on Tier 1 industries first (high probability)

### Day 2: Score

**Morning (1.5 hours):**
1. Add columns: website_status, reviews_count, rating, recent_reviews (Y/N), social_media (Y/N)
2. For each prospect, look up on Google Maps + quick Instagram check
3. Use scoring formula from `references/INDUSTRIES.md`
4. Calculate score (1-10) + assign tier

**Formula (quick version):**
```
Score = (Industry × 0.5) + (Website × 0.3) + (Signals × 0.2)

High industry (1.0) + No website (1.0) + Strong signals (1.0) = 10 (TIER 1)
High industry (1.0) + No website (1.0) + Weak signals (0.0) = 8 (TIER 1)
Medium industry (0.7) + No website (1.0) + Strong signals (1.0) = 8.5 (TIER 2)
```

**Or:** Use `lead_scorer.py` script (5 min to set up)

**Output:** Same spreadsheet, now with score + tier

**Expectation:**
- TIER 1: 15-35 leads (highest priority)
- TIER 2: 25-50 leads (secondary)
- TIER 3: 50+ leads (skip initially)

### Day 3: Templates + Setup

**Morning (1.5 hours):**
1. Create email templates using `references/TEMPLATE_FRAMEWORK.md`
2. Create tracking spreadsheet (date sent, response, status)
3. Ready to send

**Afternoon/Week 1:**
1. Start emailing Tier 1 only (20-30 leads)
2. Track responses
3. Expect 15-40% response rate on Tier 1

---

## WHAT YOU'LL PRODUCE

### Deliverable 1: CONSOLIDATED_PROSPECTS.md
Master list, all prospects, organized by tier:
- TIER 1 (9-10): High probability, 15-35 leads
- TIER 2 (6-8): Medium probability, 25-50 leads
- TIER 3 (1-5): Low probability, skip these

### Deliverable 2: EMAIL_TEMPLATES.md
3-4 ready-to-customize templates:
- Template A: No website
- Template B: Outdated website
- Template C: Good website, upgrade angle
- Template D: French version (if multilingual region)

### Deliverable 3: PRICING_REFERENCE.md
Clear pricing for your service:
- Tier 1 ($X): What's included, timeline
- Tier 2 ($X): What's included, timeline
- Tier 3 ($X): What's included, timeline
- Optional: ongoing support/retainer

### Deliverable 4: TRACKING.md
Spreadsheet to track responses:
- Date sent | Prospect | Email template | Response (Y/N) | Follow-up | Status

### Deliverable 5: INDUSTRY_ANALYSIS.md (optional)
Why Tier 1 converts better:
- Industry breakdown
- Customer research behavior
- Probability by type
- Why you skip Tier 3

---

## EXECUTION (WEEKLY)

### Week 1
- Email 10-15 Tier 1 leads
- Track responses
- Expected: 2-6 conversations

### Week 2
- Email remaining 10-15 Tier 1 leads
- Follow up on Week 1 non-responses (1 week after initial)
- Expected: 2-6 more conversations

### Week 3+
- Follow up on Week 2 non-responses
- Only move to TIER 2 if Tier 1 is substantially worked
- Continue until all Tier 1 contacted

**Expected Month 1 results:**
- 30 emails sent
- 6-12 conversations booked
- 2-4 projects closed (if sales skills are good)

---

## COMMON QUESTIONS

**Q: How long does this take?**
A: Initial research + scoring = 2-3 days. Then 1-2 hours/week to send emails + track responses.

**Q: How many leads will I get?**
A: 100-500 depending on region size. Focus on Tier 1 (15-35 leads) first.

**Q: What's a good response rate?**
A: Tier 1 should get 15-40% response rate. Tier 2 should get 10-25%.

**Q: Can I automate this?**
A: Research is manual (Google Maps lookup). Scoring can be automated with `lead_scorer.py`. Email sending should be manual (maintains personalization).

**Q: What if I'm in a different country?**
A: Same process. Different directories. See `references/RESEARCH_DIRECTORIES.md` for your region.

**Q: Should I email everyone?**
A: No. Start with Tier 1 only. Only move to Tier 2 after Tier 1 is worked.

**Q: What if my service doesn't fit these industries?**
A: Use `references/INDUSTRIES.md` as a template. Adapt probability scoring to YOUR industries. The methodology is universal.

---

## ADVANCED USAGE (MONTH 2+)

Once you've worked Tier 1 in one region:

### Option 1: Same Region, Tier 2
Move to Tier 2 (medium probability) in your first region.

### Option 2: New Region
Repeat the process in a new city/region.

### Option 3: Industry Expansion
Research new industries in your current region (e.g., add fitness if you only did salons).

---

## FILES TO READ

**First time?** Read in this order:
1. This file (QUICK_START.md) ← you're here
2. `references/INDUSTRIES.md` (understand probability)
3. `references/RESEARCH_DIRECTORIES.md` (find your local data sources)
4. `references/TEMPLATE_FRAMEWORK.md` (write emails that convert)

**Repeating for new region?**
1. `references/RESEARCH_DIRECTORIES.md` (where to find data in your region)
2. `references/INDUSTRIES.md` (same scoring system)
3. `references/TEMPLATE_FRAMEWORK.md` (same email approach)

**Want to automate?**
1. `scripts/lead_scorer.py` (if you have CSV data)

---

## SUCCESS METRICS

Track these:

- **Emails sent (per week):** Target 15-20 Tier 1 in Week 1-2
- **Response rate:** Expect 15-40% for Tier 1
- **Conversations booked:** Expect 20-50% of responses
- **Conversion rate:** Expect 25-50% of conversations → projects

Example Month 1:
- 30 emails sent
- 6 responses (20%)
- 3 conversations (50% of responses)
- 1 project (33% of conversations)

If you're below these, adjust:
- Lower response rate? Improve email personalization (see TEMPLATE_FRAMEWORK.md)
- Lower conversation rate? Improve CTA clarity
- Lower project rate? Improve your sales conversation or pricing clarity

---

## FINAL RULE

Don't email based on "no website" alone.

Email based on:
1. **Industry type** (do customers research online?)
2. **Website status** (none/outdated/good)
3. **Business signals** (recent reviews, active social, growing)

This system distinguishes between "losing customers online" (email them) and "overbooked with referrals" (skip them).

That's the edge.

