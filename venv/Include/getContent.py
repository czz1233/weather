import random
import requests
import socket
import http.client
import pymysql
from bs4 import BeautifulSoup
def getContent(url, data=None):
    #定义头部模拟浏览器
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CH,zh,q=0.8'
    }

    timeout=random.choice(range(80,100))
    while True:
        try:
            rep=requests.get(url,headers=header,timeout=timeout) #请求url，返回response对象
            rep.encoding='utf-8'
            break
        except socket.timeout as e:
            print('3',e)
            timeout.sleep(range(8,15))
        except socket.error as e:
            print('4',e)
            timeout.sleep(range(20,60))
        except http.client.IncompleteRead as e:
            print('5',e)
            timeout.sleep(range(3,15))
        except http.client.BadStatusLine as e:
            print('6',e)
            timeout.sleep(range(30,60))
    print('request success')
    return rep.text #返回文本对象