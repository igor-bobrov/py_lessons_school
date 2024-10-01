def cBalls(a):
    i, cd = 0, 0
    while i < len(a):
        count = 1
        while i + count < len(a) and a[i + count] == a[i]:  count += 1
        if count >= 3:
            cd += count
            a = a[:i] + a[i + count:]
            i = max(0, i - 3)
        else:   i += 1
    return cd
print(cBalls(list(map(int, input().strip().split()))))