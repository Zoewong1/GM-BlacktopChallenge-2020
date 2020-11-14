import csv

d = {}
with open('camtraffic.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file,['x','y','id','count','intnum','location','dis'])
    for row in csv_reader:
        d[row['id']] = (row['x'],row['y'],row['count'],row['intnum'],row['location'],row['dis'])
print(d)
        


    