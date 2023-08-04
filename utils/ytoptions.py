import yt_dlp

YTDL_OPTIONS = {
    'format': 'best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    }

ytdl = yt_dlp.YoutubeDL(YTDL_OPTIONS)

@staticmethod
def parse_duration(duration: int):
  minutes, seconds = divmod(duration, 60)
  hours, minutes = divmod(minutes, 60)
  days, hours = divmod(hours, 24)

  duration = []
  if days > 0:
    duration.append('{} день'.format(days))
  if hours > 0:
    duration.append('{} час'.format(hours))
  if minutes > 0:
    duration.append('{} мин'.format(minutes))
  if seconds > 0:
    duration.append('{} сек'.format(seconds))

  value = ' '.join(duration)
  return value

def playing(query):
  video_results = ytdl.extract_info("ytsearch:{}".format(query), download=False)['entries']
  video = video_results[0]
  return video

def description(video):
  msg = "Стрим: " + str(video['title']) + "\n"
  if video["is_live"] == True:
    msg += "Прямая трансляция\n"
  else:
    msg += "Продолжительность: " + str(parse_duration(int(video['duration']))) + "\n"

  return msg

def thumbnail(video):
  img = video['thumbnail']
  return img
