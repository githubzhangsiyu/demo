from selenium import webdriver
from bs4 import BeautifulSoup
import time,csv

url = 'http://finance.sina.com.cn/data/#stock?qq-pf-to=pcqq.group'
driver = webdriver.PhantomJS()
driver.get(url)
driver.find_element_by_xpath('//*[@id="numberDiv_0"]/a[3]').click()
time.sleep(5)
title_list = ['代码','名称','最新价','涨跌额','涨跌幅','买入','卖出','昨收','今开','最高','最低','成交量','成交额']
big_list = []
for i in range(3):
    _text = driver.page_source
    soup = BeautifulSoup(_text,'lxml')
    content = soup.select('#block_1 > tbody > tr')
    for tr in content:
        per_list = []
        for j in range(13):
            td = tr.find_all('td')[j].get_text()
            per_list.append(td)
        big_list.append(per_list)
    driver.find_element_by_xpath('//*[@id="pageDiv_0"]/span[3]').click()
    time.sleep(5)
with open('gupiao.csv','w+',newline='') as datacsv:
    csvfile = csv.writer(datacsv,dialect='excel')
    csvfile.writerow(title_list)
    for i in big_list:
        csvfile.writerow(i)

