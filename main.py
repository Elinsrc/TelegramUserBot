from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls import exceptions
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, HighQualityVideo
from pyrogram import filters

from utils.utils import config, prefix, user_msg, user_agent
from utils.ytoptions import ytdl, playing, description, thumbnail

async def main():
        plugins = dict(root="plugins")
        app = Client('client', api_id=config['api_id'], api_hash=config['api_hash'], plugins = plugins)
        call_py = PyTgCalls(app)
        call_py.start()

@app.on_message(filters.command(["vplay"], prefixes=prefix))
async def video_handler(client, message):
        try:
                if not user_msg(message):
                        await app.send_message(message.chat.id, '%svplay [ссылка]'%prefix)
                        return
                try:
                        await call_py.join_group_call(message.chat.id, AudioVideoPiped(user_msg(message), headers={'User-Agent':user_agent}))
                except exceptions.AlreadyJoinedError:
                        await call_py.change_stream(message.chat.id, AudioVideoPiped(user_msg(message), headers={'User-Agent':user_agent}))
                await app.send_message(message.chat.id, 'Стрим видео')
        except Exception as e:
                await app.send_message(message.chat.id, f'Ошибка: {e}')

async def playvideo(chat_id, url, img, preview):
        try:
                await call_py.join_group_call(chat_id, AudioVideoPiped(url, headers={'User-Agent':user_agent}))
        except exceptions.AlreadyJoinedError:
                await call_py.change_stream(chat_id, AudioVideoPiped(url, headers={'User-Agent':user_agent}))
        await app.send_photo(chat_id, photo=img, caption=preview)

@app.on_message(filters.command(["ytplay"], prefixes=prefix))
async def youtube_handler(client, message):
        try:
                if not user_msg(message):
                        await app.send_message(message.chat.id, '%sytplay [ссылка или запрос]'%prefix)
                        return

                video = playing(user_msg(message))
                preview = description(video)
                img = thumbnail(video)
                url = video['url']

                await playvideo(message.chat.id, url, img, preview)
        except Exception as e:
                await app.send_message(message.chat.id, f'Ошибка: {e}')

@app.on_message(filters.command(["pause"], prefixes=prefix))
async def pause_handler(client,message):
        await call_py.pause_stream(message.chat.id)
        await app.send_message(message.chat.id,'Стрим на паузе!')

@app.on_message(filters.command(["resume"], prefixes=prefix))
async def resume_handler(client, message):
        await call_py.resume_stream(message.chat.id)
        await app.send_message(message.chat.id, 'Пауза убранна! ')

@app.on_message(filters.command(["mute"], prefixes=prefix))
async def mute_handler(client,message):
        await call_py.mute_stream(message.chat.id)
        await app.send_message(message.chat.id,'Звук отключен!')

@app.on_message(filters.command(["unmute"], prefixes=prefix))
async def unmute_handler(client, message):
        await call_py.unmute_stream(message.chat.id)
        await app.send_message(message.chat.id, 'Включен звук!')

@app.on_message(filters.command(["stop"], prefixes=prefix))
async def stop_handler(client,message):
        await call_py.leave_group_call(message.chat.id)
        await app.send_message(message.chat.id, 'Стрим остановлен!')

@call_py.on_stream_end()
async def stream_end_handler(client: PyTgCalls, update: Update):
        await call_py.leave_group_call(update.chat_id)
        await app.send_message(update.chat_id, 'Стрим закончился!')

asyncio.run(main())
idle()
