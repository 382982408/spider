#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/7/8

'''
解析喜马拉雅音频下载（其实就是解析一个json文件）
'''

import json, urllib.request

#解析接口的json
def json_parser():
    file = open("hali_story.json", "r", encoding="utf-8")
    jsonfile = json.load(file)
    for each_music in jsonfile['tracks']:
        url = each_music["play_url"]
        name = each_music["title"]
        download(url=url, name=name)
        print("下载%s成功" % name)

#下载音乐
def download(url, name):
    urllib.request.urlretrieve(url, "./download/%s.mp3" % name)

if __name__ == '__main__':
    json_parser()