import discord
from discord.ext import commands
import asyncio
import os
import random
from discord import Embed
from datetime import datetime
import psycopg2
import json
import requests

# postgres connection method
conn = psycopg2.connect(user = "qpeynpgjkccpxh",
                        password = "f96f5d86cf1892bac455d2d0f1ea6fd71970ffbd8637a37e384150f4a74fa839",
                        host = "ec2-54-167-152-185.compute-1.amazonaws.com",
                        port = "5432",
                        database = "d4a3mdi3t849lu",
                        sslmode='require')
crsr = conn.cursor()
print(conn.get_dsn_parameters(),"\n")
print("Database Connected")

# the prefix for commands
client = commands.Bot(command_prefix = ".")

# token to connect discord api
token = 'ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk'

def mon(userid):
    crsr.execute("SELECT coins FROM userinfo where userid = %s;",[userid])
    money = crsr.fetchone()
    if(money[0] == 0):
        return 0 
    else:
        coin = money[0] - 1
        crsr.execute("UPDATE userinfo SET coins = '%s' WHERE userid = '%s';",[coin, userid])
        return 1

def remove(thing):
    thing = thing.replace(',','')
    thing = thing.replace('(','')
    thing = thing.replace(')','')
    thing = thing.replace("'",'')
    return thing

def setrarity(rarity):
    cardRarity = ["**[C]** ~ Common", "**[R]** ~ Rare", "**[SR]** ~ Super Rare", "**[UR]** ~ Ultra Rare", "**[L]** ~ Legendary"]
    cardRarityVis = ["**☆**", "**☆☆**", "**☆☆☆**", "**☆☆☆☆**", "**☆☆☆☆☆**"]
    arr = []
    if rarity <= 55:
        rank = cardRarity[0] + '\n' + cardRarityVis[0]
        arr.append(rank)
        cardColor = 0xc9c9c9
        arr.append(cardColor)
        rare = "Common"
        arr.append(rare)
    elif rarity > 55 and rarity <= 75:
        rank = cardRarity[1] + '\n' + cardRarityVis[1]
        arr.append(rank)
        cardColor = 0x72f26f
        arr.append(cardColor)
        rare = "Rare"
        arr.append(rare)
    elif rarity > 75 and rarity <= 90:
        rank = cardRarity[2] + '\n' + cardRarityVis[2]
        arr.append(rank)
        cardColor = 0x4441f2
        arr.append(cardColor)
        rare = "Super_Rare"
        arr.append(rare)
    elif rarity > 90 and rarity <= 97:
        rank = cardRarity[3] + '\n' + cardRarityVis[3]
        arr.append(rank)
        cardColor = 0xed2f52
        arr.append(cardColor)
        rare = "Ultra_Rare"
        arr.append(rare)
    else:
        rank = cardRarity[4] + '\n' + cardRarityVis[4]
        arr.append(rank)
        cardColor = 0xf7f41b
        arr.append(cardColor)
        rare = "Legendary"
        arr.append(rare)
    return arr

def color(rarity):
    if rarity == "Common":
        cardColor = 0xc9c9c9
        return cardColor
    elif rarity == "Rare":
        cardColor = 0x72f26f
        return cardColor
    elif rarity == "Super_Rare":
        cardColor = 0x4441f2
        return cardColor
    elif rarity == "Ultra_Rare":
        cardColor = 0xed2f52
        return cardColor
    elif rarity == "Legendary":
        cardColor = 0xf7f41b
        return cardColor

def time():
    arr = []
    currentTime = datetime.now()
    month = currentTime.strftime("%m")
    day = currentTime.strftime("%d")
    year = currentTime.strftime("%Y")
    date = month + '/' + day + '/' + year
    form = year + month + day
    arr.append(currentTime)
    arr.append(date)
    arr.append(form)
    return arr

def url(user,num):
    cardquery = "SELECT url FROM images WHERE globalid = %s;"
    crsr.execute(cardquery,[num])
    cardurl = str(crsr.fetchone())
    modurl = cardurl.replace(',','')
    modurl = modurl.replace('(','')
    modurl = modurl.replace(')','')
    modurl = modurl.replace("'",'')
    return modurl

def list_string(thing):
    strings = ""
    for i in thing:
        strings += i
    return strings

# console to show connection status
@client.event
async def on_ready():
   print(f'{client.user} has connected on Discord')

# Says hello, used to see if bot is online
@client.command(name = "hello")
async def hello(ctx):
    e = discord.Embed(description = ("Howdy!"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# Gives you a random quote from zenquotes
@client.command(name = "quote")
async def quote(ctx):
    owner = str(ctx.message.author.name)
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    e = discord.Embed(title = "***Some Inspiration ~***", description = quote, color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
    await ctx.send(embed = e)

@client.command(name = "tothemoon")
async def tothemoon(ctx):
    owner = str(ctx.message.author.name)
    response = requests.get("https://sochain.com//api/v2/get_price/DOGE/USD")
    json_data = json.loads(response.text)
    price = "The price of doge is: " + json_data['data']['prices'][0]['price']
    e = discord.Embed(title = "***To the Moon ~***", description = price, color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
    await ctx.send(embed = e)
    
# shows how many coins you have
@client.command(name = "coin")
async def coin(ctx):
    owner = str(ctx.message.author.name)
    userid = ctx.author.id
    crsr.execute("SELECT coins FROM userinfo where userid = %s;",[userid])
    money = crsr.fetchone()
    smoney = str(money[0])
    e = discord.Embed(title = "Currency", description = "You currently have " + smoney + " coins! " + "<:DABLOON:810940045468499988>", color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=e)

# claims 5 coins with a current cooldown of 10 seconds
@client.command(name = "claim")
@commands.cooldown(1, 10, commands.BucketType.user)
async def claim(ctx):
    owner = str(ctx.message.author.name)
    userid = ctx.author.id
    crsr.execute("SELECT coins FROM userinfo where userid = %s;",[userid])
    money = crsr.fetchone()
    coin = money[0] + 5
    crsr.execute("UPDATE userinfo SET coins = '%s' WHERE userid = '%s';",[coin, userid])
    conn.commit()
    scoin = str(coin)
    e = discord.Embed(title = "Currency", description = "you now have " + scoin + " coins! " + "<:DABLOON:810940045468499988>", color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
    await ctx.send(embed=e)

# sends an error message/cooldown message
@claim.error
async def claim_cooldown(ctx, error):
    owner = str(ctx.message.author.name)
    if isinstance(error, commands.CommandOnCooldown):
        e = discord.Embed(title = "Cooldown", description = f"You can claim your coins in {error.retry_after:.2f}s.", color = 0xa1ffb0)
        e.set_author(name = owner, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=e)

# In-Depth help command, used for full list of commands
@client.command(name = "hep_cmd")
async def hep_cmd(ctx):
    owner = str(ctx.message.author.name)
    bl = "\n \n"
    dis = ("`.register`" + " - Set up to start playing" + bl + "`.coin`" + " - Checks your currency"
     + bl + "`.claim`" + " - Adds Coins to your account" + bl + "`.roll`" + " - Uses coins to obtain cards"
     + bl + "`.inv`" + " - Check card inventory" + bl +  "`.view`" + " - Checks a card using its unique ID"
     + bl + "`.hep`" + " - breif explaination of GooseNeck Bot" + bl + "`.hep_cmd`" + " - list of commands and what they do"
     + bl + "`.home`" + " - Sends a link to our website")
    e = discord.Embed(title = "***Help Command***",description = dis, color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
    await ctx.send(embed = e)

# Quick and easy guide to start 
@client.command(name = "hep")
async def hep(ctx):
    owner = str(ctx.message.author.name)
    dis = ("Hey! Thanks for downloading GooseNeck Bot, make sure to type `.register` to get set up and claim 50 free coins. "
    "You can get cards by typing `.roll` as long as you have coins, which you can check by typing `.coin`. "
    "If you want more coins, you can type `.claim` every 10 minutes! Typeing `.inv` will tell you how many cards you "
    "have and typing a keyword after it will show how many of those cards you have. If you ever want to see a card, feel free "
    "to type `.view` and a unique ID. Thanks again for downloading GooseNeck Bot and have fun!")
    e = discord.Embed(description = dis, color = 0xa1ffb0)
    e.set_author(name = owner, icon_url = ctx.author.avatar_url)
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
    e = discord.Embed(title = "Home Page", url = "https://gooseweb.herokuapp.com/home",description = ("Will send user to home page site :D"), color = 0xa1ffb0)
    await ctx.send(embed = e)

# tells the user how many cards they have in their inventory
@client.command(name = "inv")
async def inventory(ctx, name = None):
    owner = str(ctx.message.author.name)
    userid = ctx.author.id
    username = str(ctx.author)
    user = ""
    for character in username:
        if character.isalnum():
            user += character
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    check = crsr.fetchall()

    crsr.execute("SELECT name FROM images WHERE name = %s", [name])
    real = crsr.fetchall()

    if not check:
        await ctx.send("You have not registered yet")

# tells them the total amount of cards they have
    elif name == None:
        crsr.execute("SELECT COUNT(*) FROM " + user)
        tot = str(crsr.fetchone())
        tot = remove(tot)
        e = discord.Embed(description = ("Total Cards = " + tot + "\n For a specific card enter card global id"), color = 0xa1ffb0)
        e.set_author(name = owner, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = e)

# shows them all the cards they have in an embedded list
    elif name == "all":
        embed = discord.Embed(title=f"__**{ctx.message.author.name} Results:**__", color = 0x03f8fc, timestamp = ctx.message.created_at)
        lst = []
        crsr.execute("SELECT COUNT(*) FROM " + user)
        tot = str(crsr.fetchone())
        tot = remove(tot)
        tot = int(tot)

        crsr.execute("SELECT globalid FROM " + user)
        num = str(crsr.fetchone())
        num = remove(num)

        crsr.execute("SELECT uniqueid FROM " + user)
        uid = crsr.fetchall()

        crsr.execute("SELECT date FROM " + user)
        date = str(crsr.fetchone())
        date = date.replace("datetime.date","")
        date = remove(date)
        date = date.replace(" ", "/")

        crsr.execute("SELECT cardrarity FROM " + user)
        rank = crsr.fetchall()

        crsr.execute("SELECT cardname FROM " + user)
        name = crsr.fetchall()

        for i in range(0, tot):
            unique = str(uid[i])
            unique = remove(unique)
            tname = str(name[i])
            tname = remove(tname)
            rare = str(rank[i])
            rare = remove(rare)
            lst.append((unique, tname, rare))
        print(lst)

        #cardLayout = '**Number Owned =** ' + tot + '\n **Global ID:** ' + num + '\n **Unique ID:** ' + uid + '\n **Date Rolled: **' + date + '\n**Rarity:** ' + rank
        '''
        cardLayout = srow
        embed = discord.Embed(title = name, color = 0xa1ffb0)
        embed.add_field(name=f'**{teamname}**', value=f'> Kills: {firstnum}\n> Position Pt: {secondnum}\n> Total Pt: {firstnum+secondnum}',inline=False)
        '''

        lstSorted = sorted(lst,reverse=True) # sort   
        for unique, tname, rare in lstSorted:  # process embed
            embed.add_field(name=f'{tname}', value=f'> uniqueID: {unique}\n> CardName: {tname}\n> Rarity: {rare}',inline=True)
        embed.set_author(name = owner, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

# error message that tells the user they spelled something wrong or the card does not exist
    elif not real:
        await ctx.send("The Card is spelled incorrectly or does not exist.")
        return

# searches for a specific card and how many of that card the user owns
    else:
        embed = discord.Embed(title=f"__**{ctx.message.author.name}'s Inventory:**__", color = 0x03f8fc, timestamp = ctx.message.created_at)
        lst = []
        crsr.execute("SELECT COUNT(*) FROM " + user + " WHERE cardname = %s", [name])
        tot = str(crsr.fetchone())
        tot = remove(tot)
        tot = int(tot)

        crsr.execute("SELECT globalid FROM " + user + " WHERE cardname = %s", [name])
        num = str(crsr.fetchone())
        num = remove(num)

        crsr.execute("SELECT uniqueid FROM " + user + " WHERE cardname = %s", [name])
        uid = crsr.fetchall()

        crsr.execute("SELECT date FROM " + user + " WHERE cardname = %s", [name])
        date = str(crsr.fetchone())
        date = date.replace("datetime.date","")
        date = remove(date)
        date = date.replace(" ", "/")

        crsr.execute("SELECT cardrarity FROM " + user + " WHERE cardname = %s", [name])
        rank = crsr.fetchall()

        crsr.execute("SELECT cardname FROM " + user + " WHERE cardname = %s", [name])
        name = str(crsr.fetchone())
        name = remove(name)

        for i in range(0, tot):
            unique = str(uid[i])
            unique = remove(unique)
            tname = name
            rare = str(rank[i])
            rare = remove(rare)
            lst.append((unique, tname, rare))

        #cardLayout = '**Number Owned =** ' + tot + '\n **Global ID:** ' + num + '\n **Unique ID:** ' + uid + '\n **Date Rolled: **' + date + '\n**Rarity:** ' + rank
        '''
        cardLayout = srow
        embed = discord.Embed(title = name, color = 0xa1ffb0)
        embed.add_field(name=f'**{teamname}**', value=f'> Kills: {firstnum}\n> Position Pt: {secondnum}\n> Total Pt: {firstnum+secondnum}',inline=False)
        '''

        lstSorted = sorted(lst,reverse=True) # sort   
        for unique, tname, rare in lstSorted:  # process embed
            embed.add_field(name = f'{name}', value = f'> uniqueID: {unique}\n> CardName: {tname}\n> Rarity: {rare}',inline = True)
        embed.set_author(name = owner, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

        '''
        if rarity == "all":
            crsr.execute("SELECT * FROM " + user + " ORDER BY cardrarity;")
            inv = str(crsr.fetchall())
            crsr.execute("SELECT COUNT(*) FROM " + user)
            tot = str(crsr.fetchall())
            await ctx.send(inv)
            await ctx.send(tot)
        elif rarity == "Common" or rarity == "Rare" or rarity == "Super Rare" or rarity == " Ultra Rare" or rarity == "Legendary":
            crsr.execute("SELECT cardname, cardrarity FROM " + user + " WHERE cardrarity = '" + rarity + "';")
            inv = str(crsr.fetchall())
            inv = remove(inv)
            e = discord.Embed(description = inv, color = 0xa1ffb0)
            await ctx.send(embed = e)
        else:
            e = discord.Embed(description = ("Requires second argument, use all to see all cards, plase use one of the following to see the following rarities : Common, Rare, Super Rare, Ultra Rare, Legendary"), color = 0xa1ffb0)
            await ctx.send(embed = e)
        '''

# Allows the user to view a card based on a unique ID
@client.command(name = "view")
async def view(ctx, uniqueid = None):
    if uniqueid == None:
        await ctx.send("Need a unique ID")
    else:
        owner = str(ctx.message.author.name)
        userid = ctx.author.id
        username = str(ctx.author)
        user = ""
        for character in username:
            if character.isalnum():
                user += character

        crsr.execute("SELECT count(*) FROM " + user)
        check = str(crsr.fetchone())
        check = remove(check)
        if uniqueid > check:
            await ctx.send("Card does not exist")
        else:
            crsr.execute("SELECT globalid FROM " + user + " WHERE uniqueid = %s", [uniqueid])
            num = str(crsr.fetchone())
            num = remove(num)

            crsr.execute("SELECT date FROM " + user + " WHERE uniqueid = %s", [uniqueid])
            date = str(crsr.fetchone())
            date = date.replace("datetime.date","")
            date = remove(date)
            date = date.replace(" ", "/")

            crsr.execute("SELECT cardrarity FROM " + user + " WHERE uniqueid = %s", [uniqueid])
            rank = str(crsr.fetchone())
            rank = remove(rank)
            cardColor = color(rank)

            crsr.execute("SELECT cardname FROM " + user + " WHERE uniqueid = %s", [uniqueid])
            name = str(crsr.fetchone())
            name = remove(name)

            cardLayout = '**General Info** \n **Global ID:** ' + num + '\n **Unique ID:** ' + uniqueid + '\n **Original Owner:** ' + owner + '\n **Date Rolled: **' + date + '\n\n' + '**Rarity:** ' + rank

            #gets google cloud url for photos
            murl = url(user, num)

            #card printout
            embed = discord.Embed(title = name, description = cardLayout, color = cardColor)
            embed.set_author(name = owner, icon_url = ctx.author.avatar_url)
            embed.set_image(url=murl)

            await ctx.send(embed = embed)

#inputs user's unique ID in to database and creates seperate inventory table
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
        cardrarity varchar (255),
        uniqueid int,
        globalid int,
        date date
    );
    """
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    data = crsr.fetchall()

    if not data:
        crsr.execute("INSERT INTO userinfo (userid,username,coins) VALUES(%s,%s,50);",[userid,username])
        conn.commit()
        crsr.execute(createtable)
        conn.commit()
        await ctx.send("You are now registered you silly goose.")
        
    else:
        await ctx.send("You already registered, you silly goose")

#takes one coin from the user and generates a random card/rarity and add it into their database
@client.command(name = "roll")
async def roll(ctx):
    userid = ctx.author.id
    crsr.execute("SELECT userid FROM userinfo where userid = %s;",[userid])
    data = crsr.fetchall()

    if not data:
        await ctx.send("You need to register first, you silly goose")
        return
    check = mon(userid)
    if(check == 0):
        await ctx.send("You're out of money, you silly goose")
        return
    elif(check == 1):
        num = random.randint(1, 19)
        rarity = random.randint(1, 100)
        username = str(ctx.author)
        user = ""
        for character in username:
            if character.isalnum():
                user += character
        crsr.execute("SELECT COUNT(*) FROM " + user ) 
        tot = crsr.fetchone()
        dtot = tot[0] + 1
        stot = str(dtot)       
        insert = "INSERT INTO "+ user + "(cardname, cardrarity, uniqueid, globalid, date) VALUES (%s, %s, %s, %s, %s);"

        owner = str(ctx.message.author.name)
        name = ["Alpaca10", "Boruto", "Conner", "GooseNeck", "IcyBoo", "Isabelle", "Joker", "Kratos", "Nezuko", "Nomad", "PacMan", "Plootle", "Sage", "Snorlax", "SpaceBoi", "Tom Nook", "YumStar", "Zavalla", "ZeroSuitSamus"]
        
        #rarity
        rank = setrarity(rarity)
        cardColor = rank[1]
        
        #time
        td = time()
        date = td[1]

        cardLayout = '**General Info** \n **Global ID:** ' + str(num) + '\n **Unique ID:** ' + stot + '\n **Original Owner:** ' + owner + '\n **Date Rolled: **' + date + '\n\n' + '**Rarity:** ' + rank[0]

        #gets google cloud url for photos
        murl = url(user, num)

        #card printout
        embed = discord.Embed(title = name[num-1], description = cardLayout, color = cardColor)
        embed.set_author(name = owner, icon_url = ctx.author.avatar_url)
        embed.set_image(url = murl)

        #sql
        crsr.execute(insert,(name[num-1], rank[2], stot, num, td[2]))
        conn.commit()
        await ctx.channel.send(embed = embed)

client.run(token)
