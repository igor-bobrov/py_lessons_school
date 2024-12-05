for i in range(489421, 489441):
    l = []
    for j in range(2, i):
        if i%j==0:
            if len(l) > 2:
                break
            l.append(j)
    if len(l) == 2:
        print(1, l[0], l[1], i)