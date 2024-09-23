from random import randint
a = [randint(1, 100) for j in range(int(input())) ]
b = []
print(a)

for el in a:
    if el%2==0:
        b.append(el)
print(b)
print(len(b))