import requests,pymongo
from bs4 import BeautifulSoup
# client=pymongo.MongoClient('localhost',27017)
# dbname=client['rk8']
# dataname=dbname['rk']
urll='http://www.biquku.co/3490/'
req=requests.get(urll)
encode=req.text
xml=BeautifulSoup(encode,'lxml')
a_a=xml.find_all('dd')
lista=[]
dict={}
for dd in a_a:
    lista.append(dd.a['href'])
for a in lista[0:10]:
    req_a=requests.get(urll+a).text
    xml=BeautifulSoup(req_a,'lxml')
    a_aa=xml.find('div',{'id':'content'})
    title=xml.find('h1')
    print(title,a_aa)
    # dict[title.string]=a_aa.get_text()
# dataname.insert(dict)
