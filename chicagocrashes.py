import csv
data = {}
locations = {}
with open('../chicagocrashes.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if '2019' in row['CRASH_DATE'] or '2020' in row['CRASH_DATE']:
            if 'DARKNESS' in row['LIGHTING_CONDITION']:
                if row['STREET_NAME'] in data:
                    if locations[row['STREET_NAME']] == '':
                        locations[row['STREET_NAME']] = row['LOCATION']
                    data[row['STREET_NAME']] += 1
            else:
                locations[row['STREET_NAME']] = row['LOCATION']
                data[row['STREET_NAME']] = 0

sorted_data = sorted(data.items(), key= lambda x:x[1],reverse = True)
first_10 = sorted_data[:10]
for i in first_10:
    print('intersection: ', i[0])
    print('crashes: ', i[1])
    print('location: ', locations[i[0]])