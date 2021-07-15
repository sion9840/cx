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

years1, values1 = [], []
for i in infectionCount:
    years1.append(i[0])
    values1.append(i[1])

plt.subplot(1, 2, 1)
plt.title('State')
plt.xlabel('date')
plt.ylabel('infection count')
plt.bar(range(dayCount), values1, color = 'r')
plt.plot(range(dayCount), values1, marker = 'o', color = 'b')
plt.xticks(range(dayCount), years1, rotation=45)

years1 = [years1[0]] + years1
values1 = [values1[0]] + values1

values2 = []
years2 = []
values2_max = 0
for i in range(dayCount):
    if values2_max < (values1[i+1] - values1[i]):
        values2_max = values1[i+1] - values1[i]
        values2.append(values2_max)
        years2.append(years1[i+1])

plt.subplot(1, 2, 2)
plt.title('State Increase')
plt.xlabel('date')
plt.ylabel('infection increase')
plt.plot(range(len(values2)), values2, marker = 'o', color = 'g')
plt.xticks(range(len(values2)), years2, rotation=45)

plt.suptitle('CX')
plt.show()