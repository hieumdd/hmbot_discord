#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
token = os.getenv('DISCORD')

with open('tha_thinh.txt', 'r', encoding='utf-8') as f:
    tha_thinh = f.read().splitlines()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(random.choice(tha_thinh) + message.author.mention)

keep_alive()
client.run(token)