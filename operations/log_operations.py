import math

logarythm_ops = {
    'square' : lambda a: a ** 2,
    'pow' : lambda a, b: a ** b,
    'ln' : lambda a: math.log(a),
    'lg' : lambda a: math.log10(a),
    'log' : lambda a, b:  math.log(a, b) # a - number, b - base
    }