import pandas as pd
import numpy as np
import plotly.graph_objects as go


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
    null_values = df_null.values.tolist()
    not_null_values = df_not_null.values.tolist()
    data = [
        go.Bar(
            name="Not Null",
            x=not_null_values,
            y=labels,
            orientation="h",
            marker=dict(
                color="rgb(128,128,128)",
            ),
        ),
        go.Bar(
            name="Null",
            x=null_values,
            y=labels,
            orientation="h",
            marker=dict(
                color="rgb(192,192,192)",
            ),
        ),
    ]
    layout = go.Layout(title=title, barmode="stack", width=1200, height=500)
    fig = go.Figure(data, layout)
    return fig.show()


def drop_60_missings(df):
    """a function that takes a
    dataframe and return new dataframe with columns dropped that have more
    that 60% null values and so on we cannot take any decision about.

    Args:
        df: pandas dataframe

    Returns:
        df: new dataframe
    """
    for col in df.columns:
        if df[col].isnull().sum() / len(df) * 100 >= 60:
            df.drop(columns=[col], inplace=True)
    return df