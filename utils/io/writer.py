import os

import pandas as pd


def write(file_type: str, file_name: str, data: pd.DataFrame):
    path_to_file = os.getcwd() + '/assets/' + file_type + '/' + file_name
    data.to_csv(path_to_file, index=False)
