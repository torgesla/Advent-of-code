import sys
import os
import re
import numpy as np

with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    dimensions_array = _file.read().split('\n')


def calc_area(dimensions_string):
    l, w, h = [int(num) for num in dimensions_string.split('x')]
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, l*h)


def feet_of_ribbon(dims):
    l_w_h = [int(num) for num in dims.split('x')]
    l, w, h = l_w_h
    dim_sorted = sorted(l_w_h)
    return np.product(dim_sorted) + 2 * dim_sorted[0] + 2 * dim_sorted[1]


total_area = sum([calc_area(dim) for dim in dimensions_array])
total_ribbon = sum([feet_of_ribbon(dim) for dim in dimensions_array])
print(total_ribbon)
