import csv

data1 = []
data2 = []

with open('datasorted.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data2.append(row)

with open('final.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)

header1 = data1[0]
header2 = data2[0]
pd1 = data1[1:]
pd2 = data2[1:]
headers = header1+header2
planetdata = []
for index, row in enumerate(pd1):
    planetdata.append(pd1[index]+pd2[index])

with open('merged.csv', 'a+') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(planetdata)