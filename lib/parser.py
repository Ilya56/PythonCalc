def parser(line: str):

    res = []
    line = line.replace(' ', '')

    if '+' in line:
        a = line.split('+')
        res += ['add', a[0], a[1]]
    elif '-' in line:
        a = line.split('-')
        res += ['sub', a[0], a[1]]
    elif '*' in line:
        a = line.split('*')
        res += ['mul', a[0], a[1]]
    elif '/' in line:
        a = line.split('/')
        res += ['div', a[0], a[1]]
    elif '^' in line:
        a = line.split('^')
        res += ['pow', a[0], a[1]]
    elif 'ln' in line:
        a = line.split('ln')
        res += ['ln', a[1]]
    elif 'lg' in line:
        a = line.split('lg')
        res += ['lg', a[1]]
    elif 'log' in line:
        a = line.split('log')
        a2 = a[1].split(",")
        res += ['log', a2[0], a2[1]]
    return res
