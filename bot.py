import discord
from discord.ext import commands

# Global
DESCRIPTION = "Hi! My name is Anna. I am a bot under development by Acey#4962. You can access my commands by typing in \"Anna, \" followed by your command. See you around!"
TOKEN = "NDE4ODYzMTMyNzQ4OTM5Mjg0.D1ABgw.ox70mtL0m7BFL9cP2kUgRELG3BM"

bot = commands.Bot(command_prefix=commands.when_mentioned_or("Anna,"), description=DESCRIPTION)

# this specifies what extensions to load when the bot starts up
startup_extensions = ["cogs.misc",
                      "cogs.moderation"]

# <------ Events ------>
@bot.event
async def on_ready ():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    output = f'{message.author} says: {message.content}'
    print(output)
    await bot.process_commands(message)

# <------ Commands ------>
@bot.command()
@commands.is_owner()
async def disconnect():
    """Disconnect"""
    print('Exit command received. Ending process.')
    await bot.logout()
    exit()


@bot.command()
@commands.is_owner()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


@bot.command()
@commands.is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)
