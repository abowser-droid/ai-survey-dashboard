# XLS to DB - Survey Data Explorer

Interactive dashboard for the 2025 Alliance AI Survey. Converts Excel to SQLite, visualizes with Streamlit.

## Quick Start

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
| `.venv/` | Python environment |

## Setup (First Time)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl streamlit plotly datasette
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
