import requests,pymongo
from bs4 import BeautifulSoup
dict={}
client=pymongo.MongoClient('localhost',27017)
dbname=client['one']
dataname=dbname['onedata']


urll='http://xs.sogou.com/chapter/3677306200_120497454983258/'
request=requests.get(urll).text
encode=BeautifulSoup(request,'html.parser')
finda=encode.find('div',{'class':'paper-box paper-article'})
findd=encode.find('div',{'id':'contentWp'})
print(finda.h1.string)
print(findd.get_text())
dict[finda.h1.string]=findd.get_text()
dataname.insert(dict)