import logging
from pathlib import Path
from pprint import pformat
import sys
from typing import Union

LOG_FORMAT = "%(levelname)-5s | %(asctime)s | %(module)s:%(lineno)-3s | %(message)s"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


def get_logger(name: str, level: Union[str, int] = logging.DEBUG) -> logging.Logger:
    """
    Sets up standardised logging formats and output. To be imported and used on a per-module basis

    :param name: preferably the inbuilt python dunder variable __name__
    :param level: logging module level, either string e.g. "DEBUG" or corresponding int e.g. 10
    :return: ready to use logger object with standardised formatting and outputs
    """
    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)

    logger.setLevel(level)
    logger.addHandler(stream_handler)
    return logger


def show_location(here: Path) -> None:
    for path in here.parent.iterdir():
        print(path, "\n", pformat([p for p in path.iterdir() if "__" not in p.stem]))
