import discord
from discord.ext import commands
import asyncio
import os
import random
from discord import Embed
from datetime import datetime
import psycopg2

conn = psycopg2.connect(user = "iwjahdoeduzhpw",
                        password = "61fe7582e319e7889d9571cf574b5f17687504226bbdb3dc89265468f34c5cdc",
                        host = "ec2-54-161-239-198.compute-1.amazonaws.com",
                        port = "5432",
                        database = "d2f6if7qo4eukk",
                        sslmode='require')
crsr = conn.cursor()
print(conn.get_dsn_parameters(),"\n")
print("Database Connected")

client = commands.Bot(command_prefix = ".")
token = 'ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk'

@client.event
async def on_ready():
   print(f'{client.user} has connected on Discord')

@client.command(name = "whoami")
async def whoami(ctx):
    e = discord.Embed(description = (f"You are {ctx.message.author}"), color = 0xa1ffb0)
    await ctx.send(embed = e)

@client.command(name = "fuck")
async def fuck(ctx):
    e = discord.Embed(description = ("Bend over, you silly goose!"), color = 0xa1ffb0)
    await ctx.send(embed = e)

@client.command(name = "insert")
async def insert(ctx):
    e = discord.Embed(description = ("You like that, you silly goose!"), color = 0xa1ffb0)
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
"""
@client.command(name = "play")
async def play(ctx, url : str, channel : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name =channel)
    voice = discord.utils.get(client.voice_clients, guild =ctx.guild)
    await voiceChannel.connect()
"""
# User can get to our site, for more info, invite to new server, etc
@client.command(name = "home")
async def home(ctx):
    e = discord.Embed(description = ("Will send user to home page site :D"), color = 0xa1ffb0)
    await ctx.send(embed = e)
    
@client.command(name = "inv")
async def inventory(ctx, rarity):
    userid = ctx.author.id
    username = str(ctx.author)
    user = ""
    for character in username:
        if character.isalnum():
            user += character
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    check = crsr.fetchall()
    if not check:
        await ctx.send("You have not registered yet")
    else:
        if rarity == "all":
            crsr.execute("SELECT * FROM " + user + " ORDER BY cardrarity;")
            inv = str(crsr.fetchall())
            await ctx.send(inv)
        elif rarity == "Rare" or rarity == "Super Rare" or rarity == " Super Super Rare" or rarity == "Ultra Rare" or rarity == "Common":
            crsr.execute("SELECT cardname, cardrarity FROM " + user + " WHERE cardrarity = '" + rarity + "';")
            inv = str(crsr.fetchall())
            await ctx.send(inv)
        else:
            e = discord.Embed(description = ("Requires second argument, use all to see all cards, plase use one of the following to see the following rarities : Common, Rare, Super Rare, Super Super Rare, Ultra Rare"), color = 0xa1ffb0)
            await ctx.send(embed = e)
 
@client.command(name = "register")
async def on_message(ctx):
    userid = ctx.author.id
    username = str(ctx.author)
    user = ""
    for character in username:
        if character.isalnum():
            user += character
    createtable= "CREATE TABLE IF NOT EXISTS " + user + """ (
        cardname varchar(255),
        cardrarity varchar (255)
    );
    """
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    data = crsr.fetchall()

    if not data:
        crsr.execute("INSERT INTO userinfo (userid,username) VALUES(%s,%s);",[userid,username])
        conn.commit()
        crsr.execute(createtable)
        conn.commit()
        await ctx.send("You are now registered you silly goose.")
        
    else:
        await ctx.send("You already registered, you silly goose")

@client.command(name = "roll")
async def roll(ctx):
    userid = ctx.author.id
    #if ctx.author.id == 279083868894658561:
    #    await ctx.send("no more albert")
    #    return
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    data = crsr.fetchall()

    if not data:
        await ctx.send("You need to register first, you silly goose")
        return
    
    num = random.randint(1, 19)
    rarity = random.randint(1, 100)
    username = str(ctx.author)
    user = ""
    for character in username:
        if character.isalnum():
            user += character
            
    insert = "INSERT INTO "+ user + "(cardname, cardrarity) VALUES (%s, %s);"

    owner = str(ctx.message.author.name)
    name = ["Alpaca 10", "Boruto", "Conner", "GooseNeck", "IcyBoo", "Isabelle", "Joker", "Kratos", "Nezuko", "Nomad", "Pac Man", "Plootle", "Sage", "Snorlax", "Space Boi", "Tom Nook", "Yum Star", "Zero Suit Samus"]
    #rarity
    cardRarity = ["**[C]** ~ Common", "**[R]** ~ Rare", "**[SR]** ~ Super Rare", "**[SSR]** ~ Super Super Rare", "**[UR]** ~ Ultra Rare"]
    cardRarityVis = ["**☆**", "**☆☆**", "**☆☆☆**", "**☆☆☆☆**", "**☆☆☆☆☆**"]
    if rarity <= 55:
        rank = cardRarity[0] + '\n' + cardRarityVis[0]
        cardColor = 0xc9c9c9
        rare = "Common"
    elif rarity > 55 and rarity <= 75:
        rank = cardRarity[1] + '\n' + cardRarityVis[1]
        cardColor = 0x72f26f
        rare = "Rare"
    elif rarity > 75 and rarity <= 90:
        rank = cardRarity[2] + '\n' + cardRarityVis[2]
        cardColor = 0x4441f2
        rare = "Super Rare"
    elif rarity > 90 and rarity <= 97:
        rank = cardRarity[3] + '\n' + cardRarityVis[3]
        cardColor = 0xed2f52
        rare = "Super Super Rare"
    else:
        rank = cardRarity[4] + '\n' + cardRarityVis[4]
        cardColor = 0xf7f41b
        rare = "Ultra Rare"
    #sql stuff
    #time
    currentTime = datetime.now()
    month = currentTime.strftime("%m")
    day = currentTime.strftime("%d")
    year = currentTime.strftime("%Y")
    date = '**Date Rolled:** ' + month + '/' + day + '/' + year

    cardLayout = '**General Info** \n **Global ID:** ' + str(num) + '\n **Original Owner:** ' + owner + '\n' + date + '\n\n' + '**Rarity:** ' + rank

    cardquery = "SELECT url FROM images WHERE globalid = %s;"
    crsr.execute(cardquery,[num])
    cardurl = str(crsr.fetchone())
    print(cardurl)
    modurl = cardurl.replace(',','')
    modurl = modurl.replace('(','')
    modurl = modurl.replace(')','')
    modurl = modurl.replace("'",'')
    print(modurl)
    if not cardurl:
        await ctx.channel.send("Card does not exsist")
        return
    else:
        embed = discord.Embed(title = name[num-1], description = cardLayout, color = cardColor)
        embed.set_image(url=modurl)
        crsr.execute(insert,(name[num-1], rare))
        conn.commit()
        await ctx.channel.send(embed = embed)

client.run(token)
