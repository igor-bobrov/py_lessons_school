def unique(a):
    b = {}
    for el in a:
        if el in b:
            b[el] += 1
        else:
            b[el] = 1
    return [el for el in a if b[el] == 1]
a = list(map(int, input().split(' ')))
print(unique(a)) 