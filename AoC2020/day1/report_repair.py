import sys
import os
import re


def solve():
    with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
        numbers = _file.read().split()
    numbers = [int(number) for number in numbers]

    for number1 in numbers:
        for number2 in numbers:
            cand = 2020 - number1 - number2
            if(cand in numbers):
                print(number1 * number2 * cand)
                return


solve()
