# encoding:utf-8
import re
import requests
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
client = pymongo.MongoClient('localhost', 27017)
database = client['正经']
table = database['小说']
op=webdriver.Chrome()
op.get('http://www.23us.so/files/article/html/11/11798/index.html')
request = requests.get('http://www.23us.so/files/article/html/11/11798/index.html')
request.encoding = request.apparent_encoding
request = request.text
soup = BeautifulSoup(request, 'html.parser')
demo = soup.find_all(class_='L')
for i in demo:
    url = i.a['href']
    request1 = requests.get(url)
    request1.encoding = request1.apparent_encoding
    request1 = request1.text
    req = BeautifulSoup(request1, 'html.parser')
    de = req.find_all('div', id='amain')
    for j in de:
        content = j.find_all('dd', id='contents')
        for i in content:
            data = {
                j.h1.string: i.get_text()
            }
            print(data)

