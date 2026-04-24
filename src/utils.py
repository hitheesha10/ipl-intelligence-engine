def generate_insight(df):

    chase_win = df['Chased Successfully'].mean() * 100
    avg_runs = df['Runs From Ball'].mean()
    avg_wickets = df['Wicket'].mean() * 6  # wickets per over approx

    insight = ""

    # Strategy insight
    if chase_win > 55:
        insight += "📈 Chasing is the dominant strategy. "
    elif chase_win < 45:
        insight += "🛡️ Defending totals is more effective. "
    else:
        insight += "⚖️ Balanced contest between chasing and defending. "

    # Scoring pattern
    if avg_runs > 1.4:
        insight += "🔥 High-scoring matches dominate this dataset. "
    else:
        insight += "🎯 Bowling-friendly conditions observed. "

    # Wicket behavior
    if avg_wickets > 1.5:
        insight += "💥 Frequent wicket falls increase match volatility."
    else:
        insight += "🧱 Stable batting performances are common."

    return insight