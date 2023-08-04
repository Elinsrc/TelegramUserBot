from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess

from utils.utils import prefix, owner, user_msg

@Client.on_message(filters.command(["term"], prefix))
async def shell_command(client: Client, message: Message):
        if not user_msg(message):
                await client.send_message(message.chat.id, '%sterm [команда]'%prefix)
                return

        if message.from_user.id == owner:
                process = subprocess.Popen(user_msg(message).split(), stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
                await client.send_message(message.chat.id, process)
        else:
                await client.send_message(message.chat.id, 'Команда доступна только для Владельца!')
