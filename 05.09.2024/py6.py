from random import randint
def pmas (mas):
    for row in mas:
        for el in row:
            print(el,end = ' ')
        print()
b = [[randint(10, 51) for j in range(int(input()))] for i in range(int(input()))]
pmas(b)
print()
for row in b:
    row.insert(0, sum(row))
pmas(b)
b.sort()
print()
pmas(b)
print()
for el in b:
    el.pop(0)
pmas(b)
