from .. import chat_id, logger, api_hash, api_id, proxystart, proxy, jdbot
from ..bot.utils import cookies
from telethon import events, TelegramClient
import requests
import re
#----------------------------------------------------#
# version:1.1
# author:
# date:2021-5-18
# 使用方法:放到diy下边，然后终端内输入pm2 stop jbot 然后python3 -m jbot 按照提示输入手机号和验证码，输入完后，ctrl+c停止，然后pm2 start jbot
#----------------------------------------------------#
if proxystart:
    user = TelegramClient('shopbean', api_id, api_hash,
                          proxy=proxy, connection_retries=None).start()
else:
    user = TelegramClient('shopbean', api_id, api_hash,
                          connection_retries=None).start()


@user.on(events.NewMessage(chats=[-1001197524983]))
async def myshopbean(event):
    msg = event.message.text
    if '京豆' in msg:
        urlreg = re.compile(
            r'https://api.m.jd.com/client.action\?functionId=drawShopGift\S*')
        url = urlreg.findall(msg)
        logger.info(url[0].replace(')', ''))
        if len(url) > 0 and len(cookies) > 0:
            i = 0
            info = msg.split('\n')[0]+'\n'
            for cookie in cookies:
                try:
                    i = i + 1
                    info = info + getbean(i, cookie, url[0].replace(')', ''))
                except Exception as e:
                    await jdbot.send_message(chat_id,'账号'+str(i)+'发生了错误\n'+str(e))  
                    continue
        await jdbot.send_message(chat_id,info)  

def getbean(i, ck, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Cookie": ck,
    }
    res = requests.get(url, headers=headers).json()
    beaninfo = res['result']['followDesc']+'\n'+res['result']['giftsToast']
    return '账号'+str(i)+':'+beaninfo+'\n'

