import itertools
import sys
import os
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    hypercube_layer = _file.read().split('\n')
""" cubes = {}
neighbors = {}
for r, row in enumerate(hypercube_layer):
    for c, cube in enumerate(row):
        cubes[(c, r, 0)] = int(cube == '#')


def getNumNeighbors(x0, y0, z0):
    N = 0
    for x in range(x0-1, x0+2):
        for y in range(y0-1, y0+2):
            for z in range(z0-1, z0+2):
                if((x, y, z) != (x0, y0, z0)):
                    N += cubes.get((x, y, z), 0)
    return N


for _ in range(6):
    # Update neighbor matrix
    for x0, y0, z0 in cubes:
        x_range = range(x0-1, x0+2)
        y_range = range(y0-1, y0+2)
        z_range = range(z0-1, z0+2)
        for x, y, z in itertools.product(x_range, y_range, z_range):
            neighbors[(x, y, z)] = getNumNeighbors(x, y, z)
    # Update cubes
    for (x0, y0, z0), n in neighbors.items():
        isActive = cubes.get((x0, y0, z0), 0)
        if(isActive and n in (2, 3)):
            new_status = 1
        elif(not isActive and n == 3):
            new_status = 1
        else:
            new_status = 0
        cubes[x0, y0, z0] = new_status
print(sum(cubes.values()))
 """

cubes2 = {}
neighbors2 = {}
for r, row in enumerate(hypercube_layer):
    for c, cube in enumerate(row):
        cubes2[(c, r, 0, 0)] = int(cube == '#')


def getNumNeighbors2(x0, y0, z0, w0):
    N = 0
    for x in range(x0-1, x0+2):
        for y in range(y0-1, y0+2):
            for z in range(z0-1, z0+2):
                for w in range(w0-1, w0+2):
                    if((x, y, z, w) != (x0, y0, z0, w0)):
                        N += cubes2.get((x, y, z, w), 0)
    return N


for _ in range(6):
    # Update neighbor matrix
    for x0, y0, z0, w0 in cubes2:
        x_range = range(x0-1, x0+2)
        y_range = range(y0-1, y0+2)
        z_range = range(z0-1, z0+2)
        w_range = range(w0-1, w0+2)
        for x, y, z, w in itertools.product(x_range, y_range, z_range, w_range):
            neighbors2[(x, y, z, w)] = getNumNeighbors2(x, y, z, w)
    # Update cubes
    for (x0, y0, z0, w0), n in neighbors2.items():
        isActive = cubes2.get((x0, y0, z0, w0), 0)
        if(isActive and n in (2, 3)):
            new_status = 1
        elif(not isActive and n == 3):
            new_status = 1
        else:
            new_status = 0
        cubes2[x0, y0, z0, w0] = new_status
print(sum(cubes2.values()))
