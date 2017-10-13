# -*- coding: utf-8 -*-

import click
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')

ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

@click.group()
def manager():
    """Management script for ad-operation-api"""


if __name__ == '__main__':
    manager()
