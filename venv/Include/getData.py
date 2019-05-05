'''
获取数据
'''
import bs4
from bs4 import BeautifulSoup

def getData(html_data):
    final=[]
    bs=BeautifulSoup(html_data,"html.parser")
    body=bs.body
    data=body.find('div',{'id':'7d'})
    ul=data.find('ul')
    li=ul.find_all('li')

    for day in li:
        temp=[]
        date=day.find('h1').string
        temp.append(date)
        inf=day.find_all('p')
        weather = inf[0].string
        temp.append(weather)
        tempterature_highest=inf[1].find('span').string
        tempterature_lower=inf[1].find('i').string
        temp.append(tempterature_highest)
        temp.append(tempterature_lower)
        final.append(temp)
    print('getdata success')
    return final