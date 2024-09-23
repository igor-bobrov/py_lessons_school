from random import randint

N = int(input())
mas = [randint(0, 101) for _ in range(N)]

print(mas, '\n\n', 'max in list:', max(mas), '<mas> = ', sum(mas)/N)