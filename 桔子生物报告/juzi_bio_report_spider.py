#! usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2018/3/20

__author__ = "zhangxiong"

import requests,json,lxml,pandas
import pickle
from bs4 import BeautifulSoup
from pprint import pprint

def content_list():
    req = requests.get("http://www.juzisw.com/u/jay/search_pro_index.json?_=1521550202521")
    content = req.text

    # 返回数据为字典
    con_dict = json.loads(content)
    test_project = con_dict['pageIndex']

    #存储为pickle，方便后期再次使用（load），注意dump和dumps的用法，注意load和loads的用法
    with open(r"temp_file/test_project.pkl", "wb") as f:
        pickle.dump(test_project, f)

    # 数据结构 {'1': {'path': '521.html', 'title': '丙肝治疗反应', 'level': '1.22'},……}
    # print(test_project)
    return test_project

def single_page_spider(path):
    url = "http://www.juzisw.com/u/jay/%s" % path
    req = requests.get(url=url)

    #用自带的decode解析不了
    # print(req.content.decode("utf-8"))

    #在这里也可以用自带的html.parser来解析，不过lxml会快很多
    soup = BeautifulSoup(req.content, "lxml", from_encoding="utf-8")
    # print(soup.prettify())

    #查找tag = section下所有p标签
    final_p = soup.section.find_all("p")
    #定义一个空字符串，方便去掉标签（.string）之后拼接
    result = ""
    for each in final_p:
        result += each.string

    print(result)
    return result

def process():
    test_project = content_list()

    num = 1
    final_result = []
    for each_project in test_project.values():
        try:

            path = each_project["path"]
            # name_project = each_project["title"]
            # chapter_project = each_project["level"]
            description = single_page_spider(path=path)
            each_project["description"] = description

            #字典内key值改名
            each_project["chapter"] = each_project.pop("level")
            each_project["name"] = each_project.pop("title")
            each_project["path"] = "http://www.juzisw.com/u/jay/" + each_project["path"]

            final_result.append(each_project)

            print("正在爬取第%s个检测项目……………………" % num)

            # pprint(each_project)
            num += 1

            dataBeforePandas = [(each_project["name"], each_project["chapter"], each_project["path"], each_project["description"])]
            data = pandas.DataFrame(dataBeforePandas)
            data.to_csv("temp_file/final_result.csv", header=False, index=False, mode="a+", encoding="utf-8")

        except:
            continue
    # 存储为pickle，方便后期再次使用
    with open(r"temp_file/final_result.pkl", "wb") as fp:
        pickle.dump(final_result, fp)


if __name__ == '__main__':
    process()
    print("…………………………spider finished…………………………")
