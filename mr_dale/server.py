'''
Main module of this App.
'''

from logging.config import dictConfig

from .bot import Bot
from .config import BOT_TOKEN, LOGGING_SETTINGS



def start():
    '''
    Performs initialization and launch of the bot
    '''
    dictConfig(LOGGING_SETTINGS)
    bot_instance = Bot(command_prefix='$$', case_insensitive=True)
    try:
        bot_instance.loop.run_until_complete(bot_instance.start(BOT_TOKEN))
    except KeyboardInterrupt:
        bot_instance.loop.run_until_complete(bot_instance.close())
