import csv
data = {}
locations = {}
with open('../chicagocrashes.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        try:
            lat = float(row['LATITUDE'])
            lon = float(row['LONGITUDE'])
        except:
            continue
        if '2019' in row['CRASH_DATE'] or '2020' in row['CRASH_DATE']:
            if 'DARKNESS' not in row['LIGHTING_CONDITION']:
                if 'ONE-WAY' not in row['TRAFFICWAY_TYPE']:
                    if 'PARKED MOTOR VEHICLE' not in row['FIRST_CRASH_TYPE']:
                        if 'TRAFFIC SIGNAL' in row['TRAFFIC_CONTROL_DEVICE']:
                            if (round(lat,4),round(lon,4),) in data:
                                data[(round(lat,4),round(lon,4))] += 1
                            else:
                                data[(round(lat,4),round(lon,4),)] = 1

sorted_data = sorted(data.items(), key= lambda x:x[1],reverse = True)
first_10 = sorted_data[:10]
for i in first_10:
    print('location: ', i[0])
    print('crashes: ', i[1])
    