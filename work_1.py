print('#1')
arr = ['Рыжая', 'лиса', 'перепрыгнула', 'через', 'забор', '.']
s = ''
for el in arr:
    s += el + ' '
print(s.replace(' .', '.'))

print('\n#2')
for i in range(len(arr)):
    print(str(i) + ' ' + arr[i])

print('\n#3')
s1 = 'Все бобры добры для своих бобрят'
print(s1, s1.replace('б', '1').replace('р', '*'), sep='\n')

print('\n#4')
i = input().replace('[', '').replace(']', '').replace(',', '').split(' ')
ni = []
for el in i:
    ni.append(int(el)**3)
print(ni)

print('\n#5')
s = 'qwertyuiop'
print(
    s[2], 
    s[-1],
    s[:5],
    s[:-1],
    s[::2],
    s[1::2],
    s[::-1],
    s[::-2],
    len(s),
    sep = '\n'
)

print('\n#6')
with open('input.txt', 'r') as r:
    for _ in r:
        arr = _.split(' ')
        intarr = []
        for i in range(1, len(arr)):
            intarr.append(int(arr[i]))
        sa = sum(intarr)/int(arr[0])
        out = ''
        for el in intarr:
            out += str(el) + ' '
        with open('output.txt', 'w') as w:
            w.write(out.replace(str(min(intarr)), str(sa)))
            