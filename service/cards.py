from typing import Dict
from lib import scryfall
from models import Card


def create_card(card_json: Dict) -> Card:
    return Card.create(
        id=card_json['id'],
        oracle_id=card_json['oracle_id'],
        name=card_json['name'],
        released_at=card_json['released_at'],
        mana_cost=card_json['mana_cost'],
        type_line=card_json['type_line'],
        oracle_text=card_json['oracle_text'],
        set=card_json['set'],
        artist=card_json['artist'],
    )


# TODO: debug logs if we have to fetch from Scryfall
def get_card(card_name: str) -> Card:
    card = Card.get(Card.name == card_name)

    if card is None:
        card_json = scryfall.get_exact_name(card_name)
        card = create_card(card_json)
    
    return card
