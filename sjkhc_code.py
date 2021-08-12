##京东手机狂欢城获取助力码
##版本：v1.0
##author:lyx98

#!/bin/env python3
# -*- coding: utf-8 -*

import os
import re
import time
import json
from telethon import TelegramClient


root_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]


def api_info():
    api_file = root_path + '/config/bot.json'
    with open('{}'.format(api_file), 'r', encoding='utf-8') as f:
        api_dict = json.loads(f.read())
        f.close()
        api_id = api_dict['api_id']
        api_hash = str(api_dict['api_hash'])
        return [api_id, api_hash]


def send_code(code):
    api_id = api_info()[0]
    api_hash = api_info()[1]
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message('@guaguagua_bot', 'gua-submit_codes carnivalcity {}'.format(code)))


def main():
    code_list = []
    target_path = root_path + '/log/shufflewzc_faker2_jd_carnivalcity_help'
    filename_list = os.listdir(target_path)
    filename_list = sorted(filename_list, key=lambda x: os.path.getmtime(os.path.join(target_path, x)))
    target_file = target_path + '/' + filename_list[-1]
    print(target_file)
    if os.path.exists(target_path):
        with open("{}".format(target_file), 'r', encoding='utf-8') as f:
            line_list = f.readlines()
            f.close()
            for keyword in line_list:
                result = re.findall('京东手机狂欢城助力好友互助码】(.*)\n', keyword)
                if len(result) > 0:
                    code_list.append(result[0])
            codes = '&'.join(code_list)
            send_code(codes)


if __name__ == '__main__':
    main()




