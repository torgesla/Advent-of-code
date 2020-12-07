import sys
import os

with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    bag_rules = _file.read().split('\n')
