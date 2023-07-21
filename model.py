import discord
import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from decouple import config

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        #Command methods
        async def cot():
            argument = argument.upper()
            if " " in argument:
                argument = argument.replace(" ","-")

            cota = requests.get(f'https://economia.awesomeapi.com.br/json/last/{argument}')
            cota = cota.json()
            try:
                output = cota[f'{argument}']["bid"]
                await message.channel.send(f"The conversion {argument} is: {output}")
            except:
                await message.channel.send("Currency not found.")

        async def rank_check():
            osrsrankresponse = requests.get(
                f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={argument}')
            skills = ['Overall',
                    'Attack',
                    'Defence',
                    'Strength',
                    'Hitpoints',
                    'Ranged',
                    'Prayer',
                    'Magic',
                    'Cooking',
                    'Woodcutting',
                    'Fletching',
                    'Fishing',
                    'Firemaking',
                    'Crafting',
                    'Smithing',
                    'Mining', 'Herblore', 'Agility', 'Thieving', 'Slayer', 'Farming', 'Runecrafting', 'Hunter', 'Construction']
            levels = []
            ranks = osrsrankresponse.text
            rows = ranks.split('\n')
            for i,row in enumerate(rows):
                if i == 24:
                    break
                column = row.split(',')
                levels.append(column[1])
            data = {'Skills': skills, 'Level': levels}
            df = pd.DataFrame(data)
            await message.channel.send(df)

        async def ge_pricecheck():
            url = f'https://oldschool.runescape.wiki/w/{argument}'
            html = requests.get(url)
            bs = soup(html.text, 'html.parser').find("div", class_="GEdataprices")
            item_id = bs['data-itemid']
            
            osrsgeresponse = requests.get(f'https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={item_id}')
            data = osrsgeresponse.json()
            dataname = data['item']['name']
            datadesc = data['item']['description']
            dataprice = data['item']['current']['price']
            datatoday = data['item']['today']['price']
            await message.channel.send(f"Name: {dataname}\nDescription: {datadesc}\nPrice: {dataprice}\nToday's change: {datatoday}")

        #Command call
        if not message.content[0] == "!":
            return
            
        command = message.content.split(" ")[0]
        argument = message.content.replace(f"{command} ","")

        match(command):
            case "!rank":
                await rank_check()
            case "!rsge":
                await ge_pricecheck()
            case "!cot":
                await cot()
            case _:
                await message.channel.send("Comando inválido")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config('discord_bot_key'))