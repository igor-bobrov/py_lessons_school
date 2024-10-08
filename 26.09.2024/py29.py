with open('countries.txt', 'r') as f:
    countries = dict()
    for row in f:
        countries.update([row.replace('\n', '').split(';')])
    with open('cities.txt', 'r') as w:
        for row in w:
            num, key, city = row.replace('\n', '').split(';')
            print(f"В стране {countries[key]} есть город {city}")
03.10.2024/dict_complete_data.ods 03.10.2024/py32-34.py 03.10.2024/py35.py