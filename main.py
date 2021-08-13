import os
import random

import requests
import discord
from keep_alive import keep_alive

client = discord.Client()
token = os.getenv("DISCORD_TOKEN")


def get_tha_thinh():
    with open("tha_thinh.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


def get_imgur():
    headers = {
        "Authorization": f"Client-ID {os.getenv('CLIENT_ID')}",
    }
    subreddit = 'aiyu'
    sort = "time"
    window = "all"
    page = 1
    url = f"https://api.imgur.com/3/gallery/r/{subreddit}/{sort}/{window}/{page}"
    with requests.get(
        url,
        headers=headers,
    ) as r:
        res = r.json()
    return [
        i["link"]
        for i in res["data"]
        if i["in_gallery"] is False and i["is_ad"] is False
    ]


def get_responses(message):
    image_embed = discord.Embed()
    image_embed.set_image(
        url=random.choice(get_imgur()),
    )
    return {
        "content": message.author.mention + " | " + random.choice(get_tha_thinh()),
        "embed": image_embed,
    }


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(**get_responses(message))


keep_alive()
client.run(token)
