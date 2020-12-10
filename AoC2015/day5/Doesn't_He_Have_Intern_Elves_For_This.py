import sys
import os
import math
import re

illegal = ('ab', 'cd', 'pq', 'xy')
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    naugthy_nice_list = _file.read().split('\n')


def isNice(record):
    if(any(word in record for word in illegal)):
        return False
    if(sum(map(record.lower().count, "aeiou")) < 3):
        return False
    for i in range(len(record) - 1):
        if(record[i] == record[i+1]):
            return True
    return False


def isNice2(record):
    # Arbitrary pair with at least on char in between, and one ocurrence of char1 appearing on each side of a char1/2
    return re.search(r'(..).*\1', record) \
        and re.search(r'(.).\1', record)


num_nice = sum([1 for record in naugthy_nice_list if isNice2(record)])
print(num_nice)
