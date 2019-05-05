import sys
import re
import requests
import webbrowser
from PIL import Image
from requests.exceptions import RequestException
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data = {}

with open("weather.csv", 'r', encoding='utf-8') as f:
    rawinfos = list(csv.reader(f))
    for i in rawinfos:
        data[i[0]] = i[1]


def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'}
try:
    address = data['杭州']
except:
    sys.exit("\033[31m无该城市！\033[0m")
html = get_one_page('http://www.weather.com.cn/weather1d/' + address + '.shtml', headers)
if not html:
    print("城市代码有误！")
    exit(1)
ADDRESS = re.findall('<title>(.*?)</title>', html)
aim = re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"', html,
                 re.S)
airdata = re.findall('<li class="li6 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
                     re.S)
print(ADDRESS[0][1:5])
print("当前日期：%s月%s日,%s" % (aim[0][0], aim[0][1], aim[0][4]))
print("更新时间：%s:00" % aim[0][2])
print("当前天气：%s" % aim[0][5])
print("今日温度：%s" % aim[0][6])
print("空气质量：" + airdata[0][0] + "," + airdata[0][2])
#ask_ok = input("是否深入查看（Y/N）：")
# if ask_ok=='Y' or ask_ok=='y':
lightdata = re.findall('<li class="li1 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
                       re.S)
colddata = re.findall('<li class="li2 hot">\n(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', html, re.S)
weardata = re.findall('<li class="li3 hot" id="chuanyi">\n(.*?)<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', html,
                      re.S)
washdata = re.findall('<li class="li4 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
                      re.S)
bloodata = re.findall('<li class="li5 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>', html,
                      re.S)
detail = re.findall('hour3data={"1d":(.*?),"23d"', html, re.S)
detail = re.findall('"(.*?)"', detail[0], re.S)
print("--" * 40)
print('详细数据：')
print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s" % ("时间", "状态", "温度", "风向", "风力"))

# print(detail)

final=[]
rows=[]
lines=[]
for idx, item in enumerate(detail):
    print(item)
    #这是中文逗号，分割的
    temp = re.split('，|。|？', item)
    name=temp[0]
    #这是英文逗号，
    temp2=re.split(',|。|？', name)
    rows.append(temp2[0])
    #除去温度标识
    # print(temp2[3].strip())
    te=temp2[3].strip()
    tem=[x for x in te.split('℃') if x]
    tm=int(tem[0])
   # print(list(filter(None,te.split('℃'))))
    lines.append(tm)
    print(temp2)
    final.append(temp2)
    # temp2=re.split('，|。|？', temp)



    # if item.__len__()==25:
    #     temp.append(detail[idx][0:6])
    #     temp.append(detail[idx][7:10])
    #     temp.append(detail[idx][11:12])
    #     temp.append(detail[idx][13:16])
    #     temp.append(detail[idx][17:19])
    #     temp.append(detail[idx][20:23])
    #     final.append(temp)
    #
    # if item.__len__()==26:
    #     temp.append(detail[idx][0:6])
    #     temp.append(detail[idx][7:10])
    #     temp.append(detail[idx][11:12])
    #     temp.append(detail[idx][14:17])
    #     temp.append(detail[idx][18:20])
    #     temp.append(detail[idx][21:24])
    #     final.append(temp)
    # if item.__len__()==27:
    #     temp.append(detail[idx][0:6])
    #     temp.append(detail[idx][7:10])
    #     temp.append(detail[idx][11:13])
    #     temp.append(detail[idx][14:17])
    #     temp.append(detail[idx][18:20])
    #     temp.append(detail[idx][21:25])

print(final)
print(rows)
print(lines)
with open('D:/test3.csv', 'a', errors='ignore', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(final)


for each in detail:
    each = each.split(',')
    print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s" % (each[0], each[2], each[3], each[4], each[5]))
print("--" * 40)
print("%s:\t%s\t%s" % (lightdata[0][1], lightdata[0][0], lightdata[0][2]))
print("%s:\t%s" % (colddata[0][1], colddata[0][2]))
print("%s:\t%s\t%s" % (washdata[0][1], washdata[0][0], washdata[0][2]))
print("血糖指数:\t%s,%s" % (bloodata[0][0], bloodata[0][2]))
print("%s:\t%s\t%s" % (weardata[0][2], weardata[0][1], weardata[0][3]))
print("--" * 40)
#flag = input("是否查看详细穿衣建议（Y/N）：")
# if flag=='Y' or flag=='y':
#     webbrowser.open("http://www.weather.com.cn/forecast/ct.shtml?areaid="+address)
print("数据来源：中央气象台")

plt.bar(range(len(lines)), lines,color='b',tick_label=rows)
# for x,y in zip(lines,rows):
#     plt.text(x+0.3, y+0.05, '%d' % y, ha='center', va= 'bottom')

plt.show()