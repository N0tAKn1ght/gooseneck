import random
import discord
import asyncio
import os
from discord.ext import commands
from discord import Embed


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
    embed =Embed(title = "Alpaca 10", description = "Alpaca image", image = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nbcnews.com%2Ftechnolog%2Fno-googling-says-google-unless-you-really-mean-it-1C9078566&psig=AOvVaw1dSpXwfXbmmWsQLqHbhw7c&ust=1615058177166000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPiVndnume8CFQAAAAAdAAAAABAD', color = 0xa1ffb0)
    file = discord.File("games_pics/Alpaca10.jpg", filename="Alpaca")
    await ctx.send(embed=embed)
client.run(token)
