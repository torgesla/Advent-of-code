import sys
import os
import re

with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    rules = _file.read().split('\n')
wires = {}
for rule in rules:
    ex, to_var = rule.split(' -> ')
    if(ex[0].isnumeric()):
        wires[to_var] = bin(ex)
    elif('AND' in rule):
        var1, var2 = ex.split(' AND ')
        wires[to_var] = wires[var1] & wires[var2]
    elif('OR' in rule):
        var1, var2 = ex.split(' OR ')
        wires[to_var] = wires[var1] | wires[var2]
    elif('NOT' in rule):
        var1 = ex.split(' ')[-1]
        wires[to_var] = wires[var1]
