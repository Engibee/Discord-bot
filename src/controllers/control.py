import discord
from decouple import config

from views import view


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Command call
        if not message.content[0] == '!':
            return

        command = message.content.split(' ')[0]
        argument = message.content.replace(f'{command} ', '')

        view.do_something(command, argument)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config('discord_bot_key'))
