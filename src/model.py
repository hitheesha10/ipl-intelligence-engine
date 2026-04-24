from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

FEATURE_COLS = ['Runs to Get', 'Balls Remaining', 'Innings Wickets']

def train_model(df):

    # Use only second innings (chasing scenario)
    df_model = df[df['Innings'] == 2].copy()

    # Drop rows where target is missing
    df_model = df_model.dropna(subset=['Chased Successfully'])

    # Features & target
    X = df_model[FEATURE_COLS]
    y = df_model['Chased Successfully']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(X_test, y_test)

    return model, accuracy