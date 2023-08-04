import json

def user_msg(message):
        return ' '.join(message.text.split(' ')[1:])

with open('utils/config.json', 'r') as f:
        config = json.load(f)

prefix = config['prefix']
owner = config['owner']
user_agent = config['user_agent']
