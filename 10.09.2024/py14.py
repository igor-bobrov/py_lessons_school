from random import randint

N = int(input())
mas = [randint(0, 101) for _ in range(N)]

sum1, sum2 = set(), set()

for el in mas:
    if el < 50:
        sum1.add(el)
    else:
        sum2.add(el)

print(mas, '\n\n', '< <50 > ', sum(sum1)/len(sum1), '< >= 50 > ', sum(sum2)/len(sum2))