# import requests
#
# res = requests.get('http://www.mm131.com/mingxing/')
# print(res.content.decode("gb2312"))



if __name__ == '__main__':
    a,b,c = None,3,4
    temp = [x for x in (a,b,c) if x is not None]
    print(temp)

