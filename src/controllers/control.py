import discord
from discord.ext import commands
from decouple import config
from models import model
from views import view

class Discord_bot():
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.bot = commands.Bot(intents=self.intents,command_prefix='!')

    def bot_commands(self):

        @self.bot.command(name='rank')
        async def rank(ctx,*,arg):
            await ctx.send(model.Commands_methods.rank_check(arg))

        @self.bot.command(name='rsge')
        async def rsge(ctx,*,arg):
            await ctx.send(model.Commands_methods.ge_pricecheck(arg))

        @self.bot.command(name='cot')
        async def cot(ctx,*,arg):
            await ctx.send(model.Commands_methods.cot(arg))
            
    def run(self):
        self.bot_commands()
        self.bot.run(config('discord_bot_key'))

