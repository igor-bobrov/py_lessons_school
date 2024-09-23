a = [int(s) for s in input().split()]

print(a)
minNum = min(a)
maxNum = max(a)
minNumI = a.index(minNum)
maxNumI = a.index(maxNum)

a.remove(minNum)
a.remove(maxNum)

a.insert(minNumI, maxNum)
a.insert(maxNumI, minNum)

print(a)