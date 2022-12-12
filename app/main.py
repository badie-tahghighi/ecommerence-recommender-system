from settings import *
from utils.io.loader import load


def main():
    initialize_settings()
    load('csv', 'shoes_dataset.csv')


if __name__ == "__main__":
    main()
