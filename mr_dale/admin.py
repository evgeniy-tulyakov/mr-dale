import logging

from discord.ext import commands



logger = logging.getLogger(__name__)


class Admin(commands.Cog):

    @commands.command(name='make_text_channel')
    @commands.guild_only()
    async def new_channel(self, ctx: commands.Context, channel_name: str):
        params = {
            'name': channel_name,
            'topic': 'default_text',
        }
        await ctx.guild.create_text_channel(**params)
        logger.debug(f'<{channel_name}> channel was created successfully')
        await ctx.send('ok')



def setup(bot_object):
    bot_object.add_cog(Admin())
    logger.info('<Admin> extension loaded successfully')
