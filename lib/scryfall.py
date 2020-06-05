import requests
from .wrappers import rate_limit


SCRYFALL_URL = "https://api.scryfall.com/{path}"


@rate_limit(delay=0.1)
def get_card_exact(card_name):
    url = SCRYFALL_URL.format(path="cards/named")
    params = dict(exact=card_name)
    response = requests.get(url, params)
    return response.json()
