#!usr/bin/dev python
#-*- coding:utf-8 -*-
'''
分析网页：https://m.weibo.cn/status/4162523210974837

登录的是自己的账号，慎用
'''
import requests
import pandas
import json
import time

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
Cookie = {'cookie':'_T_WM=7c32e70cd9477c13d1d3bedfd16c8899; SUB=_2A2506nBgDeThGedJ71IZ8S_NwjiIHXVUFRAorDV6PUJbkdBeLUjzkW14CHgSOyOKhN1IVxyeMA3Ew0CqpQ..; SUHB=0k1TukqRJbCnaU; SCF=Av9hjtSO90KO2RRuQo6R91vPOpUg87IQVMIGCT4_AlmDvBKMOM3taoTZ4SvB_5JCrOFBEcueNCeLHAu4umgcK0E.; SSOLoginState=1508769840; H5:PWA:UID=1; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3D1076031537790411'}

url = 'https://m.weibo.cn/api/comments/show?id=4162523210974837&page=1'
html = requests.get(url,headers = head,cookies = Cookie)
print(html.status_code)  #200代表请求成功
# print(html.text)
# print(html.content)
# print(html.json())
print(html.json()['data'][0]['id'])
print(html.json()['data'][0]['user']['screen_name'])

ii = 1
while html.status_code == 200:
    ii += 1
    url_next = 'https://m.weibo.cn/api/comments/show?id=4162523210974837&page=' + str(ii)

    try:
        for jj in range(0,len(html.json()['data'])):
            data1 = [(html.json()['data'][jj]['created_at'],
                      html.json()['data'][jj]['user']['screen_name'],
                      html.json()['data'][jj]['source'],
                      html.json()['data'][jj]['text'])]         #列表中加一个小括号，主要是方便pandas转换数据框模式
            data2 = pandas.DataFrame(data1)
            path = r"D:\study_Progame\Python\spider\微博爬虫"
            data2.to_csv(path + r"\weibo_luhan1.csv",header=False,index=False,mode="a")

    except:
        None

    time.sleep(2)

    html = requests.get(url_next,headers = head,cookies = Cookie)




