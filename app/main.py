from settings import *
from utils.io.loader import load


def main():
    initialize_settings()
    load('json', 'amazon_uk_shoes_dataset.json', write_to_file=False)


if __name__ == "__main__":
    main()
