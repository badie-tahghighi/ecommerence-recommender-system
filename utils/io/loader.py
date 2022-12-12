import os

import pandas as pd


def load(file_type: str, file_name: str):
    path_to_file = os.getcwd() + '/assets/' + file_type + '/' + file_name
    data = pd.read_csv(path_to_file)
    return data
