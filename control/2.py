import random

m = [[random.randint(5, 100) for _ in range(8)] for _ in range(8)]
max_with_7 = 0

for row in m:
    for num in row:
        if '7' in str(num):
            if max_with_7 == 0 or num > max_with_7:
                max_with_7 = num
for row in m:
    print(row)
print("max with_7:", max_with_7)

