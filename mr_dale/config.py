'''
Constants necessary for the correct execution of this bot.
here, most of the values of the environment variables are extracted.
'''

from os import getenv
from pathlib import Path



# Base settings
PROJECT_PATH = Path(__file__).resolve().parent
UI_RESOURCES_PATH = PROJECT_PATH / 'ui_resources'
BOT_TOKEN = getenv('mrdtoken')


EXTENSIONS_LIST = [
    'mr_dale.admin'
]


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
