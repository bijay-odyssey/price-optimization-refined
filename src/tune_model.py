from sklearn.model_selection import RandomizedSearchCV

def tune_model(model, X, y):
    params = {
        "n_estimators": [200, 400, 600],
        "max_depth": [8, 10, 12],
        "min_samples_leaf": [1, 5, 10]
    }

    rs = RandomizedSearchCV(
        model,
        params,
        n_iter=10,
        scoring="neg_mean_absolute_error",
        cv=3,
        n_jobs=-1,
        random_state=42
    )

    rs.fit(X, y)
    return rs.best_estimator_
