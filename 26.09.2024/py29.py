with open('countries.txt', 'r') as f:
    countries = dict()
    for row in f:
        countries.update([row.replace('\n', '').split(';')])
    with open('cities.txt', 'r') as w:
        for row in w:
            num, key, city = row.replace('\n', '').split(';')
            print(f"В стране {countries[key]} есть город {city}")
