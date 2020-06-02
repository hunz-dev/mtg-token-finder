from collections import namedtuple
import re
import time
from typing import List

from bs4 import BeautifulSoup
import requests
import scrython
import yaml


DECKS_FILE = "decks.yml"
DECKBOX_URL = "https://deckbox.org/sets/{deck_id}/export"

Deck = namedtuple('Deck', ['name', 'deck_id'])


def get_deckbox_extract(deck_id: str) -> str:
    url = DECKBOX_URL.format(deck_id=deck_id)
    return requests.get(url).text


def parse_deckbox_cards(html_extract: str) -> List[str]:
    parsed_html = BeautifulSoup(html_extract, features="html.parser")
    deck_text = re.sub('Sideboard:', '', parsed_html.body.text)
    cards = re.split('\d+|\n', deck_text)
    return [card.strip() for card in cards if len(card.strip()) > 0]


def get_scryfall_cards(card_names: List[str], rate_limit=0.05) -> List[scrython.cards.cards_object.CardsObject]:
    def _get_card_rate_limited(card_name):
        time.sleep(rate_limit)
        return scrython.cards.Named(exact=card_name)

    return [_get_card_rate_limited(name) for name in card_names]


def is_token_maker(card: scrython.cards.cards_object.CardsObject) -> bool:
    return 'token' in card.oracle_text().lower()


def main():
    with open(DECKS_FILE, 'rb') as f:
        decks_yaml = yaml.safe_load(f)

    # Load decks from yaml file
    decks = [Deck(**deck_yaml) for deck_yaml in decks_yaml]
    deck = decks[-1]  ## TODO: Run on all decks instead of just one

    # Extract HTML from Deckbox, and parse out individual cards
    html_extract = get_deckbox_extract(deck.deck_id)
    card_names = parse_deckbox_cards(html_extract)[:5]

    cards = get_scryfall_cards(card_names)
    token_cards = [card for card in cards if is_token_maker(card)]


if __name__ == '__main__':
    main()
