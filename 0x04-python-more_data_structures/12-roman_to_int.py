#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str or roman_string is None:
        return 0
    l = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    rev = roman_string[::-1]

    for i in range(len(rev)):
        x = rev[i]
        if i != 0 and l[rev[i - 1]] > l[x]:
            num -= l[x]
        else:
            num += l[x]
    return num
