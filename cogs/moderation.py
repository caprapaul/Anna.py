import discord
from discord.ext import commands


class Moderation:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="delete", aliases=["del"])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def delete_messages(self, ctx, amount: int=1):
        """Delete an amount of messages"""
        await ctx.message.delete()
        await ctx.message.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages", delete_after=3)


def setup(bot):
    bot.add_cog(Moderation(bot))
