import streamlit as st
import pandas as pd

from src.preprocess import load_data
from src.features import create_features
from src.model import train_model
from src.utils import generate_insight

# ---------------- LOAD ---------------- #
df = load_data("data/ball_by_ball_ipl.csv")
df = create_features(df)

model, acc = train_model(df)

st.set_page_config(layout="wide")
st.title("🏏 IPL Intelligence Engine")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("Filters")

year = st.sidebar.selectbox("Year", sorted(df['Year'].unique()))
match_id = st.sidebar.selectbox("Match", df['Match ID'].unique())

filtered_df = df[df['Year'] == year]
match_df = df[df['Match ID'] == match_id]

# ---------------- KPIs ---------------- #
col1, col2, col3 = st.columns(3)

col1.metric("Matches", filtered_df['Match ID'].nunique())
col2.metric("Avg Runs", round(filtered_df['Runs From Ball'].mean(), 2))
col3.metric("Model Accuracy", f"{round(acc*100,2)}%")

# ---------------- TABS ---------------- #
tab1, tab2, tab3, tab4 = st.tabs([
    "Batting",
    "Bowling",
    "Match AI",
    "Player Analysis"
])

# ---------------- BATTING ---------------- #
with tab1:
    st.subheader("Top Batters")

    top_batters = (filtered_df.groupby('Batter')['Batter Runs']
                   .sum()
                   .sort_values(ascending=False)
                   .head(10))

    st.bar_chart(top_batters)

# ---------------- BOWLING ---------------- #
with tab2:
    st.subheader("Top Bowlers")

    top_bowlers = (filtered_df.groupby('Bowler')['Wicket']
                   .sum()
                   .sort_values(ascending=False)
                   .head(10))

    st.bar_chart(top_bowlers)

    st.subheader("Phase Analysis")

    phase_stats = filtered_df.groupby('Phase')['Runs From Ball'].mean()
    st.bar_chart(phase_stats)

# ---------------- MATCH AI ---------------- #
with tab3:
    st.subheader("Win Probability Curve")

    match_df = match_df.copy()

    match_df['win_prob'] = model.predict_proba(
        match_df[['Runs to Get', 'Balls Remaining', 'Innings Wickets']]
    )[:,1]

    st.line_chart(match_df['win_prob'])

    st.subheader("Live Predictor")

    runs = st.number_input("Runs Needed", 1, 300)
    balls = st.number_input("Balls Remaining", 1, 120)
    wickets = st.slider("Wickets Lost", 0, 10)

    prob = model.predict_proba([[runs, balls, wickets]])[0][1]

    st.metric("Win Probability", f"{round(prob*100,2)}%")

    st.subheader("Insight")
    st.success(generate_insight(filtered_df))

# ---------------- PLAYER ANALYSIS ---------------- #
with tab4:
    st.subheader("Player Comparison")

    p1 = st.selectbox("Player 1", df['Batter'].unique())
    p2 = st.selectbox("Player 2", df['Batter'].unique())

    compare = df[df['Batter'].isin([p1, p2])]

    st.bar_chart(compare.groupby('Batter')['Batter Runs'].sum())

    st.subheader("Clutch Performance")

    clutch = df[df['pressure_index'] > 1.2]

    clutch_stats = (clutch.groupby('Batter')['Batter Runs']
                    .mean()
                    .sort_values(ascending=False)
                    .head(10))

    st.bar_chart(clutch_stats)