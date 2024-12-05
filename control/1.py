import random

array = [random.randint(-500, 500) for _ in range(25)]
ne = [num for num in array if num < 0]
cn = len(ne)
av = sum(ne) / cn if cn > 0 else 0

print("mas:", array, "\notr:", cn, "\navar:", av)
