import discord
from discord.ext import commands
from decouple import config
from controllers import control

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents,command_prefix='!')

@bot.command(name='rank')
async def rank(ctx,*,arg):
    await ctx.send(control.rank_check(arg))

@bot.command(name='rsge')
async def rsge(ctx,*,arg):
    await ctx.send(control.ge_pricecheck(arg))

@bot.command(name='cot')
async def cot(ctx,*,arg):
    await ctx.send(control.cot(arg))

bot.run(config('discord_bot_key'))