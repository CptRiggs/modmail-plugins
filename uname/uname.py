import discord
import os
from discord.ext import commands

class Uname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uname(self, ctx):
        """A buggy implimentation of uname from GNU Coreutils."""
        command = "uname -a 2>&1"
        stream = os.popen(command)
        output = stream.read()
        await ctx.send(output)

async def setup(bot):
    await bot.add_cog(Uname(bot))
