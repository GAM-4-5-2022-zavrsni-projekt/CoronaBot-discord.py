import discord
import random
import asyncio
from discord.ext import commands, tasks
from random import choice
from datetime import datetime, time, timedelta
from bs4 import BeautifulSoup
import requests
import re
import os
import keep_alive
import flask
import lxml
import threading
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

my_secret = os.environ['botid']
client = commands.Bot(command_prefix="%")
WHEN = time(13, 42, 0)  # vrijeme

@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Activity(
        name=">info for information"))
    await client.change_presence(activity=discord.Game(
        name=f"on {len(client.guilds)} servers"))


async def on_disconnect(msg):
    print("CoronaBot is not ready")
    await msg.channel.send("CoronaBot has been disconnected")

@client.event
async def ch_pr():
    await client.wait_until_ready()
    statuses = [f"on {len(client.guilds)} servers", "awaiting %help or %info"]

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)


client.loop.create_task(ch_pr())

@client.command(aliases=["i"],help="Additional information about the ")
async def info(ctx):
  embed=discord.Embed(title="Bot Information", color=0xEE2C2C)
  embed.set_author(name="CoronaBot")
  embed.set_thumbnail(url="https://pngimg.com/uploads/coronavirus/coronavirus_PNG46.png")
  embed.add_field(name="This is a discord bot made for educational purposes.", value="CoronaBot was made by Pavel C. and is designed to provide relevant information about covid infections and covid related deaths in Croatia and over the world. For suggestions and assistance message rus#2620 here on discord.", inline=False) 
  ctx.author.display_name
  ctx.author.avatar_url
  await ctx.send(embed=embed)

@client.command(name="ping", help="Command to check response time of the bot")
async def ping(ctx):
    await ctx.send(f"**Pong! UwU** Latency: {round(client.latency * 1000)}ms")




@client.command(pass_context = True, help="Command admins can use to subscribe a channel to Covid information updates typing %subscribe and adding the channel name without #",name='subscribe')
async def subscribe(ctx,inputname=""):
  if (inputname==""):
    await ctx.send("You should enter a channel's name after the command!")
  elif ctx.message.author.guild_permissions.administrator:
    channel = discord.utils.get(ctx.guild.channels, name=inputname)
    channel_id = channel.id
    print(channel_id)
    file1 = open("channel_id.txt","r")
    lines=file1.readlines()
    count=0
    for i in range(len(lines)):
      if int(lines[i])==channel_id:
        count+=1
    file1.close()
    if count==0:
      file1 = open("channel_id.txt","a")
      file1.write(str(channel_id)+'\n')
      file1.close()
      await ctx.send("You've sucessfully subscribed! You can unsubscribe anytime.")
    else:
      await ctx.send('This channel is already subscribed') 
  else:
    await client.send_message(ctx.message.channel, "Looks like you don't have the perm to do this.")

@client.command(pass_context = True, help="Command admins can use to unsubscribe a channel from Covid information updates typing %unsubscribe and adding the channel name without #",name='unsubscribe')
async def unsubscribe(ctx,inputname=""):
  if (inputname==""):
    await ctx.send("You should enter a channel's name after the command!")
  elif ctx.message.author.guild_permissions.administrator:
    channel = discord.utils.get(ctx.guild.channels, name=inputname)
    channel_id = channel.id
    print(channel_id)
    with open("channel_id.txt", "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                if str(channel_id) not in line.strip("\n"):
                    output.write(line)
    os.replace('temp.txt', 'channel_id.txt')

    await ctx.send("You've sucessfully unsubscribed! You can subscribe again anytime.")
  else:
    await client.send_message(ctx.message.channel, "Looks like you don't have the perm to do this.")






@client.group(aliases=["korona", "covid", "kovid"],
              help="This command provides relevant information about Covid-19 contagions and deaths for a requested country. Default country is Croatia")

async def corona(ctx, loc=""):
    print(loc)
    if loc == "":
        url = "https://www.worldometers.info/coronavirus/country/croatia"
        loc = "Croatia"
    else:
        url = (f"https://www.worldometers.info/coronavirus/country/{str(loc)}")
    print(loc)
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    information = soup.find('li', class_="news_li")
    print(information)
    children = information.findChildren("strong", recursive=False)
    embed = discord.Embed(
        title=f"__**Covid info today in {loc.capitalize()}**__ ")

    print(children)
    naslov = ""
    tekst = ""
    naslov = str(children[0])
    tekst = str(children[1])
    naslov = naslov.replace("<strong>", "")
    naslov = naslov.replace("</strong>", "")
    tekst = tekst.replace("<strong>", "")
    tekst = tekst.replace("</strong>", "")
    embed.add_field(name=naslov, value=tekst, inline=False)
    embed.set_author(name="CoronaBot")
    embed.set_thumbnail(url="https://pngimg.com/uploads/coronavirus/coronavirus_PNG46.png")
    await ctx.send(embed=embed)



async def called_once_a_day():  # Fired every day
    await client.wait_until_ready(
    )  # Make sure your guild cache is ready so the channel can be found via get_channel

    url = 'https://www.worldometers.info/coronavirus/country/croatia'
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    information = soup.find('li', class_="news_li")
    children = information.findChildren("strong", recursive=False)
    embed = discord.Embed(title=f"__**Koronavirus danas u Hrvatskoj**__ ", color=0xEE2C2C)

    naslov = ""
    tekst = ""
    naslov = str(children[0])
    tekst = str(children[1])
    naslov = naslov.replace("<strong>", "")
    naslov = naslov.replace("</strong>", "")
    tekst = tekst.replace("<strong>", "")
    tekst = tekst.replace("</strong>", "")
    embed.add_field(name=naslov, value=tekst, inline=False)
    embed.set_footer(text="You are subscribed to daily covid updates. To unsubscribe message the Russian.")

    file1 = open("channel_id.txt","r")
    channel_id=file1.readlines()
    for i in range(len(channel_id)):
      channel = client.get_channel(int(channel_id[i]))
      print(channel)
      print(channel_id[i])
      await channel.send(embed=embed)
    file1.close()


async def background_task():
    now = datetime.utcnow()
    if now.time(
    ) > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow -
                   now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(
            seconds)  # Sleep until tomorrow and then the loop will start
    while True:
        now = datetime.utcnow(
        )  # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
        target_time = datetime.combine(now.date(),
                                       WHEN)  # 6:00 PM today (In UTC)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target
                            )  # Sleep until we hit the target time
        await called_once_a_day(
        )  # Call the helper function that sends the message
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow -
                   now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(
            seconds
        )  # Sleep until tomorrow and then the loop will start a new iteration



if __name__ == "__main__":
    client.loop.create_task(background_task())
keep_alive.keep_alive()
client.run(my_secret)
