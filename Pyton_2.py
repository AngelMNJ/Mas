import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command('meme')
async def mem(ctx):
    with open('Imagenes/memes/meme_1.jpg', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTEwMTIwNTk4MDE1NjUzMDcxOQ.GmogrC.Uht6uDRMc_bXqJX3X2Y6BWs8RKvU9LmVwmP9BQ")