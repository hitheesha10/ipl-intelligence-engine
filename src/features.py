import numpy as np

def create_features(df):

    df = df.copy()  # ✅ avoid chained issues

    # ---------------- BASIC FEATURES ---------------- #
    df['Year'] = df['Date'].dt.year

    df['is_six'] = (df['Batter Runs'] == 6).astype(int)

    df['is_dot_ball'] = (
        (df['Runs From Ball'] == 0) &
        (df['Extra Runs'] == 0) &
        (df['Valid Ball'] == 1)
    ).astype(int)

    # ---------------- PHASE (VECTORIZED - FASTER) ---------------- #
    df['Phase'] = np.select(
    [
        df['Over'] <= 6,
        (df['Over'] > 6) & (df['Over'] <= 15),
        df['Over'] > 15
    ],
    ['Powerplay', 'Middle', 'Death'],
    default='Unknown'   # ✅ FIX
)
    # ---------------- PRESSURE INDEX (SAFE) ---------------- #
    df['Balls Remaining'] = df['Balls Remaining'].replace(0, 1)

    df['pressure_index'] = df['Runs to Get'] / df['Balls Remaining']

    # Clip extreme values (realistic range)
    df['pressure_index'] = df['pressure_index'].clip(0, 10)
    df['run_rate_required'] = df['Runs to Get'] / df['Balls Remaining'] * 6

    return df