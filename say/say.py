import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_map = {}

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.id in self.message_map:
            content = after.content.split()
            message = self.message_map[before.id]
            # there is probably a better way to do this..... i just don't bother with it now
            if f"say" in content[0].lower():
                bot_message = await message.edit(content=' '.join(content[1:]))
                self.message_map[before.id] = bot_message
            else:
                await message.delete()
                self.message_map.pop(before.id)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.id in self.message_map:
            await self.message_map[message.id].delete()
            self.message_map.pop(message.id)


    @commands.command()
    async def say(self, ctx, *, message):
        """Say plugin that doesn't delete the original message!"""
        bot_message = await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))
        self.message_map[ctx.message.id] = bot_message

async def setup(bot):
    await bot.add_cog(Say(bot))
