# XLS to DB Project

Survey data explorer — Excel → SQLite → Streamlit dashboard.

## Live App

**https://ai-survey-dashboard.streamlit.app**

## Quick Start (Local)

```bash
source .venv/bin/activate
streamlit run app.py
open http://localhost:8501
```

## Deployment

Hosted on Streamlit Community Cloud. Auto-deploys from GitHub.

```bash
# Push changes to redeploy
git add -A && git commit -m "Update" && git push
```

- **Repo:** https://github.com/abowser-droid/ai-survey-dashboard
- **App:** https://ai-survey-dashboard.streamlit.app

## Data

- **Source:** 2025 Alliance AI Survey (CME/CPD professionals, de-identified)
- **Database:** `survey.db` — 199 responses, 114 columns
- **Table:** `Sheet`

## Dashboard Features

- Horizontal bar charts per question (Plotly)
- Multi-select sidebar filters
- Full question text under each header
- Expandable data tables
- Raw response data at bottom

## Current Filters

| Filter | Column |
|--------|--------|
| AI Usage Frequency | How often are you using AI PROFESSIONALLY... |
| Content Creation | Do you use AI for your work in content creation... |
| Research | Do you use AI for your work in educational research... |
| Data Analysis | Do you use AI for your work in learner data... |

## Key Questions Charted

| Short Name | Full Column |
|------------|-------------|
| AI Usage Frequency | How often are you using AI PROFESSIONALLY (i.e., for work purposes in CME/CPD)? |
| Content Creation | Do you use AI for your work in content creation and writing? |
| Research & Needs Assessment | Do you use AI for your work in educational research and needs assessment? |
| Data & Outcomes Analysis | Do you use AI for your work in learner data and outcomes analysis? |
| Business Development | Do you use AI for your work in business development and strategy? |
| Accreditation & Compliance | Do you use AI for your work in accreditation and compliance? |
| Operations & Efficiency | Do you use AI for your work in operations and process efficiency? |
| Leadership & Planning | Do you use AI for your work in leadership and planning? |

## Files

- `app.py` — Streamlit dashboard
- `survey.db` — SQLite database
- `requirements.txt` — Dependencies for cloud deploy
- `.venv/` — Local Python env (pandas, streamlit, plotly, datasette)

## Adding More Filters

In `app.py`, add a new filter block:
```python
col = "Column Name"
options = sorted(df[col].dropna().unique().tolist())
selected = st.sidebar.multiselect("Label", options, default=options)

# Then add to the filter chain:
if selected:
    filtered_df = filtered_df[filtered_df[col].isin(selected)]
```

## SQL Examples

```sql
-- Daily users who use AI for content creation
SELECT * FROM Sheet
WHERE "How often are you using AI PROFESSIONALLY (i.e., for work purposes in CME/CPD)?" = 'Daily'
AND "Do you use AI for your work in content creation and writing?" = 'Yes';
```

## Notes

- First Excel row was headers; filtered out in app
- Multi-select questions span Unnamed:N columns
- All columns stored as TEXT
