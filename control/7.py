def mins(file):
    fl = open(file, 'r')
    n = int(fl.readline().strip())
    p, t, r = [], 0, {0: [], 1: [], 2: []}
    for i in range(n):
        p.append(tuple(map(int, fl.readline().strip().split(' '))))
    for a, b in p:
        t += min(a, b)
        r[min(a, b) % 3].append(max(a, b))
    if t % 3 != 0:
        return t
    minr = float('inf')
    for rem in [1, 2]:
        if r[rem]:
            minr = min(minr, min(r[rem]))
    if minr == float('inf'):
        return 
    return t - (t%3) + (minr%3)
print(mins('input.txt'))
