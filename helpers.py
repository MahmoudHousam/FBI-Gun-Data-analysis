import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


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
    layout = go.Layout(title=title, barmode="stack")
    fig = go.Figure(data, layout)
    return fig.show(renderer="svg", width=1200, height=500)


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


def to_period(
    df, col, new_col_name, period={"d", "m", "y"}, new_col_state=False, strtype=False
):
    """a function that takes a number of parameters
    and return a new dataframe with new columns converted
    to periods of time; day, month, year or convert the columns
    itself to periods.

    Args:
        df (pd.DataFrame): dataframe
        col (DataFrame.Series): column in dataframe
        new_col_name ([string]): string object in case a new column created
        period (dict, optional): [periods of time to convert to].
        Defaults to {'d', 'm', 'y'}.
        new_col_state (bool, optional): [in case of a new column, it should
        be True and new_col_name is required]. Defaults to False.
        strtype (bool, optional): [in case of converting the time period
        to string, it should be True]. Defaults to False.

    Returns:
        [pd.DataFrame]: [pd.DataFrame]
    """
    if new_col_state is False & strtype is False:
        df[col] = df[col].dt.to_period(period)
    elif new_col_state is False & strtype is True:
        df[col] = df[col].dt.to_period(period).astype(str)
    elif new_col_state is True & strtype is False:
        df[new_col_name] = df[col].dt.to_period(period)
    elif new_col_state is True & strtype is True:
        df[new_col_name] = df[col].dt.to_period(period).astype(str)
    return df