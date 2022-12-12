import os

import pandas as pd

from utils.io.formatter import format_dataframe_column_names
from utils.io.json_to_csv import json_to_csv
from utils.io.writer import write


def load(file_type: str, file_name: str, write_to_file: bool = False):
    path_to_file = os.getcwd() + '/assets/' + file_type + '/' + file_name
    data = pd.read_csv(path_to_file)
    if write_to_file:
        csv_data = json_to_csv(data)
        csv_data = format_dataframe_column_names(csv_data)
        write('csv', 'shoes_dataset.csv', csv_data)
    return data
