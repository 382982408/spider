#! /usr/bin/env python
#coding:utf-8

'''
参考链接：http://www.jb51.net/article/82105.htm
'''
import urllib
from urllib import request
import re

if __name__ == "__main__":
    #要伪装成的浏览器(我这个是用的chrome)
    headers = ("User-Agent",r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    url = 'http://www.baidu.com'
    opener = urllib.request.build_opener()

    #将要伪装成的浏览器添加到对应的http头部
    opener.addheaders = [headers]

    # 读取相应的url
    data = opener.open(url).read()

    #将获得的html解码为utf - 8
    data = data.decode("utf-8")
    print(data)