arythm_ops = {
    'add' : lambda a, b: a + b,
    'sub' : lambda a, b: a - b,
    'mul' : lambda a, b: a * b,
    'div' : lambda a, b: a / b if b != 0 else float("Inf") }