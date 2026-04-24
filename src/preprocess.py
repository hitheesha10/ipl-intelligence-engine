import pandas as pd

def load_data(path):
    df = pd.read_csv(path, index_col=0)

    # Convert types
    df['Date'] = pd.to_datetime(df['Date'])
    df['Match ID'] = df['Match ID'].astype(str)

    # ✅ FIXED (NO inplace)
    df['Method'] = df['Method'].fillna('Not Out')
    df['Player Out'] = df['Player Out'].fillna('None')
    df['Runs to Get'] = df['Runs to Get'].fillna(0)

    return df