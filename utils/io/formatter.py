import pandas as pd

name_formatter = lambda name: name.lower().replace(" ", "_")


def format_dataframe_column_names(data: pd.DataFrame) -> pd.DataFrame:
    columns: list = data.columns
    for column in columns:
        data.rename({column: name_formatter(column)}, inplace=True, axis=1)
    return data
