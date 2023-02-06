import csv

city = input('Enter a city: ')

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file)) # reader provides an iterator
    
print(data)

for row in data[1:]:
    if row[0] == city:
        print(row[1])