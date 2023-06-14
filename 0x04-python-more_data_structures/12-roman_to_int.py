def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    n = len(roman_string)

    for i in range(n - 1, -1, -1):
        value = roman_numerals[roman_string[i]]
        if i < n - 1 and value < roman_numerals[roman_string[i + 1]]:
            result -= value
        else:
            result += value

    return result
