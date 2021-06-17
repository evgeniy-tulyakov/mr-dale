from discord import Guild
from discord.ext import commands



class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)


    async def on_ready(self):
        host_guild: Guild = self.guilds[0]
        await host_guild.system_channel.send('@everyone Здравствуйте! ', tts=True)
