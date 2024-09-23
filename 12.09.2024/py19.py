orig = input()
for i in range(0, len(orig)-1, 2): 
    print(orig[i+1], orig[i], end='', sep='')   
if(len(orig)%2!=0):
    print(orig[len(orig)-1])

