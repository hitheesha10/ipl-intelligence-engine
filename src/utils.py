def generate_insight(df):

    chase_win = df['Chased Successfully'].mean() * 100

    if chase_win > 55:
        return "Chasing gives teams a strategic advantage."
    else:
        return "Defending totals remains the stronger strategy."