import re
import csv
detail= ['04日20时,n00,晴,19℃,东南风,<3级,0', '04日23时,n00,晴,17℃,东南风,<3级,0', '05日02时,n00,晴,16℃,东南风,<3级,0', '05日05时,n00,晴,15℃,东南风,<3级,0', '05日08时,d00,晴,19℃,东南风,<3级,2', '05日11时,d01,多云,24℃,东风,<3级,3', '05日14时,d01,多云,26℃,东风,<3级,3', '05日17时,d01,多云,24℃,东风,<3级,3', '05日20时,n01,多云,21℃,东风,<3级,0']


for idx, item in enumerate(detail):
    print (item[idx])
    print ("序号：%s   值：%s" % (idx,item.__len__() ))

   # print(idx)


print(detail[0][0:6])
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

