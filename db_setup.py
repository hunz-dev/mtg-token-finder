from models import database, Card


if __name__ == '__main__':
    with database:
        database.create_tables([Card])
