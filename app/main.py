from settings import *
from utils.data.fake_generator import *
from utils.io.loader import load


def main():
    initialize_settings()
    data = load('csv', 'shoes_dataset.csv', write_to_file=False)
    rows_count = data.shape[0]
    users = load('csv', 'users_dataset.csv', write_to_file=False)
    interactions = load('csv', 'interactions_dataset.csv', write_to_file=False)
    raw_reviews = load('csv', 'raw_reviews_dataset.csv', write_to_file=False)
    reviews = generate_reviews(reviews=raw_reviews, user_ids=users['id'].values, target_ids=data['asin'].values,
                               write_to_file=True)
    print(reviews)


if __name__ == "__main__":
    main()
