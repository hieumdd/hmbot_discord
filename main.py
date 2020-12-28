#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import os
import random

client = discord.Client()
with open('token.txt', 'r') as f:
    token = f.read()

with open('tha_thinh.txt', 'r', encoding='utf-8') as f:
    tha_thinh = f.read().splitlines()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #await message.channel.send('Nhân danh NAM THẦN ĐỊT MẸ t đcm thg ' + message.author.mention)
    await message.channel.send(tha_thinh[0])

client.run(token)
