'''
Main module of this App.
'''

from logging import getLogger
from logging.config import dictConfig
import sys

from discord import Intents

from .bot import Bot
from .config import BOT_TOKEN, LOGGING_SETTINGS



def start():
    '''
    Performs initialization and launch of the bot
    '''
    dictConfig(LOGGING_SETTINGS)
    logger = getLogger(__name__)

    if BOT_TOKEN is None:
        logger.critical('the access token for mr_dale was not configured!')
        sys.exit(1)

    intents_object = Intents.all()
    bot_instance = Bot(command_prefix='$$', case_insensitive=True, intents=intents_object)
    bot_instance.run(BOT_TOKEN)
