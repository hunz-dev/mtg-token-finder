import re
from typing import List
from bs4 import BeautifulSoup
import requests


DECKBOX_URL = "https://deckbox.org/sets/{deck_id}/export"


def get_extract(deck_id: str) -> str:
    url = DECKBOX_URL.format(deck_id=deck_id)
    return requests.get(url).text


def parse_cards(html_extract: str) -> List[str]:
    parsed_html = BeautifulSoup(html_extract, features="html.parser")
    deck_text = re.sub('Sideboard:', '', parsed_html.body.text)
    cards = re.split(r"\d+|\n", deck_text)
    return [card.strip() for card in cards if len(card.strip()) > 0]
