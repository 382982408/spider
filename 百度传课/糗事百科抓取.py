#!usr/bin/dev python
#coding=utf-8


import urllib
from urllib import request
import re
from bs4 import BeautifulSoup

print("爬取开始……")
for page in range(1,200):
    print("正在爬取第%s页" % page)
    #1.访问其中一个网页地址，获取网页源代码
    url = "https://www.qiushibaike.com/8hr/page/" + str(page) +"/"
    headers = ("User-Agent",r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    openner = urllib.request.build_opener()

    openner.addheaders = [headers]
    data = openner.open(url).read()
    contend = data.decode("utf-8")
    # print(contend)

    #1.提取数据
    regex = re.compile('<span>\n\n\n(.*)</span>+?',re.S)
    text = re.findall(regex,contend)
    # text = regex.findall(contend)         #这个方法好像也可以
    # print(text[0])


    #用beautifulsoup,参考http://www.jianshu.com/p/154211515a41

    soup = BeautifulSoup(contend,"lxml")
    # head = soup.title
    # print(soup.prettify())  #格式化输出，以缩进格式输出
    # print(soup.title.string)  #加上string，输出了HTML中标签的文本内容
    # for i in soup.find_all("div"):
    #     print(i.name)
    '''CSS选择器'''
    yuchuli = (soup.select('div[class="content"] > span'))
    print(yuchuli[0])

    for i in yuchuli:
        print(type(i))    #测试了一下   返回是一个tag的类，所以猜测可以用.string
        # print(i.string)
        with open(r"D:\study_Progame\testfile\spider_jiushibaike\%s.txt" % page, "a",encoding="utf-8") as file:
            file.write(str(i.string))
print("爬取完毕，good luck！")
