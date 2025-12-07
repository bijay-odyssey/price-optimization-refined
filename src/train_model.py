from sklearn.metrics import mean_absolute_error

def train_model(X_train, y_train, X_val, y_val):
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=10,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_val)

    return model, mean_absolute_error(y_val, preds)
