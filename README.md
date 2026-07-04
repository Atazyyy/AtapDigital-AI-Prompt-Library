# 🎯 AI-Powered Social Media Toolkit for Agencies

Koleksi AI tools dan prompt yang siap pakai untuk workflow social media agency — dirancang untuk riset kompetitor, strategi konten, pelaporan klien, dan pelatihan tim.

Dibuat sebagai portfolio project AI Specialist untuk mendemonstrasikan kemampuan **AI orchestration**, **prompt engineering**, dan **automation** dalam konteks social media marketing agency.

---

## 📂 Struktur Prompt

```
PROMPTS/
├── 01_competitor_research/     # Riset & analisis kompetitor
├── 02_content_strategy/        # Generate ide & rencana konten
├── 03_client_reporting/        # Laporan & insight untuk klien
└── 04_team_training/           # Panduan & SOP penggunaan AI
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install anthropic python-dotenv
```

### 2. Setup Environment

Buat file `.env` di root project:

```env
ANTHROPIC_API_KEY=your-api-key-here
ANTHROPIC_BASE_URL=https://gateway.olagon.site/anthropic
```

### 3. Run Prompt

```bash
cd SCRIPTS
python prompt_runner.py ../PROMPTS/01_competitor_research/analyze_competitor.md
```

Atau import ke script kamu:

```python
from prompt_runner import run_prompt

result = run_prompt(
    "PROMPTS/01_competitor_research/analyze_competitor.md",
    context={"brand_name": "Brand X", "industry": "Fashion"}
)
print(result)
```

---

## 📋 Prompt Catalog

### 01 — Competitor Research

| File | Fungsi |
|------|--------|
| `analyze_competitor.md` | Analisis mendalam satu kompetitor |
| `extract_trends.md` | Extract pattern & tren dari data kompetitor |
| `benchmark_report.md` | Generate laporan benchmark antar kompetitor |

### 02 — Content Strategy

| File | Fungsi |
|------|--------|
| `generate_ideas.md` | Generate ide konten berdasarkan data |
| `caption_variations.md` | Buat variasi caption untuk satu tema |
| `content_calendar.md` | Plan konten 30 hari dengan tema & timing |

### 03 — Client Reporting

| File | Fungsi |
|------|--------|
| `monthly_summary.md` | Rangkum performa bulanan jadi laporan |
| `actionable_insights.md` | Generate insight + rekomendasi action |

### 04 — Team Training

| File | Fungsi |
|------|--------|
| `ai_guidelines.md` | SOP penggunaan AI untuk tim non-teknis |

---

## 💡 Contoh Penggunaan

### Input:
```markdown
Brand: @somethinc
Platform: Instagram
Posts (7 hari terakhir):
[copy paste caption & engagement metrics]
```

### Output:
```markdown
## Analisis Kompetitor: @somethinc

### Key Findings:
1. Gunakan tone casual dengan emoji heavy
2. Fokus ke skincare education
3. Posting peak: 19:00-21:00 WIB

### Content Patterns:
- Tutorial-style content (60%)
- Product review (25%)
- Behind-the-scenes (15%)

### Recommendations:
- Tingkatkan educational content
- Optimalkan posting time
- Gunakan format carousel lebih sering
```

---

## 🎓 Yang Saya Pelajari dari Project Ini

1. **Prompt Engineering** — Mendesain prompt yang menghasilkan output konsisten
2. **Context Management** — Memahami cara memberikan konteks yang cukup tanpa overwhelming
3. **Output Formatting** — Membuat output yang langsung actionable untuk tim
4. **Documentation** — Mendokumentasikan sistem agar bisa dipakai orang lain
5. **AI Integration** — Mengintegrasikan Claude API ke workflow nyata

---

## 🔗 Connect

- **GitHub:** github.com/Atazyyy
- **Email:** agnimiftahfauza@gmail.com
- **Portfolio:** atapdigital.id

---

## 📄 License

MIT License — boleh digunakan dan dimodifikasi untuk pembelajaran.

---

*Made with ❤️ by Agni Miftah Fauzi (@Atazyyy) — AtapDigital*
