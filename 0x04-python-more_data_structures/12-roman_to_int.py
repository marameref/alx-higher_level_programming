#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    if (roman_string is None) or (type(roman_string) is not str):
        return total

    while i in range(len(roman_string)):

        if i == len(roman_string) - 1:
            total += roman[roman_string[i]]
            break

        else:
            if roman[roman_string[i]] < roman[roman_string[i+1]]:
                total += roman[roman_string[i+1]] - roman[roman_string[i]]
                i = i + 1

                if i + 1 == len(roman_string):
                    break

            else:
                total += roman[roman_string[i]]

        i = i + 1

    return total
