#! usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request   #爬虫模块or网页访问模块
import re
import time
import os
import chardet
# import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

relative_url = "http://jnhcm.com"
def getSortList(tag,page):
    req = urllib.request.Request("http://jnhcm.com/list/%s_%s.html" % (tag,page),headers=headers)
    # req = requests.get("http://www.6v6v.cn/list/1_0.html",headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    # html = html.decode("gbk")       #可有查看源代码charset=gbk
    html = html.decode("utf-8")
    # html = html.encode("utf-8")
    # print(html)
    reg = r'title="(.*?)" href="(.*?)"'
    # print(re.findall(reg,html))
    return re.findall(reg,html)         #返回值[('我们真的爱过吗？', '/book_1601.html'), ('女孩，别低头，王冠会掉', '/book_1600.html'),……]


def getNovelContent(book_url):
    req = urllib.request.Request(book_url,headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    reg = r'<a href="(.*?)" class="reader"'
    return "".join(re.findall(reg,html))                 #返回值例如['/book/1/281/']

def getChapterUrl(novelUrl):
    req = urllib.request.Request(novelUrl, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    reg = '<li><a href="(.*?)" title="(.*?)"'
    ChapterUrlList = []
    for i in re.findall(reg,html):
        ChapterUrlList.append(("http://jnhcm.com" + i[0],i[1]))
    return ChapterUrlList
    # for chapterUrl,chapterName in re.findall(reg,html):
    #     return (chapterName,"http://jnhcm.com" + chapterUrl)          #不能在这里遍历，要不然不能全部数据返回，一般要求整体返回

def getAllToList():
    for name,book_url_temp in getSortList(tag,page):
        book_url = 'http://jnhcm.com' + book_url_temp
        # print(name,book_url)
        time.sleep(5)
        novelUrl = relative_url + getNovelContent(book_url)
        # print(novelUrl)
        time.sleep(5)
        for chapterUrl,chapterName in getChapterUrl(novelUrl):
            # print("章节地址：%s,章节名字%s" % (chapterUrl,chapterName))
            try:
                list_temp = [name,chapterUrl,chapterName]
                time.sleep(3)
                chapter_content = decodeChapterUrl(list_temp[1])
                # return name,chapter_content,chapterName
                if os.path.isdir(r"D:\study_Progame\Python\spider\全书网\%s" % name):
                    pass
                else:
                    os.mkdir(r"D:\study_Progame\Python\spider\全书网\%s" % name)
                    path = r"D:\study_Progame\Python\spider\全书网\%s" % name
                with open(path + "\%s.txt" % chapterName,"w") as txt_file:
                    txt_file.write(chapter_content)
                print("save 书名 %s----章节%s----成功" % (name,chapterName))
            except:
                continue

def decodeChapterUrl(ChapterUrl):
    req = urllib.request.Request(ChapterUrl, headers=headers)

    html = urllib.request.urlopen(req).read()
    charset_info = chardet.detect(html[0:7000])
    print(charset_info)
    try:
        html = html.decode(charset_info["encoding"])
        reg = 'id="content">(.*)<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;'
        novel_content_temp = "".join(re.findall(reg,html))
        novel_content = novel_content_temp.replace("&nbsp;"," ").replace("<br />","\n")
    except:
        None
    finally:
        return novel_content


if __name__ == "__main__":
    for tag in range(1,12):
        for page in range(0,50):            #应该打印tag和page
            try:
                getAllToList()
            except:
                continue

