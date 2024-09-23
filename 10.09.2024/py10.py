a = set(input().split(' '))
b = set()
for el in a:
    b.add(el)
    a.difference(b)
    if len(b)%2==1:
        print(el, end = ' ')