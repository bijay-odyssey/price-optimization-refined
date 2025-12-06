def price_gap(df):
    df["price_gap"] = df["unit_price"] - df["avg_comp_price"]
    return df

def price_ratio(df):
    df["price_ratio"] = df["unit_price"] / df["avg_comp_price"]
    return df
