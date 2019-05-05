import sys
sys.path.append('../')
from getContent import getContent
from getData import getData
from writeData import writeData
if __name__=='__main__':
    url='http://www.weather.com.cn/weather/101210101.shtml'
    #添加url
    html=getContent(url)
    #获取数据
    result=getData(html)

    writeData(result,'D:/weather.csv')
    print('mytest')