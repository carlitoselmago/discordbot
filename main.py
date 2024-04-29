import discord
import sqlite3
from datetime import datetime
import sys

# Enter your bot's token here
token=sys.argv[1]

conn=sqlite3.connect("clase.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS messages (author TEXT, message TEXT, date TEXT)")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    author=message.author.name
    current_dateTime = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    
    cur.execute("INSERT INTO messages (author,message,date) VALUES (?,?,?)",(author,message.content,current_dateTime))
    conn.commit()
    if message.content.startswith('hello'):
        pass
        #await message.channel.send('Hello!')

client.run(token)
