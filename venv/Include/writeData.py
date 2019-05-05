import csv

def writeData(data,name):
    with open(name,'a',errors='ignore',newline='') as f:
        f_csv=csv.writer(f)
        f_csv.writerows(data)
    print('weite_csv success')
