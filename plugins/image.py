from pyrogram import Client, filters
from pyrogram.types import Message
from yamager import Yamager
import random

from utils.utils import prefix, user_msg, config
from utils.vkapi import vk_group_wall_image

@Client.on_message(filters.command(["yandex"], prefix))
async def yandex_image(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%syandex [запрос]'%prefix)
                return
        try:
                yamager = Yamager()
                images = yamager.search_yandex_images(user_msg(message))
                previews = random.choice(images)
                image = yamager.get_best_image(previews)

                if image.endswith('.gif'):
                        await client.send_document(message.chat.id, image)
                else:
                        await client.send_photo(message.chat.id, image)

        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')

@Client.on_message(filters.command(["google"], prefix))
async def google_image(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%sgoogle [запрос]'%prefix)
                return
        try:
                yamager = Yamager()
                images = yamager.search_google_images(user_msg(message))
                image = random.choice(images)

                if image.endswith('.gif'):
                        await client.send_document(message.chat.id, image)
                else:
                        await client.send_photo(message.chat.id, image)

        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')

@Client.on_message(filters.command(["stockings"], prefix))
async def stockings_image(client: Client, message: Message):
        try:
                domain = random.choice(['publictyanchulki', 'stockings4you'])
                vk_token = config["vktoken"]
                url = vk_group_wall_image(vk_token,domain)
                await client.send_photo(message.chat.id, url)

        except Exception as e:
                await client.send_message(message.chat.id, f'Ошибка: {e}')
