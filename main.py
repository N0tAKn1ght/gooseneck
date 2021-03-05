import random
import discord
import asyncio
import os
from discord.ext import commands


client = commands.Bot(command_prefix = ".")
token = 'ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk'

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f":ping_pong: Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

# Says hello, used to see if bot is online
@client.command(name="hello")
async def hello(ctx) :
    await ctx.send("Howdy!")

# Help Command, will redirect user to site to see list of command
# Quick and easy guide to start 
@client.command(name="hep")
async def hep(ctx) :
    await ctx.send("This is the help command")

# In-Depth help command, used for full list of commands
@client.command(name="hep_cmd")
async def hep_cmd(ctx) :
    await ctx.send("In-Depth help")

# User can get to our site, for more info, invite to new server, etc
@client.command(name="home")
async def home(ctx) :
    await ctx.send("Will send user to home page site :D")

# Will initiate user to base, give a preset amount of resources to get started with the game
@client.command(name="start")
async def start(ctx) :
    await ctx.send("Initiate game")

# Will perform functions (To be imported later), to give user a card and decide rarity
@client.command(name="roll")
async def roll(ctx) :
    await ctx.send("Will run 2 random functions, deciding card and rarity they obtain")

# Given a card ID, will display information about card
# i.e. Name of Card, date obtained, rarity, etc
@client.command(name="info")
async def hep_cmd(ctx) :
    await ctx.send("Display info about given card")

@client.command(pass_context = True)
async def image(ctx):
    embed = discord.Embed(title = "Alpaca 10", description = "Alpaca image", color = 0xa1ffb0)
    embed.set_footer(text="Alpaca")
    embed.set_image(file = discord.File('game_pics/Alpaca_10.jpg')
    await ctx.send(embed = embed)

client.run(token)
