#!/usr/bin/env python3
"""
Lead Scoring Automation Script

Scores prospects based on industry probability, website status, and business signals.
Input: CSV with prospect data
Output: CSV with scores + tier assignment

Usage:
    python lead_scorer.py input.csv --output scored.csv

Input CSV format:
    business_name,address,category,website_status,reviews_count,rating,recent_reviews,social_media,notes

Output CSV format:
    [all input columns] + score + tier
"""

import csv
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Industry classification (1.0 = high, 0.7 = medium, 0.2 = low)
INDUSTRY_WEIGHTS = {
    # HIGH PROBABILITY (0.9-1.0)
    "salon": 1.0,
    "hair salon": 1.0,
    "barber": 1.0,
    "hairdresser": 1.0,
    "massage": 1.0,
    "wellness": 1.0,
    "massage therapy": 1.0,
    "spa": 1.0,
    "fitness": 1.0,
    "gym": 1.0,
    "fitness studio": 1.0,
    "yoga": 1.0,
    "pilates": 1.0,
    "restaurant": 1.0,
    "cafe": 1.0,
    "coffee": 1.0,
    "bar": 1.0,
    "beauty": 1.0,
    "nail": 1.0,
    "aesthetics": 1.0,
    "skincare": 1.0,
    
    # MEDIUM PROBABILITY (0.5-0.7)
    "retail": 0.7,
    "shop": 0.7,
    "boutique": 0.7,
    "jewelry": 0.7,
    "carpenter": 0.7,
    "carpentry": 0.7,
    "electrician": 0.5,
    "plumber": 0.5,
    "plumbing": 0.5,
    "hvac": 0.2,
    "heating": 0.2,
    "trainer": 0.6,
    "personal trainer": 0.6,
    "coach": 0.5,
    
    # LOW PROBABILITY (0.1-0.3)
    "gas station": 0.1,
    "convenience": 0.1,
    "laundromat": 0.1,
}

# Website status weights (1.0 = none, 0.7 = outdated, 0.4 = old, 0.1 = current)
WEBSITE_STATUS_MAP = {
    "none": 1.0,
    "no": 1.0,
    "n": 1.0,
    "outdated": 0.7,
    "old": 0.7,
    "dated": 0.7,
    "good": 0.4,
    "decent": 0.4,
    "current": 0.1,
    "yes": 0.1,
    "y": 0.1,
}

# Business signal scoring
def score_business_signals(
    reviews_count: int,
    rating: float,
    recent_reviews: str,
    social_media: str
) -> float:
    """
    Score business signals (0.0 = weak, 1.0 = strong)
    
    Factors:
    - Recent reviews (reviews in last 30 days)
    - Review count (more = more active)
    - Rating (4.5+ = strong)
    - Social media presence (yes = +0.3)
    """
    score = 0.0
    
    # Recent reviews (weighted most heavily)
    if recent_reviews.lower() in ["yes", "y", "true", "1"]:
        score += 0.5
    
    # Review count
    if reviews_count >= 20:
        score += 0.2
    elif reviews_count >= 10:
        score += 0.1
    
    # Rating
    if rating >= 4.5:
        score += 0.2
    elif rating >= 4.0:
        score += 0.1
    
    # Social media
    if social_media.lower() in ["yes", "y", "true", "1"]:
        score += 0.1
    
    return min(score, 1.0)  # Cap at 1.0

def get_industry_weight(category: str) -> float:
    """Get industry weight from category string"""
    category_lower = category.lower().strip()
    
    # Exact match first
    if category_lower in INDUSTRY_WEIGHTS:
        return INDUSTRY_WEIGHTS[category_lower]
    
    # Substring match
    for key, weight in INDUSTRY_WEIGHTS.items():
        if key in category_lower or category_lower in key:
            return weight
    
    # Default: medium probability
    return 0.5

def get_website_weight(status: str) -> float:
    """Get website weight from status"""
    status_lower = status.lower().strip()
    return WEBSITE_STATUS_MAP.get(status_lower, 0.7)

def calculate_score(
    industry_weight: float,
    website_weight: float,
    signals_weight: float
) -> int:
    """Calculate final score (1-10)"""
    score = (industry_weight * 0.5) + (website_weight * 0.3) + (signals_weight * 0.2)
    return max(1, min(10, int(round(score * 10))))

def get_tier(score: int) -> str:
    """Assign tier based on score"""
    if score >= 9:
        return "TIER 1"
    elif score >= 6:
        return "TIER 2"
    else:
        return "TIER 3"

def score_leads(input_file: str, output_file: str):
    """Read CSV, score each lead, write output"""
    leads = []
    
    # Read input
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    
    if not leads:
        print(f"Error: No leads found in {input_file}")
        sys.exit(1)
    
    print(f"Scoring {len(leads)} leads...")
    
    # Score each lead
    for lead in leads:
        category = lead.get('category', 'unknown')
        website_status = lead.get('website_status', 'unknown')
        reviews_count = int(lead.get('reviews_count', 0)) if lead.get('reviews_count', '0').isdigit() else 0
        rating = float(lead.get('rating', 0)) if lead.get('rating', '0').replace('.','').isdigit() else 0
        recent_reviews = lead.get('recent_reviews', 'no')
        social_media = lead.get('social_media', 'no')
        
        industry_weight = get_industry_weight(category)
        website_weight = get_website_weight(website_status)
        signals_weight = score_business_signals(reviews_count, rating, recent_reviews, social_media)
        
        score = calculate_score(industry_weight, website_weight, signals_weight)
        tier = get_tier(score)
        
        lead['score'] = score
        lead['tier'] = tier
        lead['industry_weight'] = round(industry_weight, 2)
        lead['website_weight'] = round(website_weight, 2)
        lead['signals_weight'] = round(signals_weight, 2)
    
    # Write output
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = list(leads[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)
    
    # Summary
    tier1_count = sum(1 for lead in leads if lead['tier'] == 'TIER 1')
    tier2_count = sum(1 for lead in leads if lead['tier'] == 'TIER 2')
    tier3_count = sum(1 for lead in leads if lead['tier'] == 'TIER 3')
    
    print(f"\n✅ Scoring complete!")
    print(f"  TIER 1 (9-10): {tier1_count} leads (highest priority)")
    print(f"  TIER 2 (6-8):  {tier2_count} leads (secondary)")
    print(f"  TIER 3 (1-5):  {tier3_count} leads (skip)")
    print(f"\n📊 Results saved to: {output_file}")
    print(f"\n💡 Recommendation: Start with TIER 1, only move to TIER 2 after TIER 1 is worked.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lead_scorer.py input.csv [--output output.csv]")
        print("\nInput CSV must have columns:")
        print("  business_name, address, category, website_status, reviews_count,")
        print("  rating, recent_reviews, social_media, [notes]")
        print("\nExample:")
        print("  python lead_scorer.py prospects.csv --output scored.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--output" else "scored_leads.csv"
    
    if not Path(input_file).exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    score_leads(input_file, output_file)
