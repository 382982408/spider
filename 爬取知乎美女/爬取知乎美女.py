#! usr/bin/dev python
# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import time

print("开始抓取")
url = "https://www.zhihu.com/question/22918070"
html = request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())

#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
links = soup.find_all(name="img",attrs={'class':"origin_image zh-lightbox-thumb",'src':re.compile(".jpg$")})
# print(links)

# 设置保存图片的路径，否则会保存到程序当前路径
path = r'D:\study_Progame\Python\spider\爬取知乎美女\爬取的图片'
num = 1
for link in links:
    # print(link.get("src"))
    # print(type(link))
    # print(link)
    print("开始抓取第%s张…………waiting………………" % num)
    # print(link.attrs['src'])
    # print(time.time())
    # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
    request.urlretrieve(link.attrs['src'], path + r'\%s.jpg' % time.time())
    num += 1
print("抓取完成")