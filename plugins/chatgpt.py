from pyrogram import Client, filters
from pyrogram.types import Message
import openai

from utils.utils import prefix, user_msg, config

openai.api_key = config['openai_token']

is_request_executing = False

@Client.on_message(filters.command(["gpt"], prefix))
async def send_gpt(client: Client, message: Message):
        global is_request_executing
        if not user_msg(message):
                await client.send_message(message.chat.id, '%sgpt [запрос]'%prefix)
                return

        if is_request_executing:
                await client.send_message(message.chat.id, 'Запрос уже выполняется! Ждите завершения!')
                return

        try:
                is_request_executing = True
                await client.send_message(message.chat.id, "Подожите!")
                response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "system", "content": user_msg(message)}])
                await client.send_message(message.chat.id, response.choices[0].message.content)
                is_request_executing = False

        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')
