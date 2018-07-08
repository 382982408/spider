#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/14

'''
自己搭建的网站：http://118.24.53.210/
网页采用不蒜子自动进行网页访问计数
http://geekerwang.com/2016/09/01/HTTP请求刷不蒜子PV/
'''

import requests
import threading


#请求我自己的网站
def access_mysite():
    url = "http://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_301609348665"
    headers = {'Referer': 'http://118.24.53.210/'}
    req = requests.get(url=url, headers=headers)
    print(req)

#请求朋友博客
def access_superchao():
    url = "https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_1026792773208"
    headers = {'Referer': 'https://superman-wrdh.github.io/'}
    req = requests.get(url=url, headers=headers)
    print(req)

def add_count():
    n = 0
    for i in range(1000):
        access_superchao()
        n += 1
        print(n)

if __name__ == '__main__':
    threads = []
    for i in range(4):
        t = threading.Thread(target=add_count, name="hechao"+str(i))
        threads.append(t)
    for thread in threads:
        thread.start()
    thread.join()
    print("all done.")