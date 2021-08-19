import csv
data = []

with open('data2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

headers = data[0]
planetdata = data[1:]
for planet in planetdata:
    planet[2] = planet[2].lower()
planetdata.sort(key=lambda planetdata:planetdata[2])
with open('datasorted.csv', 'a+') as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(planetdata)