"""
ATAPDIGITAL AI PROMPT LIBRARY
=============================
Live Demo Script

Ikuti instruksi di bawah untuk menjalankan demo live!
"""

import sys
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from SCRIPTS.prompt_runner import run_prompt

def save_output(content: str, filename: str):
    path = Path(f"EXAMPLES/sample_outputs/{filename}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path

# ============================================================
# PILIH DEMO YANG MAU DIJALANKAN
# ============================================================
# Hapus # di depan pilihan yang kamu mau, tambahkan # di pilihan lain
# Contoh:
#     PILIHAN = "1"  # Competitor Analysis
#     PILIHAN = "2"  # Caption Variations
#     PILIHAN = "3"  # Content Ideas
# ============================================================

PILIHAN = "1"  # <-- GANTI ANGKA INI SESUAI PILIHANMU

print("=" * 60)
print("ATAPDIGITAL AI PROMPT LIBRARY - LIVE DEMO")
print("=" * 60)

# ============================================================
# DEMO 1: ANALISIS KOMPETITOR
# ============================================================
if PILIHAN == "1":
    print("\n[MENU 1: ANALISIS KOMPETITOR]")
    print("-" * 40)
    print("Contoh: Analisis @erigo, @wardah, @somethinc, dll")
    print()

    # DATA YANG PERLU DIISI
    brand_name = input("Nama Brand (contoh: @wardah): ") or "@wardah"
    platform = input("Platform (Instagram/TikTok): ") or "Instagram"
    handle = input("Handle/Username: ") or brand_name
    industry = input("Industri (contoh: Skincare Indonesia): ") or "Skincare Indonesia"

    print("\nData Posts (paste dari Instagram):")
    print("(Ketik 'selesai' kalau sudah)")
    print("-" * 40)
    posts_lines = []
    while True:
        line = input()
        if line.lower() == 'selesai':
            break
        posts_lines.append(line)
    posts_data = "\n".join(posts_lines)

    avg_likes = input("\nAvg Likes per post (kosongkan jika tidak tahu): ") or "5000"
    avg_comments = input("Avg Comments (kosongkan jika tidak tahu): ") or "100"
    avg_saves = input("Avg Saves (kosongkan jika tidak tahu): ") or "200"
    engagement_rate = input("Engagement Rate % (kosongkan jika tidak tahu): ") or "3.5"

    context = {
        "brand_name": brand_name,
        "platform": platform,
        "handle": handle,
        "industry": industry,
        "posts_data": posts_data or "Data tidak tersedia",
        "avg_likes": avg_likes,
        "avg_comments": avg_comments,
        "avg_saves": avg_saves,
        "engagement_rate": engagement_rate
    }

    print("\nGenerating analysis...")
    result = run_prompt(
        "PROMPTS/01_competitor_research/analyze_competitor.md",
        context=context,
        max_tokens=4096
    )

    filename = f"live_demo_competitor_{brand_name.replace('@', '')}.md"
    path = save_output(result, filename)
    print(f"\n[DONE] Saved to: {path}")

# ============================================================
# DEMO 2: VARIASI CAPTION
# ============================================================
elif PILIHAN == "2":
    print("\n[MENU 2: VARIASI CAPTION]")
    print("-" * 40)
    print("Contoh: Caption untuk produk baru, promo, dll")
    print()

    brand_name = input("Nama Brand: ") or "Skincare Brand"
    brand_voice = input("Brand Voice (contoh: friendly, professional): ") or "Friendly, casual"
    target_audience = input("Target Audiens: ") or "Perempuan 20-30 tahun"
    topic = input("Topik Caption: ") or "Benefits of our new serum product"
    format_type = input("Format (Instagram/TikTok): ") or "Instagram"
    primary_message = input("Pesan Utama: ") or "Product ini bagus untuk kulit"

    context = {
        "brand_name": brand_name,
        "brand_voice": brand_voice,
        "target_audience": target_audience,
        "topic": topic,
        "format": format_type,
        "primary_message": primary_message
    }

    print("\nGenerating captions...")
    result = run_prompt(
        "PROMPTS/02_content_strategy/caption_variations.md",
        context=context,
        max_tokens=4096
    )

    filename = f"live_demo_caption_{topic[:20].replace(' ', '_')}.md"
    path = save_output(result, filename)
    print(f"\n[DONE] Saved to: {path}")

# ============================================================
# DEMO 3: IDE KONTEN
# ============================================================
elif PILIHAN == "3":
    print("\n[MENU 3: IDE KONTEN]")
    print("-" * 40)
    print("Contoh: Plan konten bulanan untuk brand kamu")
    print()

    brand_name = input("Nama Brand: ") or "Coffee Brand"
    industry = input("Industri: ") or "Coffee & Cafe Indonesia"
    target_audience = input("Target Audiens: ") or "Young professionals 25-35"
    brand_voice = input("Brand Voice: ") or "Premium but approachable"
    primary_goal = input("Goal Utama: ") or "Increase engagement"

    context = {
        "brand_name": brand_name,
        "industry": industry,
        "target_audience": target_audience,
        "brand_voice": brand_voice,
        "primary_goal": primary_goal,
        "campaign_period": "Next 30 days",
        "data_insights": " belum ada data, bisa kosongkan",
        "competitor_examples": " belum ada data, bisa kosongkan",
        "budget": "Limited",
        "team_capacity": "1 content creator",
        "platform_priority": "Instagram",
        "theme_1": "Education",
        "theme_2": "Lifestyle",
        "theme_3": "Behind the scenes",
        "theme_4": "Product showcase"
    }

    print("\nGenerating content ideas...")
    result = run_prompt(
        "PROMPTS/02_content_strategy/generate_ideas.md",
        context=context,
        max_tokens=4096
    )

    filename = f"live_demo_ideas_{brand_name[:15].replace(' ', '_')}.md"
    path = save_output(result, filename)
    print(f"\n[DONE] Saved to: {path}")

print("\n" + "=" * 60)
print("Buka folder EXAMPLES/sample_outputs/ untuk melihat hasil!")
print("=" * 60)
