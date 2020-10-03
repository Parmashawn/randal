import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="r")

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def ping(ctx):
    print("{ctx.author.name} called ping")
    await ctx.send("pong")

@client.command(aliases=['rules','commands','command','com'])
async def rule(ctx):
    print("{ctx.author.name} called Help")
    await ctx.send(f"**All commands start with 'r'** \n"
                    f"*rcommand* - gives list of commands\n"
                    f"*rflip* - flips a coin\n"
                    f"*rroll* - rolls a dice\n"
                    f"*rgay* - sends a picture of someone\n"
                    f"*rquote add <message link>*  - adds the linked message as a quote\n"
                    f"*rjoin* - announces a new fighter\n"
                    f"*rmc* - gives the IP for the Calamicraft server\n"
                    f"*rpoll* - creates a yes or no poll\n"
                    f"*rpollc* <option 1> or <option 2>* - creates a poll with two options\n"
                    f"*rquote* - sends a random quote\n"
                    f"*rping* - pong! ")

@client.command(aliases=['coin'])
async def flip(ctx):
    rngflip = random.choice(["Heads :speaking_head:!","Tails :dragon:!"])
    print(f"{ctx.author.name} flipped a coin, landed on {rngflip}")
    await ctx.send(rngflip)

@client.command()
async def roll(ctx):
    rngroll = random.choice([1,2,3,4,5,6])
    print(f"{ctx.author.name} rolled a {rngroll}")
    await ctx.send(f"{ctx.author.name} rolled a {rngroll}")

@client.command()
async def rgay 




client.run('NzU2NjM1NDg1NjMxNDE0Mjgz.X2UttQ.LXhNH9yakkmE9mERDesAb8UpL4E')
