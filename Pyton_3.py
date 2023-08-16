import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_fox():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data["image"]

@bot.command('duck')
async def duck(ctx):
     image_url = get_duck_image_url()
     await ctx.send(image_url)
@bot.command('fox')
async def duck(ctx):
     image_url = get_fox()
     await ctx.send(image_url)


@bot.command('meme')
async def mem(ctx):
    img_name = random.choice(os.listdir('imagenes'))
    with open(f'imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTEwMTIwNTk4MDE1NjUzMDcxOQ.GmogrC.Uht6uDRMc_bXqJX3X2Y6BWs8RKvU9LmVwmP9BQ")