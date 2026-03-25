#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        current = roman[roman_string[i]]
        next_val = roman.get(roman_string[i + 1], 0) if i + 1 < len(roman_string) else 0
        if current < next_val:
            result -= current
        else:
            result += current
    return result
