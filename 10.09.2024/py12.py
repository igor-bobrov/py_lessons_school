from random import randint
mas = [randint(0, 11) for _ in range(20)]

print(mas)
print()

for i in range(len(mas) - 1):
    if(mas[i] == mas[i + 1]):
        print(mas[i], end=' ')