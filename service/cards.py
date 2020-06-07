from typing import Dict
import peewee
from lib import scryfall, logging
from models import Card


log = logging.get(name='card_service')


def create_card(card_json: Dict) -> Card:
    params = dict()
    for field in Card._meta.fields.keys():
        params[field] = card_json.get(field, None)

    try:
        card = Card.create(**params)
    except peewee.DatabaseError as e:
        log.warning("Unable to create card with the following params:")
        log.warning(params)
        log.warning(e)
        return None

    log.info("Created card [%s]", card.name)

    return card


def get_card(card_name: str) -> Card:
    try:
        card = Card.get(Card.name == card_name)
    except Card.DoesNotExist:
        log.debug('Card not found, searching Scryfall')
        card_json = scryfall.get_card_exact(card_name)
        card = create_card(card_json)

    return card
