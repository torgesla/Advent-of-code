import sys
import os
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    numbers = _file.read().split('\n')
numbers = [int(n) for n in numbers]
preamble = numbers[:5]


def isValid(index, number):
    previous = numbers[index-25:index]
    for num1 in previous:
        cand = number - num1
        if(cand in previous and cand != num1):
            return True
    return False


def contSet():
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers):
            sublist = numbers[i:j]
            if(sum(sublist) == invalid_number):
                print(min(sublist) + max(sublist))


""" not_valids = [number for i, number in enumerate(numbers) if(not isValid(i, number) and i >= 25)]
print(not_valids[0]) """

invalid_number = 14360655
contSet()
