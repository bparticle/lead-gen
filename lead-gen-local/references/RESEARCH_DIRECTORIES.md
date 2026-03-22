# Research Directories & Data Sources by Region

---

## BELGIUM & EUROPE (Example)

### General Business Directories
- **Golden Pages** (goldenpages.be) — Searchable by category, location, phone
  - Best for: Salons, trades, services
  - Data: Business name, address, phone, sometimes website
  - Usage: Search by location + category (example: Barber)

- **Google Maps** (maps.google.com)
  - Best for: Everything (primary data source)
  - Data: Location, hours, phone, website, reviews, photos, ratings
  - Usage: Search by business type + location → scrape name, address, reviews, website status
  - Pro tip: Filter by rating 4.0+ to find active businesses

- **Pages Jaunes** (pagesjaunesbelges.be) — French-language
  - Best for: French-speaking regions
  - Same format as Golden Pages

### Industry-Specific Examples
- **Verwarminggids.be** — Heating/HVAC installers
- **Massage-info.be** — Massage therapists & wellness
- **Salon Databases** — Some regions have hairdresser-specific directories

### Search Approach (Universal)
1. Start with Google Maps (most complete, fastest)
2. Cross-reference with local Yellow Pages equivalent (verify phone, get exact address)
3. Check industry-specific directories for specialization signals
4. Verify active business with recent reviews (last 30 days)

### Expected Volume (Small City, ~5,000-10,000 people)
- Hair salons: 8-15
- Massage/wellness: 3-5
- Fitness: 2-3
- Restaurants/cafes: 15-25
- Plumbers: 20-40
- Carpenters: 40-80
- Retail (mixed): 100+

**Total: 200-300 businesses** across all categories

---

## UNITED STATES

### General Business Directories
- **Google Maps** (maps.google.com)
  - Best for: Everything
  - Usage: Search "[Business Type] [City State]" → extract name, address, phone, website, reviews
  - Data quality: Excellent (phone, hours, reviews, photos)

- **Yelp** (yelp.com)
  - Best for: Restaurants, services, reviews
  - Data: Reviews, phone, hours, website, photos
  - Usage: Search by category + location

- **Yellow Pages** (yellowpages.com)
  - Best for: Trades, services
  - Data: Business name, address, phone
  - Usage: Search by category + ZIP code

- **Chamber of Commerce**
  - Best for: Local business listings
  - Usage: [City] Chamber of Commerce + search local directory
  - Data quality: Verified, but less complete than Google

### Industry-Specific
- **Salon Directory** (example: most states have salon boards)
- **State Licensing Boards** (electricians, plumbers, contractors)
- **LinkedIn** (B2B trades, coaches, consultants)

### Search Approach for US
1. Start with Google Maps (fastest, most complete)
2. Cross-reference with Yelp for reviews/details
3. Use Yellow Pages for trades verification
4. Check Chamber of Commerce for legitimacy

### Expected Volume (US City of 10,000 people)
- Hair salons: 10-20
- Massage/wellness: 5-10
- Fitness: 5-8
- Restaurants/cafes: 20-40
- Plumbers: 30-60
- Carpenters: 50-100
- Retail: 150+

**Total: 300-500 businesses**

---

## UNITED KINGDOM

### General Business Directories
- **Google Maps** (maps.google.com)
  - Same as US/worldwide
  
- **Yelp** (yelp.co.uk)
  - UK version, same approach

- **Pages Yellow** (yell.com)
  - UK equivalent of US Yellow Pages
  - Data: Business name, address, phone

- **Local Chamber of Commerce**
  - Verification + local listings

### Industry-Specific
- **Hairdressing Council** — Registered salons
- **REPS UK** — Fitness professionals
- **Register of Plumbers** (varies by region/apprenticeship body)

### Search Approach for UK
1. Google Maps (primary)
2. Yell.com (verification)
3. Industry bodies for specialized trades

---

## CANADA

### General Business Directories
- **Google Maps** (maps.google.ca)
- **Yelp** (yelp.ca)
- **Yellow Pages Canada** (yellowpages.ca)
- **Better Business Bureau** (bbb.org, Canadian affiliate)

### Industry-Specific
- **Provincial trade boards** (varies by province)
- **Salon/beauty boards** (provincial)

---

## AUSTRALIA & NEW ZEALAND

### General Business Directories
- **Google Maps** (maps.google.com.au / .nz)
- **Yelp** (yelp.com.au / .co.nz)
- **Yellow Pages Australia** (yellowpages.com.au)
- **Chamber of Commerce** (varies by region)

### Industry-Specific
- **Fair Work Ombudsman** (verify business legitimacy)
- **State-based trade boards**

---

## GERMANY (DE) & EUROPE (DACH)

### General Directories
- **Google Maps** (maps.google.de/at/ch)
- **Yelp** (yelp.de, yelp.at, yelp.ch)
- **Gelbe Seiten** (Germany) — Deutsche Telekom business directory
- **Herold.at** (Austria) — Austrian business directory

### Industry-Specific
- **Handwerkskammer** (German trades board)
- **Chamber of Commerce** (regional)

---

## UNIVERSAL APPROACH (Works Anywhere)

If you're in a region not listed above:

1. **Start with Google Maps** (works everywhere with internet)
   - Search "[Business Type] [Location]"
   - Extract: name, address, phone, website, reviews, photos
   - This alone is 80% of what you need

2. **Find local equivalent of Yellow Pages**
   - Search "[Country] business directory" or "[Country] yellow pages"
   - Most countries have one

3. **Check Google Search + local language**
   - Search in local language: "[Type of business] [City name]"
   - Results will show local directory listings

4. **Industry-specific boards**
   - For trades (plumbers, electricians): Search "[Country] [trade] licensing board"
   - For salons: Search "[Country] salon directory"
   - For fitness: Search "[Country] fitness professional board"

---

## DATA COLLECTION TEMPLATE

**For each prospect, collect:**

```
Business Name | Address | City | Postal Code | Country | Phone | Email | Website (Y/N) | Website URL | Website Status (None/Old/Current) | Google Rating | Review Count | Recent Reviews? (Y/N) | Instagram? | Facebook? | First Contact | Notes
```

**Example row:**
```
Salon Example | Main Street 42 | City Name | 12345 | Country | +[phone] | - | N | - | None | 4.8 | 24 | Y | Y | Y | - | Active, high-quality photos
```

---

## SPEED OPTIMIZATION TIPS

### Fast Data Collection (1-2 hours per category)
1. Open Google Maps in one window
2. Open spreadsheet in another
3. Search "[Category] [City]" → copy-paste results
4. Do NOT try to visit each website (too slow)
5. Just note: name, address, phone, website Y/N, rating

### Verification (30 min per category)
1. For Tier 1 candidates (high probability), verify phone + website
2. Check if they have recent reviews (shows active business)
3. Check social media presence (Instagram/Facebook for image businesses)

### Automation Options
- Google Maps API (paid, can scrape business data)
- Yelp API (paid, similar)
- Manual scraping (free, slower, requires spreadsheet skills)

**Recommendation:** Manual for first region (learn the process), consider API if you're doing 5+ regions.

---

## RED FLAGS (These might be wrong/outdated)

- ❌ Phone number is wrong (ask when you call)
- ❌ No reviews in 6+ months (might be closed)
- ❌ Old photos/branding on Google Maps (might have moved/rebranded)
- ❌ Website domain error/parked domain (might be inactive)

**Mitigation:** Always verify with phone call before first contact. "Hi, is [Business] still operating at [address]?"

---

## SUMMARY: FASTEST RESEARCH APPROACH

**Time estimate: 2-3 days for a region**

**Day 1 (Mapping):**
- Identify 3-4 high-probability industries in your target region
- Google Maps search each + compile basic list
- ~100-200 prospects compiled

**Day 2 (Scoring):**
- Add website status, ratings, review recency
- Score each by probability formula
- Identify Tier 1 (top 20-30)

**Day 3 (Templates + Setup):**
- Create email templates
- Create tracking sheet
- Ready to send

**Total effort:** 4-6 hours active work + 2-3 hours waiting on research

