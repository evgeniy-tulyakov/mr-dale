import logging

from discord import Guild
from discord.ext import commands



logger = logging.getLogger(__name__)


class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)


    async def on_ready(self):
        logger.info(f'Logged in as: {self.user.name} {self.user.id}')
        host_guild: Guild = self.guilds[0]
        await host_guild.system_channel.send('@everyone Здравствуйте! ', tts=True)
