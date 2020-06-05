from peewee import \
    CharField, DateField, DateTimeField, IntegerField, UUIDField
from models.base import BaseModel


class Card(BaseModel):
    id = UUIDField(primary_key=True)
    oracle_id = UUIDField(unique=True)
    name = CharField()
    released_at = CharField()
    image_url = CharField()
    mana_cost = CharField()
    type_line = CharField()
    oracle_text = CharField()
    colors = CharField()
    set_code = CharField()
    artist = CharField()
