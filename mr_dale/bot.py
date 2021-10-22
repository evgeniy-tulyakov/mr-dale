import json
import logging
from typing import Optional

from discord import Guild, TextChannel
from discord.ext import commands

from . import config, utilites



logger = logging.getLogger(__name__)


class Bot(commands.Bot):
    '''
    implements a custom class for the bot object
    '''

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)
        self.host_guild: Optional[Guild] = None
        with open(config.UI_RESOURCES_PATH / 'startup.json', 'rb') as f:
            self.ui_messages = json.load(f)


    async def on_ready(self):
        logger.info(f'Logged in as: {self.user.name} {self.user.id}')
        self.host_guild = self.guilds[0]
        expected_channel = utilites.find_channel_by_name(self.host_guild.text_channels, 'dialog')
        if expected_channel is None:
            await self.host_guild.system_channel.send(self.ui_messages['first_run_msg'], tts=True)
            bot_channel: TextChannel = await self.host_guild.create_text_channel(
                'dialog', topic=self.ui_messages['bot_channel']['topic']
            )
            await bot_channel.send(self.ui_messages['bot_channel']['first_msg'])
        else:
            await self.host_guild.system_channel.send(self.ui_messages['relode_msg'], tts=True)


    def run(self, token):
        logger.info('starting mr_dale')
        super().run(token, reconnect=True)
