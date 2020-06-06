from typing import Dict
from lib import scryfall, logging
from models import Card


log = logging.get(name='card_service')


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
    try:
        card = Card.get(Card.name == card_name)
    except Card.DoesNotExist:
        log.debug('Card not found, searching Scryfall')
        card_json = scryfall.get_card_exact(card_name)
        card = create_card(card_json)

    return card
