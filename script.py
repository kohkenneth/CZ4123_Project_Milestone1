# import relevant modules
import csv

# import data from SingaporeWeather csv file
filename = open('SingaporeWeather.csv')
file = csv.DictReader(filename)


# TASK 1 - MEMORY BASED IMPLEMENTATION

# creating tables to store values
id = []
timestamp = []
station = []
temperature = []
humidity = []

fieldnames = file.fieldnames

for col in file:
    id.append(col[fieldnames[0]])
    timestamp.append(col[fieldnames[1]])
    station.append(col[fieldnames[2]])
    temperature.append(col[fieldnames[3]])
    humidity.append(col[fieldnames[4]])

for i in range(len(timestamp)):
    timestamp[i] = timestamp[i].split(" ")[0]

# position arrays to identify data for years 2010 and 2020, Changi, and without empty data
positions = []
for i in range(len(timestamp)):
    if timestamp[i][5:9] in ("2010", "2020") and station[i] == 'Changi':
        positions.append(i)

# new arrays with filtered data
id2 = []
timestamp2 = []
station2 = []
temperature2 = []
humidity2 = []

for i in range(len(positions)):
    id2.append(id[positions[i]])

for i in range(len(positions)):
    timestamp2.append(timestamp[positions[i]])

for i in range(len(positions)):
    station2.append(station[positions[i]])

for i in range(len(positions)):
    temperature2.append(temperature[positions[i]])

for i in range(len(positions)):
    humidity2.append(humidity[positions[i]])

# querying and storing max temp for each month
temp_dict = dict()
for i in range(len(timestamp2)):
    date = timestamp2[i]
    temp = str(date).split('/')
    month_year = (temp[1], temp[2])
    if temperature2[i] != "M":
        if month_year not in temp_dict:
            temp_dict[month_year] = [date, temperature2[i]]
        else:
            if int(float(temp_dict[month_year][1])) < int(float(temperature2[i])):
                temp_dict[month_year] = [date, temperature2[i]]

hum_dict = dict()
for i in range(len(timestamp2)):
    date = timestamp2[i]
    temp = str(date).split('/')
    month_year = (temp[1], temp[2])
    if humidity2[i] != "M":
        if month_year not in hum_dict:
            hum_dict[month_year] = [date, humidity2[i]]
        else:
            if int(float(hum_dict[month_year][1])) < int(float(humidity2[i])):
                hum_dict[month_year] = [date, humidity2[i]]

# storing of data in new arrays to be outputted
hum_result = list(hum_dict.values())
temp_result = list(temp_dict.values())

# creating arrays to store results
results = []
for i in range(len(hum_result)):
    results.append([hum_result[i][0], station2[0],
                    'Max Humidity', hum_result[i][1]])
for i in range(len(temp_result)):
    results.append([temp_result[i][0], station2[0],
                    'Max Temperature', temp_result[i][1]])

print(results)

# output results to csv
with open("ScanResults.csv", 'w', newline="") as f:
    headers = ['Date', 'Station', 'Metric', 'Max Value']
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(results)
