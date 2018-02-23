#_*_encoding=utf-8*_*

import requests
import json
import pandas

def getAndSave(page):
    url = r"https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv54014&productId=4675712&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1" % page
    html = requests.get(url=url)
    text = html.text.strip("b'fetchJSON_comment98vv54014(").strip(");")
    for id in range(10):
        comments = json.loads(text)["comments"][id]["content"]       #转json
        productColor = json.loads(text)["comments"][id]["productColor"]
        productSize = json.loads(text)["comments"][id]["productSize"]
        userLevelName = json.loads(text)["comments"][id]["userLevelName"]
        creationTime = json.loads(text)["comments"][id]["creationTime"]
        userClientShow = json.loads(text)["comments"][id]["userClientShow"]
        try:
            afterUserComment = json.loads(text)["comments"][id]["afterUserComment"]["hAfterUserComment"]["content"]
        except:
            afterUserComment = str("")
        # finally:
            # print(productColor)
            # print(afterUserComment)
        dataBeforePandas = [(comments,creationTime,userClientShow,productSize,productColor,userLevelName,afterUserComment)]
        data = pandas.DataFrame(dataBeforePandas)
        path = r"D:\study_Progame\Python\spider\京东评论爬虫"
        data.to_csv(path + r"\ipad2017comments.csv",header=False,index=False,mode="a")
        print("正在保存第%s页第%s个评论" % (page, id))
def spider():
    for page in range(1,999):
        try:
            getAndSave(page)
        except:
            continue
def findPrice():            #从爬取的评论中，找到与价格相关的评论
    with open(r"D:\study_Progame\Python\spider\京东评论爬虫\ipad2017comments.csv","r") as commentsfile:
        for readline in commentsfile:
            for word in readline:
                if "元" == word or "钱" == word or "块" == word:
                    wordIndex = readline.index(word)
                    price = readline[wordIndex - 5 : wordIndex + 5]
                    print(price)

if __name__ == '__main__':
    findPrice()