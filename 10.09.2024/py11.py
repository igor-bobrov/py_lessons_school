from random import randint
mas = [randint(0, 20) for _ in range(10)]
print("Массив:", mas)
x = int(input("Что ищем: "))
fi = [i for i, value in enumerate(mas) if value == x]
if fi:
    for index in fi:
        print(f"Нашли: A[{index}]={mas[index]}")
else:
    print("Ничего не нашли.")
