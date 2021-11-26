#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string != None:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        cur = 0
        for i in range(len(roman_string)):
            cur = my_dict[roman_string[i]]
            if cur > prev:
                total += cur - (2 * prev)
            else:
                total += cur
            prev = cur
        return total
    return 0
