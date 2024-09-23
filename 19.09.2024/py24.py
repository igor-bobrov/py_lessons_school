with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as fl:
        for line in f:
            fl.write(str(int(line.strip())**2) + '\n')
