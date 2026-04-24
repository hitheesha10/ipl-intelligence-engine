import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year

    df['Batter'] = df['Batter'].str.strip().str.title()
    df['Bowler'] = df['Bowler'].str.strip().str.title()

    df.fillna({
        'Method': 'Not Out',
        'Runs to Get': 0
    }, inplace=True)

    return df