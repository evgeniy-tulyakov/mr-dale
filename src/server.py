from mr_dale.bot import Bot
from mr_dale.config import BOT_TOKEN



def start():
    bot_instance = Bot(command_prefix='$$', case_insensitive=True)
    try:
        bot_instance.loop.run_until_complete(bot_instance.start(BOT_TOKEN))
    except KeyboardInterrupt:
        bot_instance.loop.run_until_complete(bot_instance.close())
