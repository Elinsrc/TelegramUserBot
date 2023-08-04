from pyrogram import Client, filters
from pyrogram.types import Message

from utils.utils import prefix, owner

@Client.on_message(filters.command(["help"], prefix))
async def send_help(client: Client, message: Message):
        msg = "Видео:\n"
        msg += "%svplay - Запускает стрим видео с прямой ссылки\n"%prefix
        msg += "%sytplay - Стрим видео с youtube\n"%prefix
        msg += "%spause - Ставит стрим на паузу\n"%prefix
        msg += "%sresume - Убирает паузу\n"%prefix
        msg += "%smute - Убрать звук\n"%prefix
        msg += "%sunmute - Вернуть звук\n"%prefix
        msg += "%sstop - Остановить стрим\n\n"%prefix
        msg += "Картинки:\n"
        msg += "%syandex - Yandex картинки\n"%prefix
        msg += "%sgoogle - Google картинки\n"%prefix
        msg += "%sstockings - Тян в чулочках\n\n"%prefix
        msg += "Nsfw:\n"
        msg += "%srule34 - Вы знаете что это xD\n"%prefix
        msg += "Информация:\n"
        msg += "%sgpt- Отвечает на вопросты\n"%prefix
        msg += "%sxash - Информация o серверах Xash3D\n"%prefix
        msg += "%sip - Информация об ip или домене\n"%prefix
        msg += "%swiki - Статья с wikipedia\n"%prefix
        msg += "%sweather - Показывает погоду\n\n"%prefix
        msg += "Прочее:\n"
        if message.from_user.id == owner:
                msg += "%sterm - Достук к shell терминалу\n"%prefix
        msg += "%suser_id - Показывает ваш ID\n"%prefix
        msg += "%schat_id - Показывает ID чата\n"%prefix
        await client.send_message(message.chat.id, 'Команды:\n\n{}'.format(msg))

