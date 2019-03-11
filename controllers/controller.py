from lib import parser

from operations import log_operations, simple_operations

operations = {}
operations.update(log_operations.logarythm_ops)
operations.update(simple_operations.arythm_ops)


def calculate(line: str):
    expression = parser.parser(line)
    action = expression.pop(0)
    return operations[action](*expression)
