print('example 1')
l = str.split(input('print nums: '), ' ')
sum_nums = 0

for el in l:
    sum_nums += int(el)

print(sum_nums)

print('example 2')
l = str.split(input('print nums: '), ' ')
for i in range(1, len(l) - 1 ):
    if l[i] > l[i-1] and l[i] > l[i+1]:
        print(l[i])

print('example 3')
s = input()
print(s.find('bc', s.find('bc') + 1))
