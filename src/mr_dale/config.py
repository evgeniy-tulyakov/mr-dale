from os import getenv
from pathlib import Path

from dotenv import load_dotenv



# Base settings
PROJECT_PATH = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_PATH / '.env')
BOT_TOKEN = getenv('mrdtoken')
