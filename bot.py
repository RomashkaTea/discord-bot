import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '!') 
@bot.event
async def on_ready():
    print(f"Connected to {bot.user}")
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "ping":
        await message.channel.send("pong")

@bot.command()
async def test(ctx):
    await ctx.send("test") 
    
bot.run('token')     
