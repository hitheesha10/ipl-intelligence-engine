def generate_insight(df):

    chase_win = df['Chased Successfully'].mean() * 100

    if chase_win > 55:
        return "Chasing is the dominant winning strategy."
    elif chase_win < 45:
        return "Defending totals is more effective."
    else:
        return "Balanced competition between chasing and defending."