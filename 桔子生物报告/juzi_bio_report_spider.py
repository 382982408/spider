#! usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/3/20

__author__ = "zhangxiong"

import requests,json,lxml
import pickle
from bs4 import BeautifulSoup
from pprint import pprint

def content_list():
    req = requests.get("http://www.juzisw.com/u/jay/search_pro_index.json?_=1521550202521")
    content = req.text
    # 返回数据为字典
    con_dict = json.loads(content)
    test_project = con_dict['pageIndex']
    #将文件存储为pickle，方便后期再次使用（load），注意dump和dumps的用法，注意load和loads的用法
    with open(r"temp_file/test_project.pkl", "wb") as f:
        pickle.dump(test_project, f)
    return test_project

def single_page_spider():
    url = "http://www.juzisw.com/u/jay/410.html"
    req = requests.get(url=url)

    #用自带的decode解析不了
    # print(req.content.decode("utf-8"))

    #在这里也可以用html.parser来解析，不过lxml会快很多
    soup = BeautifulSoup(req.content, "lxml", from_encoding="utf-8")
    # print(soup.prettify())
    final_p = soup.section.find_all("p")

    print(final_p.string)

if __name__ == '__main__':
    single_page_spider()
