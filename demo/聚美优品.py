# -*- coding: utf-8 -*-
import pymongo,time
from bs4 import BeautifulSoup
from selenium import webdriver


class Fun():
    def save(self,dict):
        client=pymongo.MongoClient('localhost',27017)
        dbname=client['随便']
        dataname=dbname['聚美优品']
        dataname.insert(dict)
    def start(self):
        url='http://search.jumei.com/?filter=0-11-1&search=%E5%A2%A8%E9%95%9C&from=&cat='
        driver=webdriver.PhantomJS()
        driver.get(url)
        time.sleep(2)
        content=driver.page_source
        html=BeautifulSoup(content,'lxml')
        findd=html.find_all('div',{'class':'products_wrap'})
        print(findd)

        # for i in findd:
        #     img=i.find_all('img',{'height':'255'})
        #     tit=i.find_all('div',{'class':"s_l_name"})
        #     many=i.find_all('div',{'class':'search_list_price'})
        #     for im in img:
        #         self.image=im['original']
        #     for titl in tit:
        #         self.title=titl.get_text().strip()
        #     for j in many:
        #         self.price='￥'+j.span.string+'元'
        #     # [print('￥'+j.span.string) for j in many]
        #     dict={
        #         'title':self.title,
        #         'image':self.image,
        #         'price':self.price
        #     }
        #     self.save(dict)


if __name__ == '__main__':
    stu = Fun()
    stu.start()