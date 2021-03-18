import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import asyncio
import os
import random
from discord import Embed

cluster = MongoClient("mongodb+srv://TD_Laptop:MoonS00n1342!@cluster0.6ojzu.mongodb.net/test")
db = cluster["GooseNeck"]
collection = db["User ID"]

client = commands.Bot(command_prefix = ".")
token = 'ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk'

@client.event
async def on_ready():
   print(f'{client.user} has connected on Discord')

@client.command(name = "whoami")
async def whoami(ctx):
    e = discord.Embed(description = (f"You are {ctx.message.author.name}"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# Says hello, used to see if bot is online
@client.command(name = "hello")
async def hello(ctx):
    e = discord.Embed(description = ("Howdy!"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# Help Command, will redirect user to site to see list of command
# Quick and easy guide to start 
@client.command(name = "hep")
async def hep(ctx):
    e = discord.Embed(description = ("This is the help command"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# In-Depth help command, used for full list of commands
@client.command(name = "hep_cmd")
async def hep_cmd(ctx):
    e = discord.Embed(description = ("In-Depth help"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# User can get to our site, for more info, invite to new server, etc
@client.command(name = "home")
async def home(ctx):
    e = discord.Embed(description = ("Will send user to home page site :D"), color = 0xa1ffb0)
    await ctx.send(embed = e)

@client.command(name = "info")
async def hep_cmd(ctx):
    e = discord.Embed(description = ("Display info about given card"), color = 0xa1ffb0)
    await ctx.send(embed = e)

@client.command(name="register")
async def on_message(ctx):
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.message}")
    myquery = { "_id": ctx.author.id }
    if (collection.count_documents(myquery) == 0):
        post = {"_id": ctx.author.id, "score": 1}
        collection.insert_one(post)
        await ctx.channel.send('Registered!')
    else:
        await ctx.channel.send('You Already registered, you silly goose!')

@client.command(name="roll")
async def roll(ctx):
    num = random.randint(1, 18)
    rarity = random.randint(1, 100)

    if num == 1:
        ff = discord.File("gooseneck-main/gamepics/Alpaca10.jpg", filename="Alpaca10.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "Alpaca 10", description = ('General Info \n Global ID: 1'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Alpaca10.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Alpaca 10", description = ('General Info \n Global ID: 1'), color = 0x72f26f)
            embed.set_image(url="attachment://Alpaca10.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Alpaca 10", description = ('General Info \n Global ID: 1'), color = 0x4441f2)
            embed.set_image(url="attachment://Alpaca10.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Alpaca 10", description = ('General Info \n Global ID: 1'), color = 0xed2f52)
            embed.set_image(url="attachment://Alpaca10.jpg")
        else:
            embed = discord.Embed(title = "Alpaca 10", description = ('General Info \n Global ID: 1'), color = 0xf7f41b)
            embed.set_image(url="attachment://Alpaca10.jpg")
        #post = {"_id": ctx.author.id, "card": "Alpaca 10"}
        #collection.insert_one(post)
    if num == 2:
        ff = discord.File("gooseneck-main/gamepics/Boruto.png", filename="Boruto.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Boruto", description = ('General Info \n Global ID: 2'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Boruto.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Boruto", description = ('General Info \n Global ID: 2'), color = 0x72f26f)
            embed.set_image(url="attachment://Boruto.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Boruto", description = ('General Info \n Global ID: 2'), color = 0x4441f2)
            embed.set_image(url="attachment://Boruto.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Boruto", description = ('General Info \n Global ID: 2'), color = 0xed2f52)
            embed.set_image(url="attachment://Boruto.png")
        else:
            embed = discord.Embed(title = "Boruto", description = ('General Info \n Global ID: 2'), color = 0xf7f41b)
            embed.set_image(url="attachment://Boruto.png")
        #post = {"_id": ctx.author.id, "card": "Boruto"}
        #collection.insert_one(post)
    if num == 3:
        ff = discord.File("gooseneck-main/gamepics/Conner.png", filename="Conner.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Conner", description = ('General Info \n Global ID: 3'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Conner.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Conner", description = ('General Info \n Global ID: 3'), color = 0x72f26f)
            embed.set_image(url="attachment://Conner.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Conner", description = ('General Info \n Global ID: 3'), color = 0x4441f2)
            embed.set_image(url="attachment://Conner.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Conner", description = ('General Info \n Global ID: 3'), color = 0xed2f52)
            embed.set_image(url="attachment://Conner.png")
        else:
            embed = discord.Embed(title = "Conner", description = ('General Info \n Global ID: 3'), color = 0xf7f41b)
            embed.set_image(url="attachment://Conner.png")
        #post = {"_id": ctx.author.id, "card": "Commer"}
        #collection.insert_one(post)
    if num == 4:
        ff = discord.File("gooseneck-main/gamepics/GooseNeck.jpg", filename="GooseNeck.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "GooseNeck", description = ('General Info \n Global ID: 4'), color = 0xc9c9c9)
            embed.set_image(url="attachment://GooseNeck.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "GooseNeck", description = ('General Info \n Global ID: 4'), color = 0x72f26f)
            embed.set_image(url="attachment://GooseNeck.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "GooseNeck", description = ('General Info \n Global ID: 4'), color = 0x4441f2)
            embed.set_image(url="attachment://GooseNeck.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "GooseNeck", description = ('General Info \n Global ID: 4'), color = 0xed2f52)
            embed.set_image(url="attachment://GooseNeck.jpg")
        else:
            embed = discord.Embed(title = "GooseNeck", description = ('General Info \n Global ID: 4'), color = 0xf7f41b)
            embed.set_image(url="attachment://GooseNeck.jpg")
        #post = {"_id": ctx.author.id, "card": "GooseNeck"}
        #collection.insert_one(post)
    if num == 5:
        ff = discord.File("gooseneck-main/gamepics/IcyBoo.png", filename="IcyBoo.png")
        if rarity <= 55:
            embed = discord.Embed(title = "IcyBoo", description = ('General Info \n Global ID: 5'), color = 0xc9c9c9)
            embed.set_image(url="attachment://IcyBoo.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "IcyBoo", description = ('General Info \n Global ID: 5'), color = 0x72f26f)
            embed.set_image(url="attachment://IcyBoo.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "IcyBoo", description = ('General Info \n Global ID: 5'), color = 0x4441f2)
            embed.set_image(url="attachment://IcyBoo.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "IcyBoo", description = ('General Info \n Global ID: 5'), color = 0xed2f52)
            embed.set_image(url="attachment://IcyBoo.png")
        else:
            embed = discord.Embed(title = "IcyBoo", description = ('General Info \n Global ID: 5'), color = 0xf7f41b)
            embed.set_image(url="attachment://IcyBoo.png")
        #post = {"_id": ctx.author.id, "card": "IcyBoo"}
        #collection.insert_one(post)
    if num == 6:
        ff = discord.File("gooseneck-main/gamepics/Isabelle.png", filename="Isabelle.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Isabelle", description = ('General Info \n Global ID: 6'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Isabelle.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Isabelle", description = ('General Info \n Global ID: 6'), color = 0x72f26f)
            embed.set_image(url="attachment://Isabelle.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Isabelle", description = ('General Info \n Global ID: 6'), color = 0x4441f2)
            embed.set_image(url="attachment://Isabelle.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Isabelle", description = ('General Info \n Global ID: 6'), color = 0xed2f52)
            embed.set_image(url="attachment://Isabelle.png")
        else:
            embed = discord.Embed(title = "Isabelle", description = ('General Info \n Global ID: 6'), color = 0xf7f41b)
            embed.set_image(url="attachment://Isabelle.png")
        #post = {"_id": ctx.author.id, "card": "Isabelle"}
        #collection.insert_one(post)
    if num == 7:
        ff = discord.File("gooseneck-main/gamepics/Joker.jpg", filename="Joker.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "Joker", description = ('General Info \n Global ID: 7'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Joker.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Joker", description = ('General Info \n Global ID: 7'), color = 0x72f26f)
            embed.set_image(url="attachment://Joker.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Joker", description = ('General Info \n Global ID: 7'), color = 0x4441f2)
            embed.set_image(url="attachment://Joker.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Joker", description = ('General Info \n Global ID: 7'), color = 0xed2f52)
            embed.set_image(url="attachment://Joker.jpg")
        else:
            embed = discord.Embed(title = "Joker", description = ('General Info \n Global ID: 7'), color = 0xf7f41b)
            embed.set_image(url="attachment://Joker.jpg")
        #post = {"_id": ctx.author.id, "card": "Joker"}
        #collection.insert_one(post)
    if num == 8:
        ff = discord.File("gooseneck-main/gamepics/Kratos.jpg", filename="Kratos.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "Kratos", description = ('General Info \n Global ID: 8'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Kratos.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Kratos", description = ('General Info \n Global ID: 8'), color = 0x72f26f)
            embed.set_image(url="attachment://Kratos.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Kratos", description = ('General Info \n Global ID: 8'), color = 0x4441f2)
            embed.set_image(url="attachment://Kratos.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Kratos", description = ('General Info \n Global ID: 8'), color = 0xed2f52)
            embed.set_image(url="attachment://Kratos.jpg")
        else:
            embed = discord.Embed(title = "Kratos", description = ('General Info \n Global ID: 8'), color = 0xf7f41b)
            embed.set_image(url="attachment://Kratos.jpg")
        # post = {"_id": ctx.author.id, "card": "Kratos"}
        # collection.insert_one(post)
    if num == 9:
        ff = discord.File("gooseneck-main/gamepics/Nezuko.png", filename="Nezuko.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Nezuko", description = ('General Info \n Global ID: 9'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Nezuko.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Nezuko", description = ('General Info \n Global ID: 9'), color = 0x72f26f)
            embed.set_image(url="attachment://Nezuko.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Nezuko", description = ('General Info \n Global ID: 9'), color = 0x4441f2)
            embed.set_image(url="attachment://Nezuko.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Nezuko", description = ('General Info \n Global ID: 9'), color = 0xed2f52)
            embed.set_image(url="attachment://Nezuko.png")
        else:
            embed = discord.Embed(title = "Nezuko", description = ('General Info \n Global ID: 9'), color = 0xf7f41b)
            embed.set_image(url="attachment://Nezuko.png")
        #post = {"_id": ctx.author.id, "card": "Nezuko"}
        #collection.insert_one(post)
    if num == 10:
        ff = discord.File("gooseneck-main/gamepics/Nomad.png", filename="Nomad.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Nomad", description = ('General Info \n Global ID: 10'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Nomad.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Nomad", description = ('General Info \n Global ID: 10'), color = 0x72f26f)
            embed.set_image(url="attachment://Nomad.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Nomad", description = ('General Info \n Global ID: 10'), color = 0x4441f2)
            embed.set_image(url="attachment://Nomad.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Nomad", description = ('General Info \n Global ID: 10'), color = 0xed2f52)
            embed.set_image(url="attachment://Nomad.png")
        else:
            embed = discord.Embed(title = "Nomad", description = ('General Info \n Global ID: 10'), color = 0xf7f41b)
            embed.set_image(url="attachment://Nomad.png")
        #post = {"_id": ctx.author.id, "card": "Nomad"}
        #collection.insert_one(post)
    if num == 11:
        ff = discord.File("gooseneck-main/gamepics/PacMan.png", filename="PacMan.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Pac Man", description = ('General Info \n Global ID: 11'), color = 0xc9c9c9)
            embed.set_image(url="attachment://PacMan.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Pac Man", description = ('General Info \n Global ID: 11'), color = 0x72f26f)
            embed.set_image(url="attachment://PacMan.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Pac Man", description = ('General Info \n Global ID: 11'), color = 0x4441f2)
            embed.set_image(url="attachment://PacMan.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Pac Man", description = ('General Info \n Global ID: 11'), color = 0xed2f52)
            embed.set_image(url="attachment://PacMan.png")
        else:
            embed = discord.Embed(title = "Pac Man", description = ('General Info \n Global ID: 11'), color = 0xf7f41b)
            embed.set_image(url="attachment://PacMan.png")
        #post = {"_id": ctx.author.id, "card": "Pac Man"}
        #collection.insert_one(post)
    if num == 12:
        ff = discord.File("gooseneck-main/gamepics/Plootle.jpg", filename="Plootle.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "Plootle", description = ('General Info \n Global ID: 12'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Plootle.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Plootle", description = ('General Info \n Global ID: 12'), color = 0x72f26f)
            embed.set_image(url="attachment://Plootle.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Plootle", description = ('General Info \n Global ID: 12'), color = 0x4441f2)
            embed.set_image(url="attachment://Plootle.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Plootle", description = ('General Info \n Global ID: 12'), color = 0xed2f52)
            embed.set_image(url="attachment://Plootle.jpg")
        else:
            embed = discord.Embed(title = "Plootle", description = ('General Info \n Global ID: 12'), color = 0xf7f41b)
            embed.set_image(url="attachment://Plootle.jpg")
        #post = {"_id": ctx.author.id, "card": "Plootle"}
        #collection.insert_one(post)
    if num == 13:
        ff = discord.File("gooseneck-main/gamepics/Sage.png", filename="Sage.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Sage", description = ('General Info \n Global ID: 13'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Sage.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Sage", description = ('General Info \n Global ID: 13'), color = 0x72f26f)
            embed.set_image(url="attachment://Sage.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Sage", description = ('General Info \n Global ID: 13'), color = 0x4441f2)
            embed.set_image(url="attachment://Sage.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Sage", description = ('General Info \n Global ID: 13'), color = 0xed2f52)
            embed.set_image(url="attachment://Sage.png")
        else:
            embed = discord.Embed(title = "Sage", description = ('General Info \n Global ID: 13'), color = 0xf7f41b)
            embed.set_image(url="attachment://Sage.png")
        #post = {"_id": ctx.author.id, "card": "Sage"}
        #collection.insert_one(post)
    if num == 14:
        ff = discord.File("gooseneck-main/gamepics/Snorlax.png", filename="Snorlax.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Snorlax", description = ('General Info \n Global ID: 14'), color = 0xc9c9c9)
            embed.set_image(url="attachment://Snorlax.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Snorlax", description = ('General Info \n Global ID: 14'), color = 0x72f26f)
            embed.set_image(url="attachment://Snorlax.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Snorlax", description = ('General Info \n Global ID: 14'), color = 0x4441f2)
            embed.set_image(url="attachment://Snorlax.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Snorlax", description = ('General Info \n Global ID: 14'), color = 0xed2f52)
            embed.set_image(url="attachment://Snorlax.png")
        else:
            embed = discord.Embed(title = "Snorlax", description = ('General Info \n Global ID: 14'), color = 0xf7f41b)
            embed.set_image(url="attachment://Snorlax.png")
        #post = {"_id": ctx.author.id, "card": "Snorlax"}
        #collection.insert_one(post)
    if num == 15:
        ff = discord.File("gooseneck-main/gamepics/SpaceBoi.png", filename="SpaceBoi.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Space Boi", description = ('General Info \n Global ID: 15'), color = 0xc9c9c9)
            embed.set_image(url="attachment://SpaceBoi.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Space Boi", description = ('General Info \n Global ID: 15'), color = 0x72f26f)
            embed.set_image(url="attachment://SpaceBoi.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Space Boi", description = ('General Info \n Global ID: 15'), color = 0x4441f2)
            embed.set_image(url="attachment://SpaceBoi.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Space Boi", description = ('General Info \n Global ID: 15'), color = 0xed2f52)
            embed.set_image(url="attachment://SpaceBoi.png")
        else:
            embed = discord.Embed(title = "Space Boi", description = ('General Info \n Global ID: 15'), color = 0xf7f41b)
            embed.set_image(url="attachment://SpaceBoi.png")
        #post = {"_id": ctx.author.id, "card": "SpaceBoi"}
        #collection.insert_one(post)
    if num == 16:
        ff = discord.File("gooseneck-main/gamepics/TomNook.jpg", filename="TomNook.jpg")
        if rarity <= 55:
            embed = discord.Embed(title = "Tom Nook", description = ('General Info \n Global ID: 16'), color = 0xc9c9c9)
            embed.set_image(url="attachment://TomNook.jpg")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Tom Nook", description = ('General Info \n Global ID: 16'), color = 0x72f26f)
            embed.set_image(url="attachment://TomNook.jpg")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Tom Nook", description = ('General Info \n Global ID: 16'), color = 0x4441f2)
            embed.set_image(url="attachment://TomNook.jpg")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Tom Nook", description = ('General Info \n Global ID: 16'), color = 0xed2f52)
            embed.set_image(url="attachment://TomNook.jpg")
        else:
            embed = discord.Embed(title = "Tom Nook", description = ('General Info \n Global ID: 16'), color = 0xf7f41b)
            embed.set_image(url="attachment://TomNook.jpg")
        #post = {"_id": ctx.author.id, "card": "Tom Nook"}
        #collection.insert_one(post)
    if num == 17:
        ff = discord.File("gooseneck-main/gamepics/YumStar.png", filename="YumStar.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Yum Star", description = ('General Info \n Global ID: 17'), color = 0xc9c9c9)
            embed.set_image(url="attachment://YumStar.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Yum Star", description = ('General Info \n Global ID: 17'), color = 0x72f26f)
            embed.set_image(url="attachment://YumStar.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Yum Star", description = ('General Info \n Global ID: 17'), color = 0x4441f2)
            embed.set_image(url="attachment://YumStar.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Yum Star", description = ('General Info \n Global ID: 17'), color = 0xed2f52)
            embed.set_image(url="attachment://YumStar.png")
        else:
            embed = discord.Embed(title = "Yum Star", description = ('General Info \n Global ID: 17'), color = 0xf7f41b)
            embed.set_image(url="attachment://YumStar.png")
        #post = {"_id": ctx.author.id, "card": "Yum Star"}
        #collection.insert_one(post)
    if num == 18:
        ff = discord.File("gooseneck-main/gamepics/ZSS.png", filename="ZSS.png")
        if rarity <= 55:
            embed = discord.Embed(title = "Zero Suit Samus", description = ('General Info \n Global ID: 18'), color = 0xc9c9c9)
            embed.set_image(url="attachment://ZSS.png")
        elif rarity > 55 and rarity <= 75:
            embed = discord.Embed(title = "Zero Suit Samus", description = ('General Info \n Global ID: 18'), color = 0x72f26f)
            embed.set_image(url="attachment://ZSS.png")
        elif rarity > 75 and rarity <= 90:
            embed = discord.Embed(title = "Zero Suit Samus", description = ('General Info \n Global ID: 18'), color = 0x4441f2)
            embed.set_image(url="attachment://ZSS.png")
        elif rarity > 90 and rarity <= 97:
            embed = discord.Embed(title = "Zero Suit Samus", description = ('General Info \n Global ID: 18'), color = 0xed2f52)
            embed.set_image(url="attachment://ZSS.png")
        else:
            embed = discord.Embed(title = "Zero Suit Samus", description = ('General Info \n Global ID: 18'), color = 0xf7f41b)
            embed.set_image(url="attachment://ZSS.png")
        #post = {"_id": ctx.author.id, "card": "Zero Suit Samus"}
        #collection.insert_one(post)
    await ctx.channel.send(file = ff, embed = embed)

client.run(token)