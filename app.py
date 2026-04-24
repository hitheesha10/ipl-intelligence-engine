import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import from src (MODULAR ARCHITECTURE)
from src.preprocess import load_data
from src.features import create_features
from src.model import train_model
from src.utils import generate_insight


# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(layout="wide")
st.title("🏏 IPL Intelligence Engine")


# ---------------- LOAD DATA ---------------- #
@st.cache_data
def load_pipeline():
    df = load_data("data/ball_by_ball_ipl.csv")
    df = create_features(df)
    model, acc = train_model(df)
    return df, model, acc

df, model, acc = load_pipeline()


# ---------------- COMMENTARY FUNCTION ---------------- #
def generate_commentary(row):

    if row['Wicket'] == 1:
        return f"💥 WICKET! {row['Player Out']} is out ({row['Method']})!"
    elif row['Batter Runs'] == 6:
        return "🔥 SIX! Massive hit!"
    elif row['Batter Runs'] == 4:
        return "⚡ FOUR! Beautiful shot!"
    elif row['Runs From Ball'] == 0:
        return "🛑 Dot ball."
    elif row['Runs From Ball'] == 1:
        return "➡️ Single."
    elif row['Runs From Ball'] == 2:
        return "🏃 Two runs."
    elif row['Runs From Ball'] == 3:
        return "🏃🏃 Three runs!"
    else:
        return f"{row['Runs From Ball']} runs"


# ---------------- SIDEBAR ---------------- #
st.sidebar.title("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))
match_id = st.sidebar.selectbox("Select Match", df['Match ID'].unique())

filtered_df = df[df['Year'] == year]
match_df = df[df['Match ID'] == match_id].copy()


# ---------------- KPIs ---------------- #
col1, col2, col3 = st.columns(3)

col1.metric("Matches", filtered_df['Match ID'].nunique())
col2.metric("Avg Runs/Ball", round(filtered_df['Runs From Ball'].mean(), 2))
col3.metric("Model Accuracy", f"{round(acc*100,2)}%")


# ---------------- TABS ---------------- #
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Batting",
    "Bowling",
    "Match AI",
    "Player Analysis",
    "Match Replay 🎬"
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

    st.subheader("📈 Win Probability Curve")

    match_df = match_df.sort_values(['Innings', 'Over', 'Ball']).copy()
    match_df['ball_number'] = range(len(match_df))

    match_df['win_prob'] = model.predict_proba(
        match_df[['Runs to Get', 'Balls Remaining', 'Innings Wickets']]
    )[:, 1]

    fig, ax = plt.subplots()
    ax.plot(match_df['ball_number'], match_df['win_prob'])
    ax.set_xlabel("Ball Progression")
    ax.set_ylabel("Win Probability")
    ax.set_title("Match Win Probability Curve")

    st.pyplot(fig)

    # Insight
    final_prob = match_df['win_prob'].iloc[-1]

    if final_prob > 0.7:
        st.success("Dominant chase performance detected.")
    elif final_prob < 0.3:
        st.warning("Strong defense by bowling team.")
    else:
        st.info("Highly competitive match with momentum shifts.")

    # Predictor
    st.subheader("🎯 Live Match Predictor")

    runs = st.number_input("Runs Needed", 1, 300)
    balls = st.number_input("Balls Remaining", 1, 120)
    wickets = st.slider("Wickets Lost", 0, 10)

    prob = model.predict_proba([[runs, balls, wickets]])[0][1]

    st.metric("Win Probability", f"{round(prob*100,2)}%")

    st.subheader("🧠 Insight")
    st.success(generate_insight(filtered_df))


# ---------------- PLAYER ANALYSIS ---------------- #
with tab4:

    st.subheader("⚔️ Player vs Player Comparison")

    p1 = st.selectbox("Player 1", df['Batter'].unique())
    p2 = st.selectbox("Player 2", df['Batter'].unique())

    player_df = df[df['Batter'].isin([p1, p2])]

    comparison = player_df.groupby('Batter').agg({
        'Batter Runs': 'sum',
        'Batter Balls Faced': 'sum',
        'is_six': 'sum'
    })

    comparison['Strike Rate'] = (
        comparison['Batter Runs'] / comparison['Batter Balls Faced'] * 100
    )

    st.dataframe(comparison)

    st.subheader("📊 Performance Comparison")
    st.bar_chart(comparison[['Batter Runs', 'Strike Rate', 'is_six']])

    winner = comparison['Batter Runs'].idxmax()
    st.success(f"🏆 Better Performer: {winner}")

    st.subheader("🔥 Clutch Performers")

    clutch = df[df['pressure_index'] > 1.2]

    clutch_stats = (clutch.groupby('Batter')['Batter Runs']
                    .mean()
                    .sort_values(ascending=False)
                    .head(10))

    st.bar_chart(clutch_stats)


# ---------------- MATCH REPLAY ---------------- #
with tab5:

    st.subheader("🎬 Smart Match Replay")

    match_ids = df['Match ID'].unique()
    selected_match = st.selectbox("Select Match", match_ids)

    replay_df = df[df['Match ID'] == selected_match].copy()
    replay_df = replay_df.sort_values(['Innings', 'Over', 'Ball'])

    replay_df['commentary'] = replay_df.apply(generate_commentary, axis=1)

    replay_df['win_prob'] = model.predict_proba(
        replay_df[['Runs to Get', 'Balls Remaining', 'Innings Wickets']]
    )[:, 1]

    ball_index = st.slider("Scrub Through Match", 0, len(replay_df) - 1, 0)

    current = replay_df.iloc[ball_index]

    st.markdown(f"""
    ### 🏏 Over {current['Over']}.{current['Ball']}
    **Score:** {current['Innings Runs']}/{current['Innings Wickets']}  
    **Event:** {current['commentary']}  
    """)

    st.progress(float(current['win_prob']))
    st.write(f"Win Probability: {round(current['win_prob']*100,2)}%")

    st.subheader("📜 Recent Events")

    history = replay_df.iloc[max(0, ball_index-5):ball_index+1]

    for _, row in history.iterrows():
        st.write(f"{row['Over']}.{row['Ball']} → {row['commentary']}")