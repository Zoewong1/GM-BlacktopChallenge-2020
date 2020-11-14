import csv

data = {}
locations = {}
with open('../chicagoviolations.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if '2019' in row['VIOLATION DATE'] or '2020' in row['VIOLATION DATE']:
            if row['INTERSECTION'] in data:
                if locations[row['INTERSECTION']] == '':
                    locations[row['INTERSECTION']] = row['LOCATION']
                data[row['INTERSECTION']] += int(row['VIOLATIONS'])
            else:
                locations[row['INTERSECTION']] = row['LOCATION']
                data[row['INTERSECTION']] = int(row['VIOLATIONS'])

sorted_data = sorted(data.items(), key= lambda x:x[1],reverse = True)
# print(sorted_data)
first_10 = sorted_data[:10]
for i in first_10:
    print('intersection: ', i[0])
    print('violations: ', i[1])
    print('location: ', locations[i[0]])

print('LOWEST VIOLATIONS')
last_10 = sorted_data[-10:]
for i in last_10[::-1]:
    print('intersection: ', i[0])
    print('violations: ', i[1])
    print('location: ', locations[i[0]])










        


    