import discord
from discord.ext import commands, tasks
import json
import asyncio

with open('config.json') as config_file:
    config = json.load(config_file)

token = config['token']
channel = int(config['channel'])

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@tasks.loop(minutes=int(config['minutes']))
async def ping():
    a = bot.get_channel(channel)
    if a:
        message = await a.send('@everyone')
        await asyncio.sleep(0.5)
        await message.delete()
        print(f'pinged in {channel}')

@bot.event
async def on_ready():
    ping.start()

bot.run(token)

# made by @gradiscopy. 
