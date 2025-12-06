from sklearn.model_selection import GridSearchCV

def tune_rf(model, X, y):
    params = {
        "n_estimators": [100, 200],
        "max_depth": [None, 10]
    }

    gs = GridSearchCV(
        model,
        params,
        cv=3,
        scoring="neg_mean_absolute_error"
    )

    gs.fit(X, y)
    return gs.best_estimator_
