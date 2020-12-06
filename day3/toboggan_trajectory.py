import sys
import os
import re
import numpy as np

strats = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    _map = _file.read().split('\n')
width = len(_map[0])


def check(add_x, add_y):
    x, y = (0, 0)
    encountered = []
    try:
        while(True):
            encountered.append(_map[y][x])
            x, y = (x+add_x) % width, y+add_y
    except IndexError:
        return encountered.count('#')


prod = np.prod([check(x, y) for x, y in strats])
print(prod)
