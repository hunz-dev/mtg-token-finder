import re
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
    def token_type(self):
        expression = r"([\d]+\/[\d]+.*?creature\stoken)\s?(with\s[a-z]+)?"
        matches = re.finditer(expression, self.oracle_text)
        tokens = ', '.join([match.group(0) for match in matches])
        return tokens if len(tokens) > 0 else None
