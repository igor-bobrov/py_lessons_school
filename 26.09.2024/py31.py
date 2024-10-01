with open('countries.txt', 'r') as f:
    with open('cities.txt', 'r') as w:
        countries = dict()
        s = list()
        for_sort = dict()
        for row in f:
            countries.update([row.replace('\n', '').split(';')])
        for row in w:
            num, key, citys = row.replace('\n', '').split(';')
            s.append(key)
        for key in set(s):
            for_sort.update([(countries[key], s.count(key))])
        for i in sorted(for_sort, key=for_sort.__getitem__):
            print(i, for_sort[i])    
        