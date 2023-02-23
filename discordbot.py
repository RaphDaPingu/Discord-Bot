import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = commands.Bot(command_prefix='%', intents=intents)

MY_ID = 197341306152812544

#kicks user when already in a voice channel

@client.event
async def on_ready():
    try:
        member = client.get_user(MY_ID)

        for channel in client.get_all_channels():
            if ("VoiceChannel" in str(type(channel))):
                if (member in channel.members):
                    member = channel.guild.get_member(member.id)
                    await member.edit(voice_channel=None)
    except Exception as e:
        print(e)

#kicks user when trying to log into a voice channel

@client.event
async def on_voice_state_update(member, before, after):
    if (member.id == MY_ID):
        if (before.channel is None and after.channel is not None):
            await member.edit(voice_channel=None)
    
client.run(TOKEN)
