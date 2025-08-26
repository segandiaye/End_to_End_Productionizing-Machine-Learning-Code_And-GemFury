"""
Command Line
"""

import click
from wqp import __version__
from loguru import logger

@click.group(name='wqp', help='A command line tool to train a wine quality predictor')
@click.version_option(__version__)
def wqp():
    logger.info("You called my name wqp ?")
    pass