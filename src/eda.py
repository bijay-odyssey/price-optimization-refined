import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_eda(df):
    summary = df.describe(include="all")
    missing = df.isnull().sum()

    return summary, missing


def plot_distributions(df):
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        plt.figure(figsize=(4, 3))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        plt.show()
