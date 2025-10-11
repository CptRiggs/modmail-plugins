import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_map = {}

    @commands.Cog.listener()
    async def on_message_delete(message):
        if message in self.message_map:
            await self.message_map[message].delete()


    @commands.command()
    async def say(self, ctx, *, message):
        """Say plugin that doesn't delete the original message!"""
        bot_message = await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
        self.message_map[message.id] = bot_message

async def setup(bot):
    await bot.add_cog(Say(bot))
