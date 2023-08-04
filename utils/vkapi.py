import random
import requests

def vk_group_wall_image(vk_token,domain):
        version = '5.90'
        m=[]
        files=[]
        max = requests.get('https://api.vk.com/method/wall.get?access_token={}&v={}'.format(vk_token, version), params = {'domain': domain}).json()['response']['count']
        wall = requests.get('https://api.vk.com/method/wall.get?access_token={}&v={}'.format(vk_token, version), params = {'domain': domain, 'count': max, 'offset': random.randint(0, max)-1}).json()['response']['items'][0]

        if "attachments" in wall:
                if wall['attachments'][0]['type'] in ['doc', 'video', 'photo', 'audio']:
                        att = wall['attachments'][0]['photo']['sizes']
                        for size in att:
                                num = 0
                                if size['width'] > num:
                                        num = size['width']
                                        url = size['url']
                        return url
