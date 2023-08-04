from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import wikipedia
import asyncio
import os

from utils.utils import prefix, user_msg, config

@Client.on_message(filters.command(["wiki"], prefix))
async def send_wiki(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%swiki [запрос]'%prefix)
                return
        try:
                wikipedia.set_lang("ru")
                p = wikipedia.page(user_msg(message))
                t = wikipedia.summary(user_msg(message))
                msg = "Страница: %s\n\n"%p.url
                msg += "\t %s"%t
                await client.send_message(message.chat.id, msg)
        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')

@Client.on_message(filters.command(["weather"], prefix))
async def send_weather(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%sweather [Город]'%prefix)
                return
        try:
                weather = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'lang':'ru', 'units': 'metric', 'APPID': '02048c30539276ca0aaca33944aa39c1', 'q':user_msg(message)}).json()

                msg = "Погода в " + str(weather['sys']['country']) + "/" + str(weather["name"]) + ":\n"
                msg += '•Температура: ' + str('%.0f' %(weather["main"]["temp"])) + '°C\n'
                msg += '•Скорость ветра: ' + str(weather["wind"]["speed"]) + 'м/с\n'
                msg += '•Влажность: ' + str(weather["main"]["humidity"]) + '%\n'
                msg += '•Состояние: ' + str(weather["weather"][0]["description"]) + "\n";
                msg += '•Давление: ' +  str('%.0f' %( float(weather['main']['pressure'])/1000*750.06)) + ' мм рт. ст.\n'

                await client.send_message(message.chat.id, msg)
        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')

@Client.on_message(filters.command(["ip"], prefix))
async def send_ip(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%sip [ip или домен]'%prefix)
                return
        try:
                ipapi = requests.get('http://ip-api.com/json/{}?fields=query,reverse,countryCode,country,regionName,city,zip,lat,lon,timezone,org,as,asname,isp&lang=ru'.format(user_msg(message))).json()

                msg = "IP: " + str(ipapi['query']) + "\n"
                msg += "Хост: " + str(ipapi['reverse']) + "\n"
                msg += "Страна: " + str(ipapi["countryCode"]) + "/" + str(ipapi['country']) + "\n"
                msg += "Регион: " + str(ipapi['regionName']) + "\n"
                msg += "Город: " + str(ipapi['city']) + "\n"
                msg += "Индекс: " + str(ipapi['zip']) + "\n"
                msg += "Широта: " + str(ipapi['lat']) + "\n"
                msg += "Долгота: " + str(ipapi['lon']) + "\n"
                msg += "Временная зона: " + str(ipapi['timezone']) + "\n"
                msg += "Организация: " + str(ipapi['org']) + "\n"
                msg += "AS: " + str(ipapi['as']) + "\n"
                msg += "ASNAME: " + str(ipapi['asname']) + "\n"
                msg += "Провайдер: " + str(ipapi['isp']) + "\n"

                await client.send_message(message.chat.id, msg)
        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')

@Client.on_message(filters.command(["user_id"], prefix))
async def send_userid(client: Client, message: Message):
        id = message.from_user.id
        await client.send_message(message.chat.id, f"Ваш ID: {id}")

@Client.on_message(filters.command(["chat_id"], prefix))
async def send_chatid(client: Client, message: Message):
        chat_id = message.chat.id
        await client.send_message(message.chat.id, f"ID чата: {chat_id}")
