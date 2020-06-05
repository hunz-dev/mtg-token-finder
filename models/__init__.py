from peewee import SqliteDatabase

database = SqliteDatabase('scryfall.db')

# Models have to be imported after DB init
from .card import Card
