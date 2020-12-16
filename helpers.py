import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def explore_nans(df, title):
    """a function that takes a dataframe and inspect the Null vs
    Not-null values to visualize a groupped bar chart that will help take
    decisions to deal with missing data.

    Args:
        df: pandas dataframe
        title: (string): x label title

    Returns:
        bar chart: Null vs Not-null values
    """
    df_null = df.isnull().sum()
    df_not_null = df.notnull().sum()
    labels = df.columns.tolist()
    null_values = df.isnull().sum().values.tolist()
    not_null_values = df.notnull().sum().values.tolist()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.barh(labels, null_values, label="Null")
    ax.barh(labels, not_null_values, label="Not Null", color="green")
    plt.xlabel(title, fontsize=20)
    ax.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt.show()