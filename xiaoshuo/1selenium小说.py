import requests,pymongo
from bs4 import BeautifulSoup
# client=pymongo.MongoClient('localhost',27017)
# dbname=client['rk9']
# dataname=dbname['rk']
# urll='http://www.biquge.co/book/23/23794/'
# req=requests.get(urll)
# req.encoding=req.apparent_encoding
# encode=req.text
# html=BeautifulSoup(encode,'lxml')
# dd_a=html.find_all('dd')
# lista=[]
# for a_a in dd_a[:-3]:
#     lista.append(a_a.a['href'])
# for str_a in lista[0:5]:
#     reqq=requests.get(urll+str_a)
#     reqq.encoding=reqq.apparent_encoding
#     decode=reqq.text
#     html=BeautifulSoup(decode,'lxml')
#     content=html.find('div',{'id':'content'})
#     title=html.find('div',{'class':'bookname'})
#     print(title.h1.string)
#     print(content.get_text())
#     dict={
#         title.h1.string:content.get_text()
#     }
#     dataname.insert(dict)
# from selenium import webdriver
# op=webdriver.Chrome()
# op.get('http://www.23us.com/html/55/55519/')
#
# urll='http://www.23us.com/html/55/55519/'
# req=requests.get(urll)
# req.encoding=req.apparent_encoding
# code=req.text
# html=BeautifulSoup(code,'html.parser')
# finda=html.find_all('td',{'class':"L"})
# lista=[]
# for i in finda[:-3]:
#     lista.append(i.a['href'])
# for io in lista[0:10]:
#     reqq=requests.get(urll+io)
#     reqq.encoding=reqq.apparent_encoding
#     codee=reqq.text
#     html=BeautifulSoup(codee,'html.parser')
#     cont=html.find('dd')
#     title=html.find('dd',{'id':"contents"})
#     print(cont.h1.string)
#     print(title.get_text())
  def parse(self, response):
        for i in range(1,6):
            uu = self.start_urls[0].format(q=str(i))
            yield scrapy.Request(uu,callback=self.comment_content)
  def comment_content(self,response):
        urll = json.loads(response.text)
        a = urll['data']['commentList']
        for k in a:
            name=k['author']
            data=k['date']
            cont=k['content']
            print(name,data,cont)
            item = QunawangItem(name=name,data=data,content=cont)
            yield item

