# XLS to DB - Survey Data Explorer

Interactive dashboard for the 2025 Alliance AI Survey. Converts Excel to SQLite, visualizes with Streamlit.

## Live App

**https://ai-survey-dashboard.streamlit.app**

Share this link with collaborators — filters work for everyone.

## Local Development

```bash
source .venv/bin/activate
streamlit run app.py
```

Opens at **http://localhost:8501**

## Features

- **SurveyMonkey-style charts** — horizontal bar charts with percentages and counts
- **Multi-select filters** — slice data by multiple criteria simultaneously
- **Full question text** — each chart shows the complete survey question
- **Expandable data tables** — click to see raw numbers under each chart
- **Individual responses** — full data table at the bottom

## Filters

Sidebar filters (all multi-select):
- AI Usage Frequency (Daily, Weekly, Monthly, etc.)
- Uses AI: Content Creation (Yes/No)
- Uses AI: Research (Yes/No)
- Uses AI: Data Analysis (Yes/No)

Charts and data update instantly when you change filters.

## Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit dashboard |
| `survey.db` | SQLite database (200 rows, 114 columns) |
| `2025 Alliance AI Survey Results-deidentified.xlsx` | Original Excel source |
| `.venv/` | Python environment (local only) |
| `requirements.txt` | Dependencies for Streamlit Cloud |

## Setup (First Time Local)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl streamlit plotly datasette
```

## Deployment

Hosted on Streamlit Community Cloud. Deploys automatically from `main` branch.

- **Repo:** https://github.com/abowser-droid/ai-survey-dashboard
- **App:** https://ai-survey-dashboard.streamlit.app

To redeploy after changes:
```bash
git add -A && git commit -m "Update" && git push
```

## Alternative: SQL Queries

Command line:
```bash
sqlite3 survey.db "SELECT * FROM Sheet LIMIT 10;"
```

Datasette (technical web UI):
```bash
source .venv/bin/activate
datasette survey.db
```
