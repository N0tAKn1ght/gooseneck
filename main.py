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

@client.command(pass_context = True)
async def ping(ctx) :
    embed = discord.Embed(title = "card check", description = (f":ping_pong: Pong with {str(round(client.latency, 2))}")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def whoami(ctx):
    embed = discord.Embed(title = "card check", description = (f"You are {ctx.message.author.name}")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# Says hello, used to see if bot is online
@client.command(pass_context = True)
async def hello(ctx):
    embed = discord.Embed(title = "card check", description = ("Howdy!")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# Help Command, will redirect user to site to see list of command
# Quick and easy guide to start 
@client.command(pass_context = True)
async def hep(ctx):
    embed = discord.Embed(title = "card check", description = ("This is the help command")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# In-Depth help command, used for full list of commands
@client.command(pass_context = True)
async def hep_cmd(ctx):
    embed = discord.Embed(title = "card check", description = ("In-Depth help")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# User can get to our site, for more info, invite to new server, etc
@client.command(pass_context = True)
async def home(ctx):
    embed = discord.Embed(title = "card check", description = ("Will send user to home page site :D")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# Will initiate user to base, give a preset amount of resources to get started with the game
@client.command(pass_context = True)
async def start(ctx):
    embed = discord.Embed(title = "card check", description = ("Initiate game")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# Will perform functions (To be imported later), to give user a card and decide rarity
@client.command(pass_context = True)
async def roll(ctx):
    embed = discord.Embed(title = "card check", description = ("Will run 2 random functions, deciding card and rarity they obtain")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

# Given a card ID, will display information about card
# i.e. Name of Card, date obtained, rarity, etc
@client.command(pass_context = True)
async def info(ctx):
    embed = discord.Embed(title = "card check", description = ("Display info about given card")), color = 0xa1ffb0)
    await ctx.send(embed = embed)

@client.command(pass_context = True)
async def randomNumber(ctx):
    embed = discord.Embed(title = "card check", description = (random.randint(1, 18)), color = 0xa1ffb0)
    await ctx.send(embed = embed)



@client.command(pass_context = True)
async def image(ctx):
    embed = discord.Embed(title = "alpaca 10", file = discord.File('13868967033_82c85fbc18_c(1).jpg'), color = 0xa1ffb0)
    await ctx.send(embed = embed)

client.run(token)
