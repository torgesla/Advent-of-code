import sys
import os
import math


def calcAxis(letter1, letter2):
    def calcBody(key, lower, upper):
        if(lower == upper):
            return lower
        if(key[0] == letter1):
            key = key[1:]
            upper = math.floor((lower + upper)/2)
            return calcBody(key, lower, upper)
        elif(key[0] == letter2):
            key = key[1:]
            lower = math.ceil((upper + lower)/2)
            return calcBody(key, lower, upper)
    return calcBody


calcRow = calcAxis('F', 'B')
calcColumn = calcAxis('L', 'R')
def calcId(key): return 8 * calcRow(key[:-3], 0, 127) + calcColumn(key[-3:], 0, 7)


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    keys = _file.read().split('\n')
""" max_id = max([calcId(key) for key in keys])
print(max_id) """
keys = [calcId(key) for key in keys]
for key in keys:
    if(key + 1 not in keys):
        print(key + 1)
