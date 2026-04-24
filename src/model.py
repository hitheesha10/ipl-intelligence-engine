from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df):

    df_chase = df[df['Innings'] == 2].copy()

    X = df_chase[['Runs to Get', 'Balls Remaining', 'Innings Wickets']]
    y = df_chase['Chased Successfully']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy