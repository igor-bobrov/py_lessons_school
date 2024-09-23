with open('info.txt', 'r') as info:
    with open('best.txt', 'w') as best:
        for el in info:
            pInfo = el.split(', ')
            st, en = pInfo[1].split(':'), pInfo[2].split(':')
            if (int(en[0])*60 + int(en[1])) - (int(st[0])*60 + int(st[1])) >= 4*60:
                best.write(pInfo[0] + '\n')