import csv

data = {}
locations = {}
with open('../chicagoviolations.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file,['intersection','cameraid','adress','date','violations','x','y','lat','lon','loc'])
    for row in csv_reader:
        if '2019' in row['date'] or '2020' in row['date']:
            if row['intersection'] in data:
                if locations[row['intersection']] == '':
                    locations[row['intersection']] = row['loc']
                data[row['intersection']] += int(row['violations'])
            else:
                locations[row['intersection']] = row['loc']
                data[row['intersection']] = int(row['violations'])

sorted_data = sorted(data.items(), key= lambda x:x[1],reverse = True)
first_10 = sorted_data[:10]
for i in first_10:
    print('intersection: ', i[0])
    print('violations: ', i[1])
    print('location: ', locations[i[0]])





        


    