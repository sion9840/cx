import csv
import matplotlib.pyplot as plt

f = open(r"C:\Users\user\Desktop\이민승 수학\서울시 코로나19 확진자 현황.csv")
data = list(csv.reader(f))
del data[0]

infectionCount = {}
dayCount = 0

for cell in data:
    date = cell[1]
    year, month, day = map(int, date.split('-'))
    
    if date in infectionCount.keys():
        infectionCount[date] += 1
    else:
        infectionCount[date] = 1

infectionCount = list(infectionCount.items())
infectionCount.reverse()
dayCount = len(infectionCount)

print(infectionCount)

years, values = [], []
for i in infectionCount:
    years.append(i[0])
    values.append(i[1])

plt.bar(range(dayCount), values, color = 'r')
plt.plot(range(dayCount), values, marker = 'o', color = 'b')
plt.xticks(range(dayCount), years)
plt.show()