def spiral(n, m):
    massp = [[0] * m for _ in range(n)]
    
    left, rig, top, bot = 0, m - 1, 0, n - 1
    num = 1
    
    while left <= rig and top <= bot:
        for i in range(left, rig + 1):
            massp[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bot + 1):
            massp[i][rig] = num
            num += 1
        rig -= 1
        
        if top <= bot:
            for i in range(rig, left - 1, -1):
                massp[bot][i] = num
                num += 1
            bot -= 1
            
        if left <= rig:
            for i in range(bot, top - 1, -1):
                massp[i][left] = num
                num += 1
            left += 1
    
    return massp

n, m = int(input()), int(input())
mas = spiral(n, m)
for row in mas:
    for el in row:
        print(el, end = '\t')
    print('\n\n')
