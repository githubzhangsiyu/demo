# -*- coding: utf-8 -*-
import time, requests, re,os
from bs4 import BeautifulSoup

url = 'http://www.maiziedu.com/course/393'

def save(path,uel):
    if os.path.exists(path):
        dir(path)
        url_u(uel,path)
    else:
        os.makedirs(path)
        url_u(uel,path)
def url_u(urll,path):
    print('-----------------------------')
    for i in urll:
        reqq=requests.get(i).content
        ff=open(path+'1.mp4','wb')
        ff.write(reqq)
        ff.close()
def open_index(url):
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = req.apparent_encoding
        return req.text
    else:
        print('打开网页错误')


def parser_index(values):
    html = BeautifulSoup(values, 'lxml')
    findd = html.find_all('a', {'class': 'font14 color66'})
    return findd


def parser_zi(haha,pathh):
    soup = re.compile('\$lessonUrl = "(.*?)"',re.S)
    s = soup.findall(haha)
    print(s)
    path='D://zjondo-kj/爬虫第二个月/7.4'+pathh[:-5]+'//'
    save(path,s)


def get_url(list):
    for nr in list[:2]:
        urll = url + nr['href']
        title = nr.get_text()
        htmll = open_index(urll)
        parser_zi(htmll,title)


if __name__ == '__main__':
    html = open_index(url)
    content = parser_index(html)
    get_url(content)
