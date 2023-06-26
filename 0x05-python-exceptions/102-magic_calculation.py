#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 4):
            result += a**b / i
    except ZeroDivisionError:
        result = a + b
    except Exception:
        result = a * b
    return result
