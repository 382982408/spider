import time
import requests
import json
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = "http://www.meizitu.com/a/1.html"
html = requests.get(url=url,headers=headers)

soup = BeautifulSoup(html.content,"html.parser")          #用lxml解析不全，原因见https://segmentfault.com/q/1010000006871106/a-1020000006872334
links = soup.find_all("img",{"class":"scrollLoading","src":re.compile(".jpg$")})        #参考爬取知乎美女.py
# print(links)
path = "D:\study_Progame\Python\spider\妹子网\img"
for link in links:
    with open("D:\study_Progame\Python\spider\妹子网\img\link.txt","a",encoding="utf-8") as file:
        file.write(str(link['src']) + "\n")
    # print(link['src'])      #或者通过.attrs['src']取，参考爬取知乎美女.py和http://blog.csdn.net/zjiang1994/article/details/52679174
    # link_ag = requests.get(url=link,headers=headers)
    # urllib.request.urlretrieve(link_ag, path + r'\%s.jpg' % time.time())
# print(html.content)
ii = 0
num = 1
while True:

    ii += 1
    url_next = "http://www.meizitu.com/a/" + str(ii) + ".html"
    html = requests.get(url=url_next, headers=headers)
    print(html.status_code)
    soup = BeautifulSoup(html.content,
                         "html.parser")  # 用lxml解析不全，原因见https://segmentfault.com/q/1010000006871106/a-1020000006872334
    links = soup.find_all("img", {"class": "scrollLoading", "src": re.compile(".jpg$")})  # 参考爬取知乎美女.py
    # print(links)
    for link in links:
        with open("D:\study_Progame\Python\spider\妹子网\img\link.txt", "a", encoding="utf-8") as file:
            file.write(str(link['src']) + "\n")

        try:

            response = urllib.request.Request(link['src'],headers=headers)
            print(link['src'])
        finally:
            fileImg = open("D:\study_Progame\Python\spider\妹子网\img\%s.jpg" % num, "wb")
            fileImg.write(urllib.request.urlopen(response).read())
        # urllib.request.urlretrieve(response,"D:\study_Progame\Python\spider\妹子网\img\%s.jpg" % num)
        print("正在保存第%d张" % num)
        num += 1
        time.sleep(2)
#
#
#
    html = requests.get(url=url_next,headers=headers)
#
    time.sleep(5)