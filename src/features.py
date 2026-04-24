import numpy as np

def create_features(df):

    df['Year'] = df['Date'].dt.year

    df['is_six'] = (df['Batter Runs'] == 6).astype(int)

    df['is_dot_ball'] = (
        (df['Runs From Ball'] == 0) &
        (df['Extra Runs'] == 0) &
        (df['Valid Ball'] == 1)
    ).astype(int)

    # Phase classification
    def get_phase(over):
        if over <= 6:
            return 'Powerplay'
        elif over <= 15:
            return 'Middle'
        else:
            return 'Death'

    df['Phase'] = df['Over'].apply(get_phase)

    # Pressure index
    df['pressure_index'] = (
        df['Runs to Get'] / (df['Balls Remaining'] + 1)
    )

    return df