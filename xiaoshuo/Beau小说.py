import pymongo,requests,re
from bs4 import BeautifulSoup
client=pymongo.MongoClient('localhost',27017)
dbname=client['big']
dataname=dbname['biadata']

urll='http://xs.sogou.com/list/3677306200'
request=requests.get(urll)
r= request.text
soup= BeautifulSoup(r,'html.parser')  #转化成和html格式
file = soup.find_all('a','text-ellips')
str_ll='http://xs.sogou.com/chapter/3677306200'
lista=[]
dict={}
listtitle=[]
for i in file:
    str_href=i.attrs['href']
    file_num=re.sub('/chapter/3677306200','',str_href)
    str_url=str_ll+file_num
    str_title=i.span.string
    lista.append(str_url)
    listtitle.append(str_title)
for a in lista[0:2]:
        request=requests.get(a)
        req=request.text
        html=BeautifulSoup(req,'html.parser')
        content=html.find('div',{'id':'contentWp'})
        title=html.find('div',{'class':'paper-box paper-article'})
        print(title.h1.string)
        print(content.get_text())
        dict[title.h1.string]=content.get_text()
dataname.insert(dict)

