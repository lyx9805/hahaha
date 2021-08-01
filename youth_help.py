import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys

#####################TGbot##########################
TG_BOT_TOKEN = '1735606998:AAGGh3J4WbpqKv7-NwnPBGUyZGGB1ZJWIU0'
TG_USER_ID = '1600767733'
TG_API_HOST = ''              # tg 代理api
TG_PROXY_IP = ''            # tg机器人的TG_PROXY_IP; secrets可填
TG_PROXY_PORT = ''
#####################################################


#################################中青阅读链接#####################################

urls = ['https://focus.youth.cn/article/s?signature=VOZvBzYN5rkDxgX7YY6vmNSMbmjRIV5qyDY7L3yAP6WMnmlGK9&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39416330&time=1627183043&app_version=2.0.2&sign=adad46a31c08365f68576149c02c189d',
        'https://focus.youth.cn/article/s?signature=6jEkyrXeG8nBYgKax6MQGXswLygGhKwy6ye4DwldQJz0L2RON3&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39453859&time=1627183058&app_version=2.0.2&sign=c257df5c9b98eccc72a3e3b5bb789015',
        'https://focus.youth.cn/article/s?signature=QqvZWbEKpA2yrNR1M0x8OzUK3bDOfLoYkYMa9VGjJl8gXB5keP&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39430690&time=1627183067&app_version=2.0.2&sign=bd48ff6ba8f684ec7e3403fb8c2fe8f7',
        'https://focus.youth.cn/article/s?signature=6K3Zgj0LVrQbJw94VZDkK9cbXMNnco5wDEp4mxB5qW8oDnvelE&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39523161&time=1627702010&app_version=2.0.2&sign=f77cfd5d5b70bd96c9d7668a4708a652',
        'https://focus.youth.cn/article/s?signature=dQOvnJNrgR0GzE9azZgwQXs8OENVHrwBQpwaV6yqY2lXojxeM8&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39330175&time=1627702028&app_version=2.0.2&sign=e0909e0ad613a840e1696b9b96cc4dc5',
        'https://focus.youth.cn/article/s?signature=gENjGxJw2L6opAMamveGnyTRVvm2TO9pEvd1nX3kY58KdmBzRO&uid=54424182&phone_code=ae472b3df050b7272370704c049963b7&scid=39535029&time=1627702062&app_version=2.0.2&sign=166476ca1a0de64fb60ac634b440fc2f'
        ]
#########################################################################################################


###############################User-Agent####################################

ua_list = ['Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN',
           'Mozilla/5.0 (Linux; Android 10; CDY-AN90 Build/HUAWEICDY-AN90; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200801 Mobile Safari/537.36 MMWEBID/4006 MicroMessenger/7.0.18.1740(0x2700123B) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
           'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI',
           'Mozilla/5.0 (Linux; Android 8.1.0; MI 5X Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200801 Mobile Safari/537.36 MMWEBID/9633 MicroMessenger/7.0.18.1740(0x2700123B) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
           'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001124) NetType/WIFI Language/zh_CN'
           ]
###################################################################################################


###########################################IP代理##############################################

ip_url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=9ef2ce60a5e2c1621ab89c3f342bfa4c&orderNo=GL20210616100341bvC9uqlM&count=1&isTxt=1&proxyType=1'

###############################################################################################


begin_time = time.time()

#获取本次阅读的IP和UA
ua = random.choice(ua_list)
print('UA：{}'.format(ua))
ip = requests.get(ip_url)
print('IP：{}'.format(ip.text))


option = webdriver.ChromeOptions()
option.add_argument('user-agent={}'.format(ua))   #选择请求头
option.add_argument('--proxy-server={}'.format(ip.text))  #使用ip代理
# option.add_argument('--headless')   #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
option.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
option.add_argument('window-size=1920x3000') #指定浏览器分辨率
option.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
option.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
option.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度


message_info = ''


def message(str_msg):
    global message_info
    print(str_msg)
    message_info = "{}\n{}".format(message_info, str_msg)
    sys.stdout.flush()


def telegram_bot(title, content):
    try:
        print("\n")
        bot_token = TG_BOT_TOKEN
        user_id = TG_USER_ID
        if not bot_token or not user_id:
            print("tg服务的bot_token或者user_id未设置!!\n取消推送")
            return
        print("tg服务启动")
        if TG_API_HOST:
            url = f"{TG_API_HOST}/bot{TG_BOT_TOKEN}/sendMessage"
        else:
            url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'chat_id': str(TG_USER_ID), 'text': f'{title}\n\n{content}', 'disable_web_page_preview': 'true'}
        proxies = None
        if TG_PROXY_IP and TG_PROXY_PORT:
            proxyStr = "http://{}:{}".format(TG_PROXY_IP, TG_PROXY_PORT)
            proxies = {"http": proxyStr, "https": proxyStr}
        try:
            response = requests.post(url=url, headers=headers, params=payload, proxies=proxies).json()
        except:
            print('推送失败！')
        if response['ok']:
            print('推送成功！')
        else:
            print('推送失败！')
    except Exception as e:
        print(e)


def send(title, content):
    content += '\n\n开源免费By: https://github.com/curtinlv/JD-Script'
    if TG_BOT_TOKEN and TG_USER_ID:
        telegram_bot(title=title, content=content)
    else:
        print('未启用 telegram机器人')


def main():
    browser = webdriver.Chrome('C:/Python file/Scrapy/chromedriver.exe', options=option)
    try:
        print('本次阅读共有{}篇文章'.format(len(urls)))
        for url in urls:
            print('正在阅读第{}篇文章...'.format(int(urls.index(url)) + 1))
            browser.get(url)
            time.sleep(2)
            ele = browser.find_element_by_id("open_all")
            webdriver.ActionChains(browser).move_to_element(ele).click(ele).perform()  # 点击查看全文
            time.sleep(1)
            height = browser.execute_script("return action=document.body.scrollHeight")  # 获取页面滚动高度
            for i in range(500, height, int(height / random.randint(7, 10))):
                browser.execute_script('window.scrollTo(0,{})'.format(i))
                time.sleep(random.randint(1, 3))
            print('第{}篇文章阅读完毕！'.format(int(urls.index(url)) + 1))
        end_time = time.time()
        print('全部文章阅读完毕！本次阅读共花费{}s!'.format(end_time - begin_time))
        send('###中青助力阅读###', '本次共阅读了{0}篇文章，花费了{1}s！'.format(len(urls), int(end_time-begin_time)))
        browser.close()
    except:
        browser.close()


if __name__ == '__main__':
    main()









