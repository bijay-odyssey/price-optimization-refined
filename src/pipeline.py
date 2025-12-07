from sklearn.pipeline import Pipeline

def build_pipeline(preprocessor, model):
    return Pipeline(
        steps=[
            ("features", FunctionTransformer(add_price_features)),
            ("prep", preprocessor),
            ("model", model)
        ]
    )
