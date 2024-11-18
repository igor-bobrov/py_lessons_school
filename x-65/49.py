
import matplotlib.pyplot as plt
import numpy as np

countries = {}
count = {}
reg = {}
cou = {}
r2c = {}
num, names = [], []
num1, names1 = [], []

with open('countries.txt', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        line = f.readline().replace(";", " ").split()
        if not line: break
        countries[line[0]] = line[1]
        count[line[1]] = 0
        cou[line[1]]= 0

with open('cities.txt', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        line1 = f.readline().replace(";", ' ').split()
        if not line1: break
        count[countries[line1[1]]] += 1

with open('regions.txt', 'r', encoding='utf-8') as fl:
    fl.readline()
    while True:
        line2 = fl.readline().split()
        if not line2: break
        reg[line2[0]] = " ".join(line2[1:])

with open('region2country.txt', 'r', encoding='utf-8') as f:
    f.readline()
    while True:
        line3 = f.readline().split()
        if not line3: break
        r2c[line3[0]] = line3[1]

with open('regions.txt', 'r', encoding='utf-8') as fl:
    fl.readline()
    while True:
        line4 = fl.readline().split()
        if not line4: break
        cou[countries[r2c[line4[0]]]] += 1

for coun, val in sorted(count.items(), key=lambda item: -item[1])[:10]:
    names.append(coun)
    num.append(val)

for coun, val in sorted(cou.items(), key=lambda item: -item[1])[:10]:
    names1.append(coun)
    num1.append(val)

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2, 1, 1)
ax1.bar(names[::-1], num[::-1], color='b', alpha=0.5)
ax1.set_ylabel('Значение')
ax1.set_title('Значения по городам')
ax1.set_xticks(range(len(names)))
ax1.set_xticklabels(names[::-1], rotation=45)

ax2 = fig.add_subplot(2, 1, 2)
ax2.bar(names1[::-1], num1[::-1], color='g', alpha=0.5)
ax2.set_ylabel('Значение')
ax2.set_title('Значения по регионам')
ax2.set_xticks(range(len(names1)))
ax2.set_xticklabels(names1[::-1], rotation=45)

plt.tight_layout()
plt.show()
