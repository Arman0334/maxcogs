import discord
import logging
from random import choice
from redbot.core import commands

from .constants import POKEMON

log = logging.getLogger("red.maxcogs.pokenamegen")


class PokeNameGen(commands.Cog):
    """Get random pokémon names."""

    __author__ = "MAX"
    __version__ = "0.0.1"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    def __init__(self, bot):
        self.bot = bot

    # I cannot tell you how bored i was when i made this cog...
    # It's mostly just meant for people who like pokémon for the most.
    # Pokémon names are from the global national dex: https://pokemondb.net/pokedex/national.

    @commands.command(aliases=["pokeng"])
    @commands.bot_has_permissions(embed_links=True)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def pokenamegen(self, ctx):
        """Get random pokémon names."""
        emb = discord.Embed(
            title="Here's a random pokémon name:",
            description=choice(POKEMON),
            colour=await ctx.embed_color(),
        )
        try:
            await ctx.reply(embed=emb, mention_author=True)
        except discord.HTTPException:
            await ctx.send(embed=emb)
            log.info(
                "Command 'pokenamegen' failed to use reply due to message was unknown."
            )