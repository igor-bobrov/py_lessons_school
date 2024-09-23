#print('string number %s, or simply %d' % ('as', 1))
#print('string number {}, or simply {}'.format('as', 1))

print('\tF:\tC:')
for i in range(0, 301, 20):
    print('{},\t{}'.format(i, (5*(i+32)/9)))

print('\n\n\tF:\tC:')
for i in range(0, 301, 20):
    print('%6d,\t%8.2f' % ((i, (5*(i+32)/9))))

print('\n\n\tF:\tC:')
for i in range(0, 301, 20):
    print(f'{i:6i},\t{(5*(i+32)/9):8.2f}')



