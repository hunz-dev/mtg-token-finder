from peewee import SqliteDatabase, Model


database = SqliteDatabase('scryfall.db')


# Create a base-class all models will inherit
class BaseModel(Model):
    class Meta:
        database = database
