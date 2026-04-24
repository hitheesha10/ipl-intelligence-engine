import pandas as pd

def load_data(path):
    df = pd.read_csv(path, index_col=0)

    # Fix types
    df['Date'] = pd.to_datetime(df['Date'])
    df['Match ID'] = df['Match ID'].astype(str)

    # Fill missing
    df['Method'].fillna('Not Out', inplace=True)
    df['Player Out'].fillna('None', inplace=True)
    df['Runs to Get'].fillna(0, inplace=True)

    return df