countries = {}
count = {}
reg = {}
cou ={}
r2c={}
num, names =[],[]
num1, names1 =[],[]
import matplotlib.pyplot as plt
import numpy as np
with open('countries.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while True:
        line = f.readline().replace(";", ' ').split()
        if not line:
            break
        countries[line[0]] = line[1]
        count[line[1]] = 0
with open('cities.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    while True:
        line1 = f.readline().replace(";", ' ').split()
        if not line1:
            break
        count[countries[line1[1]]] +=1
for coun, val in sorted(count.items(), key=lambda item: -item[1])[:10]:
    names.append(coun)
    num.append(val)
    
with open('region2country.txt', 'r', encoding='utf-8') as fl:
    line3 = fl.readline()
    while True:
        line3 = fl.readline().split()
        if not line3:
            break
            r2c[line3[0]] = line3[1]
    with open('regions.txt', 'r', encoding='utf-8') as fa:
        line2 = fa.readline()
        while True:
            line2 = fa.readline().split()
            if not line2:
                break
            reg[line2[0]] = line2[1:]
            cou[line2[1]] = 0
        cou[reg[r2c[line3[1]]]]+=1
for coun, val in sorted(cou.items(), key=lambda item: -item[1])[:10]:
    names1.append(coun)
    num1.append(val)

x_axis=np.arange(10)[::-1]
plt.xticks(x_axis, names, rotation=45)
plt.bar(x_axis, num, align="center", width=0.5, alpha=0.5)
plt.xticks(x_axis, names1, rotation=45)
plt.bar(x_axis, num1, align="center", width=0.5, alpha=0.5)
plt.show()
