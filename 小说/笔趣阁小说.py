import requests,pymongo
from bs4 import BeautifulSoup
client=pymongo.MongoClient('localhost',27017)
dbname=client['rk9']
dataname=dbname['rk']
urll='http://www.biquge.co/book/23/23794/'
req=requests.get(urll)
req.encoding=req.apparent_encoding
encode=req.text
html=BeautifulSoup(encode,'lxml')
dd_a=html.find_all('dd')
lista=[]
for a_a in dd_a[:-3]:
    lista.append(a_a.a['href'])


for str_a in lista[0:3]:
    reqq=requests.get(urll+str_a)
    reqq.encoding=reqq.apparent_encoding
    decode=reqq.text
    html=BeautifulSoup(decode,'lxml')
    content=html.find('div',{'id':'content'})
    title=html.find('div',{'class':'bookname'})
    print(title.h1.string)
    print(content.get_text())
    dict={
        title.h1.string:content.get_text()
    }
    dataname.insert(dict)


