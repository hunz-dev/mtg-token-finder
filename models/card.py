from peewee import CharField, UUIDField
from models.base import BaseModel


# TODO: Add inserted at time
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

    @property
    def is_token_maker(self):
        return 'token' in self.oracle_text.lower()
