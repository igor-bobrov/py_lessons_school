print('*', end='')
for i in range(1, 11):
    print('\t{0:4d}:'.format(i), end='')
print('\n')
for i in range(1, 11):
    print('{}:\t'.format(i), end='')
    for j in range(1, 11):
        print("{0:4d}\t".format(i*j), end='')
    print()
