with open('input.txt', 'r') as inp:
    for rows in inp:
        row = rows.replace('\n', '').split(' ')
        summary = []
        for el in row:
            if el.isdigit():
                summary.append(int(el))
        if sum(summary)/len(summary) >= 4.5:
            print(row[0], row[1] + ',', 'средний балл:', sum(summary)/len(summary))
