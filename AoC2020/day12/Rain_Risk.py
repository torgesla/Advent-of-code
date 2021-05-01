import sys
import os
import math


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    directions = _file.read().split('\n')
directions = [(pair[0], int(pair[1:])) for pair in directions]


def update_theta():
    return math.atan((pos_y - ship_pos_y) / (pos_x - ship_pos_x))


def update_compass():
    return


ship_pos_x, ship_pos_y = 0, 0
pos_x, pos_y = 10, 1
theta = update_theta()
for direction_pair in directions:
    action, value = direction_pair
    if(action in 'NSEW'):
        if(action == 'N'):
            pos_y += value
        elif(action == 'S'):
            pos_y -= value
        elif(action == 'E'):
            pos_x += value
        elif(action == 'W'):
            pos_x -= value
        theta = update_theta()
    elif(action == 'F'):
        ship_pos_x += value * math.cos(theta)
        pos_x += value * math.cos(theta)
        ship_pos_y += value * math.sin(theta)
        pos_y += value * math.sin(theta)
    else:
        if(action == 'L'):
            theta += math.radians(value)
        elif(action == 'R'):
            theta -= math.radians(value)
        update_compass()
print(abs(ship_pos_x) + abs(ship_pos_y))
