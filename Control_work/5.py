mas = input().strip().split(' ')
unic = set(mas)
found = [0 for i in unic]
for i in mas:
    for j in range(len(unic)):
        if i==list(unic)[j]:
            print(i, end = '')
            if found[j] != 0:
                print('_' + str(found[j]), end = '')
            print(end = ' ')
            found[j] += 1
            break