with open('fruit.txt', 'r') as inp:
    arr = []
    for rows in inp:
        row = rows.lower().replace('\n', '').split(' ')
        for el in row:
            arr.append(el)
    fruit = set(arr)
    with open('output.txt', 'w') as out:
        for el in fruit:
            out.write("\"" + str(el) + "\" - " + str(arr.count(el)) + " раз(а)" + '\n')