#!usr/bin/dev python
#-*- coding:utf-8 -*-

'''
Created by zhangxiong,
2017年10月28日22:53:32
version：V1.0
'''
print "This is a software for signature design.\n"
print "NOTICE:Do not use it for commercial or business purpose. Just for learning and communication only!\n"
print "#"*100
print "Any question, please sent me emails to contact. [zounsheon@126.com]\n"
print "#"*100
print "Processing and Please Waiting for several seconds" + "..." * 300

from Tkinter import *
import tkMessageBox
import requests,re,urllib,urllib2,os

def spider(name):
    # data = r"id=%E5%BC%A0%E9%9B%84&idi=jiqie&id1=1502&id2=905&id3=%23FF0000&id4=%23FFFF00&id5=0&id6="
    data = {
        'id':name,
        'idi':'jiqie',
        'id1':'1502',
        'id2':'905',
        'id3':'# FF0000',
        'id4':'# FFFF00',
        'id5':'0',
        'id6':''
    }
    res = requests.post(url="http://www.jiqie.com/a/re19.php",data=data)
    contend = res.content
    reg = '<img src="\.\./(i/.*?)">'
    design_img_link = "http://www.jiqie.com/" + re.findall(reg,contend)[0]
    # print design_img_link
    # urllib.urlretrieve(design_img_link,name + ".gif")             #这种下载方式打不开,原因是默认方式为post请求，改为requests的get请求就好了，详情见http://blog.csdn.net/dkcgx/article/details/46966503
    with open(name + ".gif","wb") as imgFile:
        response = requests.get(design_img_link)
        imgFile.write(requests.get(design_img_link).content)

def design():
    name = e1.get()
    # if e1.get() =="":
    if not name:
        tkMessageBox.showinfo("出错了","请输入姓名")
    else:
        spider(name)
        img_exhibition(name=name)
        top.protocol("WM_DELETE_WINDOW", ask_quit)              #在关闭时继续执行，激发任务，即将产生的临时文件删除
        print "Design successfully!Have fun!"

def img_exhibition(name):
    photo = PhotoImage(file=name + ".gif",width="500",height="200")
    # print type(photo)
    a_img = Label(image=photo)
    a_img.image = photo
    a_img.grid(row=0,column=10)

def ask_quit():
    name = e1.get()
    if tkMessageBox.askyesno("Tip", "确定要退出吗？您可在退出之前保存您的签名文件（位于当前目录），否则退出后签名文件将会自动删除！！！"):
        top.quit()
        os.remove(name + ".gif")



top = Tk()
top.title("签名设计")
# top.geometry("500x300-800-400")
# top.geometry("230x50-800-400")
top.geometry("+600+400")
top.resizable(width=False,height=False)
a1 = Label(top,text="姓名：")              #创建标签组件
a1.grid(row=0,column=0)

a2 = Label(top,text="Created by ZX")
a2.grid(row=2,column=1)

e1 = Entry(top)
e1.grid(row=0,column=1)

b1 = Button(top,text="设计",command=design)          #给个事件，可以用command，回调函数,函数不加括号,点击即触发函数运行
b1.grid(row=0,column=5)


top.mainloop()  # 不能提前到“标签”前，个人理解可以看做是一个循环