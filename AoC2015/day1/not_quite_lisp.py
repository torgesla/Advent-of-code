import sys
import os
import re

with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    parantheses = _file.read()


def floor():
    return parantheses.count('(') - parantheses.count(')')


def pos_basement():
    current = 0
    for i, char in enumerate(parantheses):
        current += 1 if char == '(' else -1
        if(current == -1):
            return i


floor()
print(pos_basement())
