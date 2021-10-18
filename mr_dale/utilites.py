from typing import Optional, Sequence

from discord.abc import GuildChannel



def find_channel_by_name(
    channels: Sequence[GuildChannel], channel_name: str
) -> Optional[GuildChannel]:
    predicate = lambda item: item.name == channel_name
    for channel in channels:
        if predicate(channel):
            return channel
