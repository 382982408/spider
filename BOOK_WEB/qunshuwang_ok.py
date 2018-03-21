# -*- coding: utf-8 -*-
import urllib.request#爬虫模块/网页访问模块
import re

def getSortList(sort,page=1):
    res = urllib.request.urlopen('http://www.quanshuwang.com/list/%s_%s.html' %(sort,page))
    html = res.read()#返回的数据编码为gbk
    html = html.decode('gbk')#解码decode 把一种编码转换成unicode
    html = html.encode('utf-8')#编码encode  把unicode转换成另一种编码
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    return re.findall(reg,html)

def getNovelContent(url):
    html = urllib.request.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<div class="b-oper"><a href="(.*?)"'
    url = re.findall(reg,html)[0]
    return url

def getNovelList(url):
    html = urllib.request.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapterList = re.findall(reg,html)
    return chapterList

def getChapterContent(url):
    print(url)
    html = urllib.request.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
    reg = re.compile(reg,re.S)
    return re.findall(reg,html)[0]

for sort in range(1,12):
    for page in range(1,972):
        for name,url in getSortList(page):
            print(name,url)
            novelUrl = getNovelContent(url)
            for chapterUrl,chapterName in getNovelList(novelUrl):
                print(getChapterContent('%s/%s' %(novelUrl,chapterUrl)))


#a = [(1,2),(3,4)]
# a,b = [(1,2),(3,4)]
#易学难精  灵活