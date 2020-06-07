import requests
from lib.wrappers import rate_limit
from lib import logging


SCRYFALL_URL = "https://api.scryfall.com/{path}"
log = logging.get(name='scryfall')


@rate_limit(delay=0.1)
def get_card_exact(card_name):
    url = SCRYFALL_URL.format(path="cards/named")
    log.debug("Looking up card [%s] on Scryfall", card_name)
    params = dict(exact=card_name)
    response = requests.get(url, params)
    return response.json()
