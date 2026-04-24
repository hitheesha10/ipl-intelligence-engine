from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

FEATURE_COLS = ['Runs to Get', 'Balls Remaining', 'Innings Wickets']

def train_model(df):

    # Use only chase data
    df_chase = df[df['Innings'] == 2].copy()

    # Drop missing safely
    df_chase = df_chase.dropna(subset=FEATURE_COLS + ['Chased Successfully'])

    # ✅ Ensure DataFrame (not numpy)
    X = df_chase[FEATURE_COLS]
    y = df_chase['Chased Successfully']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy