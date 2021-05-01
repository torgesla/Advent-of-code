import sys
import os
import math


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    earliest_timestamp, bus_ids = _file.read().split('\n')
earliest_timestamp = int(earliest_timestamp)
bus_ids = [(int(x), -i) for i, x in enumerate(bus_ids.split(',')) if x != 'x']  # Tuples of(bus_id, min_after_first)

# Part 1
""" 
    earliest_dep = math.inf
    for bus_id in bus_ids:
        factor = math.ceil(earliest_timestamp / bus_id)
        this_bus_dep = factor * bus_id
        if (this_bus_dep < earliest_dep):
            earliest_bus_id = bus_id
            earliest_dep = this_bus_dep
    waiting_time = earliest_dep - earliest_timestamp
    print(waiting_time * bus_id) 
"""
# Part 2
"""
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1


    def findMinX(busid_rest):
        prod = 1
        for bus_id, _ in busid_rest:
            prod *= bus_id
        result = 0
        for bus_id, rest in busid_rest:
            q = prod // bus_id
            result += rest * mul_inv(q, bus_id) * q
        return result % prod


    print(findMinX(bus_ids))
"""
