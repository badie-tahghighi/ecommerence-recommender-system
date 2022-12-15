from datetime import timezone
import datetime

import pandas as pd
from faker import Faker

from utils.io.writer import write

faker = Faker()


def generate_users(rows_count: int = 10000, write_to_file: bool = False) -> pd.DataFrame:
    genders = ['male', 'female']
    marriage_status = ['single', 'married']
    result: pd.DataFrame = pd.DataFrame()
    for index in range(rows_count):
        name = faker.name()
        gender = faker.word(1, genders)
        age = faker.random_int(10, 100)
        date_joined = datetime.datetime.fromisoformat(faker.iso8601())
        utc_time = date_joined.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        marriage = faker.word(1, marriage_status)
        balance = faker.random_int(0, 100000)
        id = faker.md5()
        country = faker.country()
        result = pd.concat([result, pd.DataFrame({
            'id': id,
            'name': name,
            'gender': gender,
            'age': age,
            'date_joined': utc_timestamp,
            'marriage_status': marriage,
            'balance': balance,
            'country': country,
        }, index=[0])])
    if write_to_file:
        write('csv', 'users_dataset.csv', result)
    return result


def generate_interactions(user_ids: list, target_ids: list, rows_count: int = 10000,
                          write_to_file: bool = False) -> pd.DataFrame:
    result: pd.DataFrame = pd.DataFrame()
    interaction_types = ['comment', 'liked', 'bought', 'added_to_wish_list', 'followed', 'opened', 'shared',
                         'revisited']

    for index in range(rows_count * len(interaction_types)):
        user_id = faker.word(1, user_ids)
        interaction_type = faker.word(1, interaction_types)
        time = datetime.datetime.fromisoformat(faker.iso8601())
        utc_time = time.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        target_id = faker.word(1, target_ids)
        result = pd.concat([result, pd.DataFrame({
            'user_id': user_id,
            'interaction_type': interaction_type,
            'target_id': target_id,
            'time': utc_timestamp,
        }, index=[0])])
    if write_to_file:
        write('csv', 'interactions_dataset.csv', result)
    return result


def generate_reviews(reviews: pd.DataFrame, user_ids: list, target_ids: list,
                     write_to_file: bool = False) -> pd.DataFrame:
    result = pd.DataFrame()
    for index, row in reviews.iterrows():
        user_id = faker.word(1, user_ids)
        target_id = faker.word(1, target_ids)
        text = row['Review Text']
        time = datetime.datetime.fromisoformat(faker.iso8601())
        utc_time = time.replace(tzinfo=timezone.utc)
        utc_timestamp = utc_time.timestamp()
        rate = row['Rating']
        result = pd.concat([result, pd.DataFrame({
            'user_id': user_id,
            'target_id': target_id,
            'text': text,
            'rate': rate,
            'time': utc_timestamp,
        }, index=[0])])
    if write_to_file:
        write('csv', 'reviews_dataset.csv', result)
    return result
