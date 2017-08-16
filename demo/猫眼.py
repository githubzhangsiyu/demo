import requests,os
from bs4 import BeautifulSoup
lista=[]
for i in range(0,100,10):
    urll='http://maoyan.com/board/4'+'?offset='+str(i)
    lista.append(urll)
for j in lista[0:1]:
    req=requests.get(j)
    req.encoding=req.apparent_encoding
    code=req.text
    html=BeautifulSoup(code,'html.parser')
    findd=html.find_all('div',{'class':'board-item-main'})
    img=html.find_all('img',{'class':'board-img'})
    for num,im in enumerate(img):
        gg=requests.get(im['data-src']).content
        path='E://Django4/untitled25/6.15/'+str(num)
        os.makedirs(path)
        _file=open(path+str(num)+'.jpg','wb')
        _file.write(gg)
        _file.close()
    for i in findd:
        tit=i.find('p',{'class':'name'})
        start=i.find('p',{'class':'star'})
        sy=i.find('p',{'class':'releasetime'})
        title=tit.a.string
        startname=start.string.strip()
        shangying=sy.string
        print(title,startname,shangying)











