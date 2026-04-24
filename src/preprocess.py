import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Fix missing values (NO chained assignment)
    df['Method'] = df['Method'].fillna('Not Out')
    df['Player Out'] = df['Player Out'].fillna('None')
    df['Runs to Get'] = df['Runs to Get'].fillna(0)
    df['Balls Remaining'] = df['Balls Remaining'].fillna(0)

    # Ensure numeric columns are correct
    numeric_cols = [
        'Runs to Get',
        'Balls Remaining',
        'Innings Wickets',
        'Runs From Ball',
        'Batter Runs',
        'Extra Runs'
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Drop rows with critical missing values
    df = df.dropna(subset=['Match ID', 'Over', 'Ball'])

    return df