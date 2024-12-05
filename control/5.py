mas = input().strip().split(' ')
u = set(mas)
f = [0 for _ in u]
for i in mas:
    for j in range(len(u)):
        if i == list(u)[j]:
            print(i, end = '')
            if f[j] != 0:
                print('_' + str(f[j]), end = '')
            print(end = ' ')
            f[j]+=1
            break