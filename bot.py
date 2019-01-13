import discord
import asyncio
from discord.ext import commands
import helpers

#import random

# Global
TOKEN = 'NTI2MDgxMTI5ODgzODkzODAw.Dv__IQ.Rb-777SzlAKO4ultW8scd6n-JrY'
client = commands.Bot(command_prefix = 'Anna, ')
client.remove_command('help')

# <------ Events ------>
@client.event
async def on_ready ():
    print ("Bot is ready.")

@client.event 
async def on_message(message):
    output = f'{message.author} says: {message.content}'
    print (output)
    await client.process_commands(message)

# <------ Commands ------>
@client.command()
async def ping():
    await client.say('Pong!')


@client.command()
async def say(*args):
    output = ''

    for word in args:
        output += word
        output += ' '
    
    await client.say(output)


@client.command()
async def hug(*args):
    output = f'*Hugs {args[0]} warmly*'
    await client.say(output)


@client.command(pass_context = True) # Passes in context of the command
async def delete(ctx, amount = 100):

        messages = []
        channel = ctx.message.channel

        async for message in client.logs_from(channel, limit = int(amount)):
            messages.append(message)

        await client.delete_messages(messages)
        await client.say('Done.')

@client.command(pass_context = True)
async def remind(ctx, *args): # Format: Anna, remind me in -timer- -extension- to -message-
    
    message = ''
    for word in args[5:] :
        message += word
        message += ' '

    extension = args[3]
    print(extension)
    
    try:
        unscaledTime = int(args[2])
    except:
        await client.say("Sorry, I didn't understand when you wanted to be reminded.")
        return
    
    scaledTime = helpers.getScaledTime(extension, unscaledTime)
    
    if scaledTime > 604800:
        output = "Sorry, I can't set a reminder longer than 1 week."
    else:
        await client.say(f'Noted!')
        await asyncio.sleep(scaledTime)
        output = f'Hey, {ctx.message.author.mention}, you asked me to remind you to {message}'
    
    await client.say(output)

@client.command()
async def thanks():
    await client.say('No problem, glad I could help! 👍')

@client.command()
async def help():
    await client.say('Hi! My name is Anna. I am a bot under development by Acey#4962. You can access my commands by typing in "Anna, " followed by your command. See you around!')

@client.command()
async def disconnect():
    print('Exit command received. Ending process.')
    client.logout()
    exit()

client.run(TOKEN)
