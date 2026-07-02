"""
AtapDigital AI Prompt Library - Demo Runner
Generate sample outputs untuk portfolio showcase
"""

import sys
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from SCRIPTS.prompt_runner import run_prompt

def save_output(content: str, filename: str):
    """Save output to file."""
    path = Path(f"EXAMPLES/sample_outputs/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[SAVED] {path}")
    return path

def main():
    print("=" * 60)
    print("AtapDigital AI Prompt Library - Demo Runner")
    print("=" * 60)

    # ============================================================
    # DEMO 1: Competitor Analysis - Brand Fashion
    # ============================================================
    print("\n" + "=" * 60)
    print("DEMO 1: Competitor Analysis - @erigo.id (Fashion)")
    print("=" * 60)

    competitor_context = {
        "brand_name": "@erigo.id",
        "platform": "Instagram",
        "handle": "@erigo.id",
        "industry": "Fashion Streetwear Indonesia",
        "posts_data": """
POST 1: "New Drop Alert! 🔥 Erigo x Local Artist Collection"
Likes: 25K | Comments: 892 | Saves: 3.2K | Format: Carousel

POST 2: "Outfit inspo buat daily kamu dari @erigo.id"
Likes: 18K | Comments: 456 | Saves: 2.1K | Format: Reels

POST 3: "Behind the scenes - Photoshoot process"
Likes: 12K | Comments: 234 | Saves: 890 | Format: Stories Reels

POST 4: "Limited Edition! Erigo x [Collab] sold out in 2 hours!"
Likes: 32K | Comments: 1.5K | Saves: 4.5K | Format: Static + Video

POST 5: "Customer style: How our followers style Erigo"
Likes: 8.5K | Comments: 567 | Saves: 1.8K | Format: Carousel UGC

POST 6: "Promo week: Discount up to 40% + free shipping!"
Likes: 15K | Comments: 345 | Saves: 567 | Format: Static
        """,
        "avg_likes": "18500",
        "avg_comments": "675",
        "avg_saves": "2150",
        "engagement_rate": "5.2"
    }

    try:
        result = run_prompt(
            "PROMPTS/01_competitor_research/analyze_competitor.md",
            context=competitor_context,
            max_tokens=4096
        )
        path = save_output(result, "demo_01_competitor_analysis_erigo.md")
        print(f"[SUCCESS] Demo 1 completed!")
    except Exception as e:
        print(f"[ERROR] Demo 1 failed: {e}")

    # ============================================================
    # DEMO 2: Caption Variations - Skincare Product
    # ============================================================
    print("\n" + "=" * 60)
    print("DEMO 2: Caption Variations - Niacinamide Product")
    print("=" * 60)

    caption_context = {
        "brand_name": "Skincare Brand",
        "brand_voice": "Casual, friendly, educational - like a knowledgeable friend",
        "target_audience": "Perempuan 20-30 tahun, skincare enthusiast di Indonesia",
        "topic": "Niacinamide 10% - Benefits dan kenapa harus punya di skincare routine",
        "format": "Instagram Feed Post",
        "primary_message": "Niacinamide adalah all-rounder ingredient yang cocok untuk semua skin type, membantu minimize pores, control oil, dan brighten skin tone"
    }

    try:
        result = run_prompt(
            "PROMPTS/02_content_strategy/caption_variations.md",
            context=caption_context,
            max_tokens=4096
        )
        path = save_output(result, "demo_02_caption_variations_niacinamide.md")
        print(f"[SUCCESS] Demo 2 completed!")
    except Exception as e:
        print(f"[ERROR] Demo 2 failed: {e}")

    # ============================================================
    # DEMO 3: Content Ideas - Coffee Brand
    # ============================================================
    print("\n" + "=" * 60)
    print("DEMO 3: Content Ideas - Coffee Subscription Brand")
    print("=" * 60)

    ideas_context = {
        "brand_name": "BrewBean Coffee",
        "industry": "Coffee Subscription & Cafe - Indonesia",
        "target_audience": "Young professionals 25-40, coffee enthusiasts, urban millennials",
        "brand_voice": "Passionate about quality coffee, educational, premium but approachable",
        "primary_goal": "Increase brand awareness dan engagement untuk subscription service",
        "campaign_period": "Q3 2026",
        "data_insights": """
- Audience interested in coffee origin stories
- Behind-the-scenes content perform 3x better
- User-generated content (brew reviews) very limited
- Competitors focus on product, not experience
- High interest in 'coffee hack' content
        """,
        "competitor_examples": """
- @kopi_kenangan: Meme-heavy, viral content
- @coffee_toffee: Promo-focused, casual
- @javagate: Premium, educational about beans
        """,
        "budget": "Limited - focus on organic content",
        "team_capacity": "1 content creator, 1 designer",
        "platform_priority": "Instagram first, TikTok second",
        "theme_1": "Coffee Education",
        "theme_2": "Lifestyle & Morning Ritual",
        "theme_3": "Behind the Scenes",
        "theme_4": "Subscription Value Prop"
    }

    try:
        result = run_prompt(
            "PROMPTS/02_content_strategy/generate_ideas.md",
            context=ideas_context,
            max_tokens=4096
        )
        path = save_output(result, "demo_03_content_ideas_brewbean.md")
        print(f"[SUCCESS] Demo 3 completed!")
    except Exception as e:
        print(f"[ERROR] Demo 3 failed: {e}")

    print("\n" + "=" * 60)
    print("ALL DEMOS COMPLETED!")
    print("=" * 60)
    print("\nCheck EXAMPLES/sample_outputs/ for results")
    print("These outputs can be used as portfolio showcase.")

if __name__ == "__main__":
    main()
