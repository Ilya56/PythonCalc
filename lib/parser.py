def parser(line: str):

    res = []
    line = line.replace(' ', '')

    if '+' in line:
        a = line.split('+')
        res += ['add', float(a[0]), float(a[1])]
    elif '-' in line:
        a = line.split('-')
        res += ['sub', float(a[0]), float(a[1])]
    elif '*' in line:
        a = line.split('*')
        res += ['mul', float(a[0]), float(a[1])]
    elif '/' in line:
        a = line.split('/')
        res += ['div', float(a[0]), float(a[1])]
    elif '^' in line:
        a = line.split('^')
        res += ['pow', float(a[0]), float(a[1])]
    elif 'ln' in line:
        a = line.split('ln')
        res += ['ln', float(a[1])]
    elif 'lg' in line:
        a = line.split('lg')
        res += ['lg', float(a[1])]
    elif 'log' in line:
        a = line.split('log')
        a2 = a[1].split(",")
        res += ['log', float(a2[0]), float(a2[1])]
    else:
        raise Exception("OperationNotFound")
    return res
