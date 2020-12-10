import sys
import os
import numpy as np
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    adapters = _file.read().split('\n')
adapters = [int(adapter) for adapter in adapters]
adapters.sort()

"""
    def calc_diff(adapter):
        global current
        diff = adapter - current
        current = adapter
        return diff


    diff = [calc_diff(adapter) for adapter in adapters]
    diff.append(3)  # From final adapter to phone
    print(diff)
    print(diff.count(1) * diff.count(3))
"""


"""
    def calcCombinations(adapters):
        adapters.append(0)
        adapters.sort()
        combs = {adapters[-1]: 1}  # In case of last adapter
        for i, adap in reversed(list(enumerate(adapters[:-1]))):
            candidates = [cand for cand in adapters[i + 1:i + 4] if cand - adap <= 3]
            combs[adap] = sum(combs[cand] for cand in candidates)
        return combs[0]


    print(calcCombinations(adapters))
"""
