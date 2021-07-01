from os import getenv
from pathlib import Path

from dotenv import load_dotenv



# Base settings
PROJECT_PATH = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_PATH / '.env')
BOT_TOKEN = getenv('mrdtoken')


# Configuring the logging mechanism
LOG_FORMAT = {
    'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
}

LOGGING_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'default': LOG_FORMAT},
    'handlers': {
        'info_console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'error_console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'stream': 'ext://sys.stderr'
        }
    },
    'loggers': {
        'mr_dale': {
            'level': 'INFO',
            'handlers': ['info_console_handler', 'error_console_handler'],
            'propagate': False
        },
        'discord': {
            'level': 'ERROR',
            'handlers': ['error_console_handler'],
            'propagate': False
        }
    }
}
