#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import discord
import os
import random

client = discord.Client()
with open('token.txt', 'r') as f:
    token = f.read()

list_of_text = [
    'HM đẹp zai vl',
    'HM chym to vl',
    'Quyên Quyên Quyên',
    'Chatbot này ngu nhưng nó biết trêu Sơn hahahahahahahahaha'
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send('Nhân danh NAM THẦN ĐỊT MẸ t đcm thg ' + message.author.mention)
    await message.channel.send(random.choice(list_of_text))

client.run(token)