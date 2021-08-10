from telethon import TelegramClient
import time

api_id = 4837309
api_hash = '51a7244aa4f9f1bb83b3093bb6dadcb0'

time.sleep(10)  #数字换成想要的秒数

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('@TuringLabbot', '/submit_activity_codes bean'))
