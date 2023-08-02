import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

class Commands_methods:
    def cot(argument):
        argument = argument.upper()
        if ' ' in argument:
            tocon = argument.split(' ')[0]
            fromcon = argument.split(' ')[1]
            cota = requests.get(
                f'https://economia.awesomeapi.com.br/json/last/{tocon}-{fromcon}'
            )
            cota = cota.json()
            output = cota[f'{tocon}{fromcon}']['bid']
            return f'The conversion {tocon} to {fromcon} is: {output}'
        
        try:
            cota = requests.get(
                    f'https://economia.awesomeapi.com.br/json/last/{argument}'
                )
            cota = cota.json()
            output = cota[f'{argument}BRL']['bid']
            return f'The conversion {argument} to BRL is: {output}'
        except:
            return f'Sorry but you commited an input error (Ooopsie)\neither that, or the API server is offline.'



    def rank_check(argument):
        osrsrankresponse = requests.get(
            f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={argument}'
        )
        skills = [
            'Overall',
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
            'Mining',
            'Herblore',
            'Agility',
            'Thieving',
            'Slayer',
            'Farming',
            'Runecrafting',
            'Hunter',
            'Construction',
        ]
        levels = []
        ranks = osrsrankresponse.text
        rows = ranks.split('\n')
        for i, row in enumerate(rows):
            if i == 24:
                break
            column = row.split(',')
            levels.append(column[1])
        data = {'Skills': skills, 'Level': levels}
        df = pd.DataFrame(data)
        return df


    def ge_pricecheck(argument):
        try:
            url = f'https://oldschool.runescape.wiki/w/{argument}'
            html = requests.get(url)
            bs = soup(html.text, 'html.parser').find('div', class_='GEdataprices')
            item_id = bs['data-itemid']
        except:
            return "Couldn't find the item."

        osrsgeresponse = requests.get(
            f'https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={item_id}'
        )
        data = osrsgeresponse.json()
        dataname = data['item']['name']
        datadesc = data['item']['description']
        dataprice = data['item']['current']['price']
        datatoday = data['item']['today']['price']

        return f"Name: {dataname}\nDescription: {datadesc}\nPrice: {dataprice}\nToday's change: {datatoday}"
