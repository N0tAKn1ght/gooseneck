import random
import discord
import asyncio
import os
from discord.ext import commands

client = commands.Bot(command_prefix = ".")
token = 'ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk'



@client.command(pass_context = True)
async def randomNumber(ctx):
    embed = discord.Embed(title = "card check", description = (random.randint(1, 18)), color = 0xa1ffb0)
    await ctx.send(embed = embed)

bot.run(token)
