def add_price_features(df):
    df = df.copy()

    df["price_gap"] = df["unit_price"] - df["avg_comp_price"]
    df["price_ratio"] = df["unit_price"] / (df["avg_comp_price"] + 1e-6)
    df["log_price"] = np.log1p(df["unit_price"])

    return df
