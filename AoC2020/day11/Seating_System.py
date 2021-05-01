import sys
import os
import numpy as np
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    seat_map = _file.read().split('\n')
seat_map = [list(row) for row in seat_map]  # Because strings are immutable
max_row, max_column = len(seat_map), len(seat_map[0])


def num_neighbours(row_nr, column_nr):
    neighbours = ''
    for i in range(row_nr - 1, row_nr + 2):
        for j in range(column_nr - 1, column_nr + 2):
            if i in range(max_row) and j in range(max_column) and (i, j) != (row_nr, column_nr):
                neighbours += old_seatmap[i][j]
    return neighbours.count('#')


old_seatmap = seat_map.copy()
while(True):
    new_seatmap = old_seatmap.copy()
    for row_nr, row in enumerate(old_seatmap):
        for column_nr, cell in enumerate(row):
            neighbours = num_neighbours(row_nr, column_nr)  # Returns number of adjacent taken seats
            if((row_nr, column_nr) == (0, 3)):
                print(neighbours)
            if(cell == 'L' and neighbours == 0):
                new_seatmap[row_nr][column_nr] = '#'
            elif(cell == '#' and neighbours >= 4):
                new_seatmap[row_nr][column_nr] = 'L'
    break
for row in new_seatmap:
    print(row)
print(sum([row.count('#') for row in new_seatmap]))
