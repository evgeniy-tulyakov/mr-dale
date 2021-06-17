import os
from pathlib import Path

from dotenv import load_dotenv
from mr_dale.bot import Bot



def start():
    dotenv_path = Path(__file__).resolve().parent.parent / '.env'
    print(dotenv_path)
    load_dotenv(dotenv_path)
    token = os.getenv('mrdtoken')
    bot_instance = Bot(command_prefix='$$', case_insensitive=True)
    try:
        bot_instance.loop.run_until_complete(bot_instance.start(token))
    except KeyboardInterrupt:
        bot_instance.loop.run_until_complete(bot_instance.close())
