# +, -, /, *
def parser(line: str):
    res = []
    plus = '+'
    minus = '-'
    mul = '*'
    div = '/'

    if plus in line:
        a = line.split(plus)
        res += ['add', a[0], a[1]]
    elif minus in line:
        a = line.split(minus)
        res += ['sub', a[0], a[1]]
    elif mul in line:
        a = line.split(mul)
        res += ['mul', a[0], a[1]]
    elif div in line:
        a = line.split(div)
        res += ['div', a[0], a[1]]
    return res

if __name__ == '__main__':
    print(parser("2+2"))
    print(parser("2-2"))
    print(parser("2*2"))
    print(parser("2/2"))
    print(parser("45-2"))
    print(parser("2/8"))

