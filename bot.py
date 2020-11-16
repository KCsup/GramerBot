import discord
import os
import json
import random
import glob
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix='!', case_insensitive=True)
file = open('token.json')
data = json.load(file)

fpath = os.getcwd()
isDir = os.path.isdir(fpath + '\Logs')

muted: bool

if isDir:
    print('epic')
elif not isDir:
    os.mkdir(fpath + '\Logs')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Your Mom!'))
    print('GramerBot is ready.')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 357966938301005825:
        client.unload_extension(f'cogs.{extension}')
    elif ctx.author.id != 357966938301005825:
        await ctx.send('You cannot unload cogs! You must be KCsup to do this!')
        print(format(ctx.author.name) + ' tried to unload a cog.')


@client.command()
async def reload(ctx: commands.Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(data['token'])
file.close()
