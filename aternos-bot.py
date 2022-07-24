#install discord.py and python-aternos before use pip install discord.py  and pip install python-aternos

import logging

from discord.ext import commands
from python_aternos import Client

logging.basicConfig(level=logging.INFO)

token = ""  # bot token here
user = ""  # enter your aternos username here
pswd = ""  # enter your aternos password here
aternos = Client.from_credentials(user, pswd)
servers = aternos.list_servers()

print(servers)  # make sure u make a new account and add only 1 server to it.

s = servers[0]
client = commands.Bot(command_prefix=".")  # changer your default prefix from here


@client.event
async def on_ready():
    print("Bot is now ready")


@client.command()
async def start(ctx):
    try:
        servers = aternos.list_servers()
        print(servers)
        s = servers[0]
        s.start()
        await ctx.send("Server is now Starting... (Will be online in 2-3 min)")
    except Exception as e:
        await ctx.send(e)


@client.command()
async def status(ctx):
    await ctx.send(s.status)


client.run(token)
