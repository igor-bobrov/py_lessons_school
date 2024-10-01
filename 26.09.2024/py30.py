with open('countries.txt', 'r') as f:
    with open('cities.txt', 'r') as w:
        countries = dict()
        s = list()
        for row in f:
            countries.update([row.replace('\n', '').split(';')])
        for row in w:
            num, key, citys = row.replace('\n', '').split(';')
            s.append(key)
        for key in set(s):
            print(f"В {countries[key]} есть {s.count(key)} городов")
        
            