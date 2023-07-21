import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

from control import MyClient


async def cot(argument):
    argument = argument.upper()
    if ' ' in argument:
        argument = argument.replace(' ', '-')

    cota = requests.get(
        f'https://economia.awesomeapi.com.br/json/last/{argument}'
    )
    cota = cota.json()
    try:
        output = cota[f'{argument}']['bid']
        await MyClient.message.channel.send(
            f'The conversion {argument} is: {output}'
        )
    except:
        await MyClient.message.channel.send('Currency not found.')


async def rank_check(argument):
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
    await MyClient.message.channel.send(df)


async def ge_pricecheck(argument):
    url = f'https://oldschool.runescape.wiki/w/{argument}'
    html = requests.get(url)
    bs = soup(html.text, 'html.parser').find('div', class_='GEdataprices')
    item_id = bs['data-itemid']

    osrsgeresponse = requests.get(
        f'https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={item_id}'
    )
    data = osrsgeresponse.json()
    dataname = data['item']['name']
    datadesc = data['item']['description']
    dataprice = data['item']['current']['price']
    datatoday = data['item']['today']['price']
    await MyClient.message.channel.send(
        f"Name: {dataname}\nDescription: {datadesc}\nPrice: {dataprice}\nToday's change: {datatoday}"
    )
