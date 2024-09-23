mas = input().split(' ')
minrow = mas[0]
for el in mas:
    if len(el) < len(minrow):
        minrow = el
print(minrow)