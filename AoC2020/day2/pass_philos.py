import sys
import os
import re


def check(line):
    rule_letter, code = line.split(': ')
    rule, letter = rule_letter.split()
    lower_limit, upper_limit = rule.split('-')
    letter_count = code.count(letter)
    return letter_count in range(int(lower_limit), int(upper_limit) + 1)


def check2(line):
    rule_letter, code = line.split(': ')
    rule, letter = rule_letter.split()
    index1, index2 = rule.split('-')
    return (code[int(index1)-1] == letter) ^ (code[int(index2)-1] == letter)


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    lines = _file.read().split('\n')
n = sum([1 for line in lines if check2(line)])
print(n)
