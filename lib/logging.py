import logging


FORMAT_STR = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get(name='token-finder', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(FORMAT_STR)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
