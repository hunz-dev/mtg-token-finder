import yaml

from lib import deckbox, logging
from service import cards as cards_service
from service.namedtuples import Deck


DECKS_FILE = "decks.yml"
OUTPUT_FILE = "out/tokens.xlsx"

log = logging.get('token-lookup')


def check_deck(deck: Deck):
    # Extract HTML from Deckbox, and parse out individual cards
    html_extract = deckbox.get_extract(deck.deck_id)
    card_names = deckbox.parse_cards(html_extract)

    # Get all Card objects and determine which ones have tokens
    cards = [cards_service.get_card(name) for name in card_names]
    token_cards = [c for c in cards if c and c.token_type is not None]

    # Write results to an Excel workbook
    log.info("Writing results for [%s] to [%s]", deck.name, OUTPUT_FILE)
    cards_service.write_to_workbook(deck.name, token_cards, OUTPUT_FILE)


def main():
    with open(DECKS_FILE, 'rb') as f:
        decks_yaml = yaml.safe_load(f)

    # Load decks from yaml file
    decks = [Deck(**deck_yaml) for deck_yaml in decks_yaml]
    [check_deck(deck) for deck in decks]


if __name__ == '__main__':
    main()
