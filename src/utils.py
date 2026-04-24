def generate_insight(df):

    chase_win = df['Chased Successfully'].mean() * 100
    avg_runs = df['Runs From Ball'].mean()
    avg_wickets = df['Wicket'].mean() * 6  # wickets per over approx

    insight = ""

    # ---------------- STRATEGY ---------------- #
    if chase_win > 55:
        insight += "📈 Chasing is the dominant strategy. Teams should prefer batting second when possible. "
    elif chase_win < 45:
        insight += "🛡️ Defending totals is more effective. Setting a target creates pressure advantage. "
    else:
        insight += "⚖️ Balanced contest — toss decision has minimal impact. "

    # ---------------- SCORING PATTERN ---------------- #
    if avg_runs > 1.4:
        insight += "🔥 High-scoring environment. Power hitters and aggressive batting are key to winning. "
    elif avg_runs < 1.2:
        insight += "🎯 Bowling-friendly conditions. Teams should prioritize wicket preservation and strike rotation. "
    else:
        insight += "📊 Moderate scoring pattern. Balanced batting strategy works best. "

    # ---------------- WICKET BEHAVIOR ---------------- #
    if avg_wickets > 1.5:
        insight += "💥 Frequent wickets create volatility — middle-order depth becomes crucial. "
    else:
        insight += "🧱 Stable batting conditions — partnerships are the main success factor. "

    # ---------------- FINAL INTELLIGENCE LAYER ---------------- #
    if chase_win > 55 and avg_runs > 1.4:
        insight += "🚀 Ideal strategy: Chase aggressively with strong finishers."
    elif chase_win < 45 and avg_wickets > 1.5:
        insight += "🎯 Ideal strategy: Defend with attacking bowlers and early wickets."
    else:
        insight += "🧠 Adaptive strategy required based on match situation."

    return insight