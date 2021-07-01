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
        host_guild: Guild = self.guilds[0]
        ch: Optional[TextChannel] = find(
            lambda item: item.name == 'dialog', host_guild.text_channels
        )

        if ch is None:
            await host_guild.system_channel.send('@everyone Здравствуйте! ', tts=True)
            await host_guild.create_text_channel('dialog', topic='Диалог с ботом')
        else:

            await host_guild.system_channel.send('@everyone снова увиделись! ', tts=True)
