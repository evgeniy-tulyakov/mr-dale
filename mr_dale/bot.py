import json
import logging
from typing import Optional

from discord import Guild, TextChannel
from discord.ext import commands
from discord.utils import find



logger = logging.getLogger(__name__)


class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)


    async def on_ready(self):
        logger.info(f'Logged in as: {self.user.name} {self.user.id}')
        with open('mr_dale/ui_resources/startup.json', 'rb') as f:
            ui_messages = json.load(f)
        host_guild: Guild = self.guilds[0]
        expected_bot_channel: Optional[TextChannel] = find(
            lambda item: item.name == 'dialog', host_guild.text_channels
        )
        if expected_bot_channel is None:
            await host_guild.system_channel.send(content=ui_messages['first_run_msg'], tts=True)
            bot_channel: TextChannel = await host_guild.create_text_channel(
                'dialog', topic=ui_messages['bot_channel']['topic']
            )
            await bot_channel.send(content=ui_messages['bot_channel']['first_msg'])
        else:
            await host_guild.system_channel.send(ui_messages['relode_msg'], tts=True)
