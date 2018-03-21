# -*- coding:utf-8 -*-
'''
爬取电影天堂
'''
import requests,re
from pprint import pprint
from pymongo import MongoClient

def mongo_conection(db,collection):
    client = MongoClient("192.168.233.141",27017)
    db = client[db]
    data_collection = db[collection]
    return data_collection


def get_film_list(page):
    response = requests.get("http://www.ygdy8.net/html/gndy/dyzz/list_23_%s.html" % page)
    response.encoding = "gb2312"
    html = response.text
    # print(response.apparent_encoding)
    reg = r'<a href="(.*?)" class="ulink">(.*?)</a>'
    return re.findall(reg,html)

def get_film_content(url):
    response = requests.get(url)
    response.encoding = "gb2312"
    html = response.text
    reg_downloadurl = r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>'
    reg_content = r'<br /><br />(◎.*?)<br /><br /><img'
    reg_fig = r'src="(.*?jpg)"'
    downloadurl = re.findall(reg_downloadurl,html)[0]
    film_content = re.findall(reg_content,html)[0]
    fig_url = re.findall(reg_fig,html)
    # print(downloadurl)          #获取下载地址
    # print(film_content)         #获取电影内容
    # print(fig_url)     #获取电影海报下载地址
    dict1 = {
        "downloadurl":downloadurl,
        "film_content":film_content,
        "fig_url":fig_url,
            }
    return dict1
    # pprint(dict1)




    # pandas.DataFrame.to_csv(r"D:\study_Progame\film.csv",[downloadurl,fig_url,film_content])


if __name__ == '__main__':
    for page in range(1,168):
        try:
            num = 0
            for url_temp, name in get_film_list(page):
                url = r"http://www.ygdy8.net" + url_temp
                dict_content = get_film_content(url)

                collection = mongo_conection("film", "dianyingtiantang")
                collection.insert(dict_content)
                num += 1
                print("正在存储第%s页第%s个电影" % (page, num))
        except:
            pass


