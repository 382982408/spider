#! /usr/bin/dev python
# conding=utf-8

import re

if __name__ == "__main__":
    # 1.判断字符串是否为小写字母
    str1 = "111wqdwqd"
    an = re.match("[a-z]+$",str1)       #match不用谢^边界符，因为match是从开头去查找的
    print(an)
    print(type(an))
    if an:
        print("全是小写")
    else:
        print("不全是小写")

    print("#" * 10,"第二种方法","#" * 10)

    str1 = "111wqdwqd"
    an = re.search("^[a-z]+$",str1)
    print(type(an))
    print(an)
    if an:
        print("全是小写")
    else:
        print("不全是小写")


    print("#" * 10,"第三种方法","#" * 10)

    str1 = "111wqdwqd"
    regex = re.compile("^[a-z]+$")      #编译正则表达式，得到对象，推荐使用，可减少代码量
    an = regex.search(str1)
    print(type(an))
    print(an)
    if an:
        print("全是小写")
    else:
        print("不全是小写")

    print("*" * 10, "任务2", "*" * 10)
    #2.提取分组的字符串
    str2 = '1234214sdadsvfdv234234cadsvcds'
    obj = re.search("([0-9]+)([a-z]+)([0-9]+)([a-z]+)",str2)
    print(obj.group(0))
    print(obj.group(1))
    print(obj.group(2))

    print("*" * 10, "任务3", "*" * 10)
    #2.从字符串中提取邮箱和手机号
    str3 = "sqw13245654545svcsfvzounsheon@126.com"