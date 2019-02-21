import discord
from discord.ext import commands
import asyncio
import helpers


class Misc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Check the ping"""
        await ctx.send('Pong! {0}'.format(round(self.bot.latency, 1)))

    @commands.command()
    async def say(self, ctx, message: str):
        """Say something"""
        await ctx.send(message)

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        """Hug someone"""
        output = f'*Hugs {user.display_name} warmly*'
        await ctx.send(output)

    @commands.command(name="remind")
    async def remind(self, ctx, *args):
        """Format: Anna, remind me in -timer- -extension- to -message-"""
        message = ''
        for word in args[5:]:
            message += word
            message += ' '

        extension = args[3]
        print(extension)

        try:
            unscaled_time = int(args[2])
        except:
            await ctx.send("Sorry, I didn't understand when you wanted to be reminded.")
            return

        scaled_time = helpers.getScaledTime(extension, unscaled_time)

        if scaled_time > 604800:
            output = "Sorry, I can't set a reminder longer than 1 week."
        else:
            await ctx.send(f'Noted!')
            await asyncio.sleep(scaled_time)
            output = f'Hey, {ctx.message.author.mention}, you asked me to remind you to {message}'

        await ctx.send(output)

    @commands.command()
    async def thanks(self, ctx):
        """Thank Anna"""
        await ctx.send('No problem, glad I could help! 👍')


def setup(bot):
    bot.add_cog(Misc(bot))
