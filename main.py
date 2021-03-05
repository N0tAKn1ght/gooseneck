import discord
import os
import asyncio
import asyncpg

client = discord.Client()
async def run():
    description = "GooseNeck bot"
    credentials = {"user": "USERNAME", "password": "MoonS00n1342!", "database": "gooseneck", "host": "172.17.0.1"}
    db = await asyncpg.create_pool(**credentials)
    await db.execute("CREATE TABLE IF NOT EXISTS users(id bigint PRIMARY KEY, data text);")

    bot = Bot(description = description, db = db)
    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.help'):
        await message.channel.send('Hello!')
client.run('ODA4NDE1ODg5ODc1NjY0OTI3.YCGN9w.qIBD2q-uteQ_YIyEYeubBFVCNhk')
