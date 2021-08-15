import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '!') 
@bot.event
async def on_ready():
    print(f"Connected to {bot.user}")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send("Unknown command.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "ping":
        await message.channel.send("pong")
        
@commands.has_permissions(ban_members=True)
@bot.command() 
async def бан(ctx, user: discord.Member, *, reason="No reason"):
    await user.ban(reason=reason)
    ban = discord.Embed(title=f"<:geneleak:869697081558831164> Забанен {user.name}!", description=f"Причина: {reason}\nЗабанил: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)
@commands.has_permissions(ban_members=True) # ну просто нету unban_Members
@bot.command() # use: !unban Romashka#9339
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} Unbanned")
    return

@bot.command()
async def test(ctx):
    await ctx.send("test") 
    
bot.run('token')     
