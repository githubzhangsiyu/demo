import requests, time
from bs4 import BeautifulSoup
from multiprocessing import Pool

url = 'http://maoyan.com/board/'


def open_index(urll):
    req = requests.get(urll)
    if req.status_code == 200:
        req.encoding = req.apparent_encoding
        return req.text
    else:
        print('打开页面出错')


def parser_index(html_index):
    html = BeautifulSoup(html_index, 'html.parser')
    findd = html.find_all('dd')
    for nr in findd:
        img = nr.find('img', {'class': 'board-img'})
        tit = nr.find('p', {'class': 'name'})
        start = nr.find('p', {'class': 'star'})
        sy = nr.find('p', {'class': 'releasetime'})
        img_add=img['data-src']
        title=tit.a.string
        start_name=start.string.strip()
        try:
            sy_time=sy.string
        except:
            print('上映完毕')
        print(title+'\n'+img_add+'\n'+start_name+'\n'+sy_time+'\n\n')



def main(llist):
    html = open_index(url + llist)
    parser_index(html)


if __name__ == '__main__':
    start = time.time()
    lista = ['7', '1', '2', '6']
    list = [x for x in lista]
    pool = Pool()
    pool.map(main, list)
    end = time.time()
    print(end - start)
