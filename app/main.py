from settings import *
from utils.data.fake_generator import *
from utils.io.loader import load


def main():
    initialize_settings()
    data = load('csv', 'preprocessed_shoes.csv', write_to_file=False)
    rows_count = data.shape[0]
    # users = load('csv', 'users_dataset.csv', write_to_file=False)
    # interactions = load('csv', 'interactions_dataset.csv', write_to_file=False)
    raw_reviews = load('csv', 'raw_reviews_dataset.csv', write_to_file=False)
    # reviews = load('csv', 'reviews_dataset.csv', write_to_file=False)
    users = generate_users(rows_count, True)
    generate_interactions(users['id'], data['asin'], rows_count, True)
    generate_reviews(raw_reviews, users['id'], data['asin'], True)


if __name__ == "__main__":
    main()
