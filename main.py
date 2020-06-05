import re
import time
from typing import List, Dict

from bs4 import BeautifulSoup
import requests
import yaml

from lib import scryfall, deckbox
from models import Card
from service import cards as cards_service
from service.namedtuples import Deck


DECKS_FILE = "decks.yml"


def is_token_maker(card: Card) -> bool:
    return 'token' in card.oracle_text.lower()


def main():
    with open(DECKS_FILE, 'rb') as f:
        decks_yaml = yaml.safe_load(f)

    # Load decks from yaml file
    decks = [Deck(**deck_yaml) for deck_yaml in decks_yaml]
    deck = decks[-1]  ## TODO: Run on all decks instead of just one

    # Extract HTML from Deckbox, and parse out individual cards
    html_extract = deckbox.get_extract(deck.deck_id)
    card_names = deckbox.parse_cards(html_extract)[:5]

    cards = [cards_service.get_card(name) for name in card_names]

    print(cards)


if __name__ == '__main__':
    main()
