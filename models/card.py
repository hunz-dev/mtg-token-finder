from peewee import \
    CharField, DateField, DateTimeField, IntegerField, UUIDField
from models.base import BaseModel


class Card(BaseModel):
    id = UUIDField(primary_key=True)
    oracle_id = UUIDField(unique=True)
    name = CharField()
    released_at = CharField()
    mana_cost = CharField()
    type_line = CharField()
    oracle_text = CharField()
    set = CharField()
    artist = CharField()
