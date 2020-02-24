for post in ['', '1', '2', '3', '4', '5', '6']:
    f = open('questions' + post + '.txt', 'r')
    g = open('new_questions' + post + '.txt', 'w')

    ok = True
    for line in f:
        if line[0].isdigit() or line[0] == '*' or line[0] == ' ' or line[0] == '\n':
            while len(line) > 1 and (line[-2] == ' ' or line[-2] == '.'):
                line = line[:-2] + '\n'
            if line != '\n' or ok:
                g.write(line)
            ok = line != '\n'

    f.close()
    g.close()

    f = open('new_questions' + post + '.txt', 'r')
    g = open('questions' + post + '.txt', 'w')

    for line in f:
        g.write(line)

    f.close()
    g.close()
