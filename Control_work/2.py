import random

matrix = [[random.randint(5, 100) for _ in range(8)] for _ in range(8)]
max_with_7 = None

for row in matrix:
    for num in row:
        if '7' in str(num):
            if max_with_7 is None or num > max_with_7:
                max_with_7 = num

print("Матрица:")
for row in matrix:
    print(row)

if max_with_7 is not None:
    print("max with _ 7:", max_with_7)
else:
    print("no one with _ 7.")
