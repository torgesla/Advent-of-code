import sys
import os
import numpy as np
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    instructions = _file.read().split('\n')
grid = np.zeros((1000, 1000))
""" for instruction in instructions:
    splitted = instruction.split(' ')
    start_x, start_y = splitted[-3].split(',')
    end_x, end_y = splitted[-1].split(',')
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    if('off' in instruction):
        grid[start_x:end_x + 1, start_y:end_y + 1] = 0.0
    elif('on' in instruction):
        grid[start_x:end_x + 1, start_y:end_y + 1] = 1.0
    else:
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                grid[x, y] = 0.0 if grid[x, y] else 1.0 """
for instruction in instructions:
    splitted = instruction.split(' ')
    start_x, start_y = splitted[-3].split(',')
    end_x, end_y = splitted[-1].split(',')
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    ins = splitted[-4]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if(ins == 'on'):
                grid[x, y] += 1.0
            elif(ins == 'off'):
                grid[x, y] = max(0.0, grid[x, y] - 1)
            else:
                grid[x, y] += 2.0


print(sum(sum(grid)))
