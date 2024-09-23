a = int(input())
b = tuple(map(int, input().split(' ')))

if a in b:
    for el in range(list(b).index(a) + 1, len(b)):
        print(list(b)[el], end=' ')
else:
    print(b)

