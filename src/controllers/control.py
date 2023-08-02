import discord
from discord.ext import commands
from decouple import config
from models import model
from views import view

class Discord_bot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        bot = commands.Bot(intents=intents,command_prefix='!')
        bot.run(config('discord_bot_key'))

    def bot_command(self):
        @self.bot.command(name='rank')
        async def rank(ctx,*,arg):
            await ctx.send(self.model.rank_check(arg))

        @self.bot.command(name='rsge')
        async def rsge(ctx,*,arg):
            await ctx.send(self.model.ge_pricecheck(arg))

        @self.bot.command(name='cot')
        async def cot(ctx,*,arg):
            await ctx.send(self.model.cot(arg))
