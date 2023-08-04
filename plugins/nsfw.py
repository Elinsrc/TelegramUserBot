from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import random

from utils.utils import prefix, user_msg, config

@Client.on_message(filters.command(["34"], prefix))
async def send_rule34(client: Client, message: Message):
    try:
        data = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit=500&tags={}".format(user_msg(message))).json()
    except json.JSONDecodeError:
        await client.send_message(message.chat.id, "Ничего ненайдeнно по тегу: {} ".format(args(message)))

    count = len(data)
    images = []
    image = data[random.randint(0, count)]
    images.append("https://wimg.rule34.xxx//images/{}/{}".format(image["directory"], image["image"]))

    img = '{}\n'.join(images)
    tags = '{}'.format(image['tags'])

    if img.endswith('.gif'):
        await client.send_document(message.chat.id, img)
    elif img.endswith('.mp4'):
        await client.send_video(message.chat.id, img)
    else:
        await client.send_photo(message.chat.id, img)

    await client.send_message(message.chat.id, f'Теги: {tags}\n')
