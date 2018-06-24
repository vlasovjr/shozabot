import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/pidor' or 'кто пидор?':
        bot.sendMessage(chat_id, '/pidor@SublimeBot')
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))


token = '547202133:AAETA12HvovlE_nzFoIHDpeVWXNZHF62-Io'

bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)