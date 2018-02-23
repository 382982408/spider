# -*-encoding:utf-8-*-
import requests
import urllib.request
from pyquery import PyQuery as pq
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}


def get_html_img(url):
    response = requests.get(url=url, headers=headers)
    html = response.text
    doc = pq(html)
    items = doc("img")
    result = []
    for item in items:
        doc = pq(item)
        src = doc.attr("src")
        if src.startswith("http"):
            result.append(src)
    return result


def get_img_name(url):
    if url.count('/') == 0:
        return url
    else:
        index = url.rindex('/')
        return url[index:len(url)]


def download_img_from_url(url, save_path):
    imgs = get_html_img(url)
    flag = False
    for i in imgs:
        # req = requests.get(i,headers=headers)                 #不知道为什么不行
        req = urllib.request.Request(url=i, headers=headers)        #为什么不用requests请求
        name = get_img_name(i)
        file = open(save_path + name, 'wb')
        try:
            file.write(urllib.request.urlopen(req).read())
        except Exception as e:
            flag = True
            print('download img  %s  failed ' % i)
        file.close()
        if not flag:
            print('download img  %s  successful ' % i)
        else:
            import os
            os.remove(save_path + name)


if __name__ == '__main__':
    download_img_from_url(url="http://www.meizitu.com/a/1.html", save_path=r"D:\study_Progame\Python\spider\妹子网\何超")