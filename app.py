import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Survey Explorer", layout="wide")

# Load data
@st.cache_data
def load_data():
    conn = sqlite3.connect("survey.db")
    df = pd.read_sql("SELECT * FROM Sheet", conn)
    df = df[df.iloc[:, 0] != "Response"]
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

freq_col = "How often are you using AI PROFESSIONALLY (i.e., for work purposes in CME/CPD)?"
freq_options = sorted(df[freq_col].dropna().unique().tolist())
selected_freqs = st.sidebar.multiselect("AI Usage Frequency", freq_options, default=freq_options)

content_col = "Do you use AI for your work in content creation and writing?"
content_options = sorted(df[content_col].dropna().unique().tolist())
selected_content = st.sidebar.multiselect("Uses AI: Content Creation", content_options, default=content_options)

research_col = "Do you use AI for your work in educational research and needs assessment?"
research_options = sorted(df[research_col].dropna().unique().tolist())
selected_research = st.sidebar.multiselect("Uses AI: Research", research_options, default=research_options)

data_col = "Do you use AI for your work in learner data and outcomes analysis?"
data_options = sorted(df[data_col].dropna().unique().tolist())
selected_data = st.sidebar.multiselect("Uses AI: Data Analysis", data_options, default=data_options)

# Apply filters
filtered_df = df.copy()
if selected_freqs:
    filtered_df = filtered_df[filtered_df[freq_col].isin(selected_freqs)]
if selected_content:
    filtered_df = filtered_df[filtered_df[content_col].isin(selected_content)]
if selected_research:
    filtered_df = filtered_df[filtered_df[research_col].isin(selected_research)]
if selected_data:
    filtered_df = filtered_df[filtered_df[data_col].isin(selected_data)]

# Header
st.title("2025 Alliance AI Survey")
is_filtered = (len(selected_freqs) < len(freq_options) or
               len(selected_content) < len(content_options) or
               len(selected_research) < len(research_options) or
               len(selected_data) < len(data_options))
st.markdown(f"**{len(filtered_df)} responses**" + (" *(filtered)*" if is_filtered else ""))
st.markdown("---")

# Question definitions
questions = {
    "AI Usage Frequency": {
        "col": "How often are you using AI PROFESSIONALLY (i.e., for work purposes in CME/CPD)?",
        "order": ["Daily", "Weekly", "A few times a month", "A few times a year", "Never"]
    },
    "Content Creation": {
        "col": "Do you use AI for your work in content creation and writing?",
        "order": ["Yes", "No"]
    },
    "Research & Needs Assessment": {
        "col": "Do you use AI for your work in educational research and needs assessment?",
        "order": ["Yes", "No"]
    },
    "Data & Outcomes Analysis": {
        "col": "Do you use AI for your work in learner data and outcomes analysis?",
        "order": ["Yes", "No"]
    },
    "Business Development": {
        "col": "Do you use AI for your work in business development and strategy?",
        "order": ["Yes", "No"]
    },
    "Accreditation & Compliance": {
        "col": "Do you use AI for your work in accreditation and compliance?",
        "order": ["Yes", "No"]
    },
    "Operations & Efficiency": {
        "col": "Do you use AI for your work in operations and process efficiency?",
        "order": ["Yes", "No"]
    },
    "Leadership & Planning": {
        "col": "Do you use AI for your work in leadership and planning?",
        "order": ["Yes", "No"]
    },
}

def render_question(title, col, order=None):
    """Render a SurveyMonkey-style question breakdown."""
    counts = filtered_df[col].value_counts()
    total = counts.sum()

    # Build dataframe with percentages
    data = []
    for val in (order if order else counts.index):
        if val in counts.index:
            count = counts[val]
            pct = (count / total) * 100
            data.append({"Response": val, "Count": count, "Percent": pct})

    chart_df = pd.DataFrame(data)

    # Question header with full text
    st.subheader(title)
    st.markdown(f"**{col}**")

    # Horizontal bar chart
    fig = px.bar(
        chart_df,
        x="Percent",
        y="Response",
        orientation="h",
        text=chart_df.apply(lambda r: f"{r['Percent']:.1f}% ({int(r['Count'])})", axis=1),
        color="Response",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        showlegend=False,
        xaxis_title="",
        yaxis_title="",
        xaxis=dict(range=[0, 100], ticksuffix="%"),
        height=max(150, len(chart_df) * 40 + 50),
        margin=dict(l=0, r=0, t=10, b=10),
        yaxis=dict(autorange="reversed")
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    # Data table underneath
    with st.expander("View data"):
        display_df = chart_df.copy()
        display_df["Percent"] = display_df["Percent"].apply(lambda x: f"{x:.1f}%")
        st.dataframe(display_df, hide_index=True, use_container_width=True)

    st.markdown("---")

# Render each question
for title, config in questions.items():
    render_question(title, config["col"], config.get("order"))

# Raw data section
st.header("Individual Responses")
st.dataframe(filtered_df, use_container_width=True, height=400)
