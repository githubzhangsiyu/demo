#encoding=utf-8
import requests,pymongo
from bs4 import BeautifulSoup
client=pymongo.MongoClient('localhost',27017)
dbname=client['链家']
dataname=dbname['链家信息']
lista=[]#链接列表
listpage=[]#页数列表
imgsrc=[]#图片列表
urll='https://bj.lianjia.com/ershoufang/'
for page in range(1,101):
        listpage.append(urll+'pg'+str(page)+'/')#拼合100页的链接
for one in listpage[0:1]:#获取第一页的所有内容
    req=requests.get(one)#打开链接
    req.encoding=req.apparent_encoding#改写编码
    code=req.text#读出文件
    html=BeautifulSoup(code,'lxml')#解析网页
    findd=html.find_all('div',{'class':'info clear'})#过滤进入内容
    for con in findd:#循环内容列表
        a_a=con.a['href']#获取所有链接
        gz=con.find('div',{'class':'followInfo'})#过滤关注人
        gzr=gz.get_text()#得到关注人
        title=con.a.string#获取标题
        req=requests.get(a_a)#打开网址
        req.encoding=req.apparent_encoding#改写编码
        code=req.text#读出文件
        html=BeautifulSoup(code,'lxml')#解析网页
        finda=html.find('ul',{'class':"smallpic"})#过滤网页中图片
        for i in finda:
            #获取子页面的图片
            imgsrc.append(i.img['src'])
        #创建字典
        dict={
            'title':title,
            'gzr':gzr,
            'img':imgsrc
        }
        dataname.insert(dict)#插入字典
        print('下一页')