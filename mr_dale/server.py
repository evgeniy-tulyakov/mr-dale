'''
Main module of this App.
'''

from discord import Intents
from logging.config import dictConfig

from .bot import Bot
from .config import BOT_TOKEN, LOGGING_SETTINGS



def start():
    '''
    Performs initialization and launch of the bot
    '''
    dictConfig(LOGGING_SETTINGS)
    intents_object = Intents.all()
    bot_instance = Bot(command_prefix='$$', case_insensitive=True, intents=intents_object)
    try:
        bot_instance.loop.run_until_complete(bot_instance.start(BOT_TOKEN))
    except KeyboardInterrupt:
        bot_instance.loop.run_until_complete(bot_instance.close())
