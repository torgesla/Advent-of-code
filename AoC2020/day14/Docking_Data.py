import sys
import os
import itertools
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    mask_operations = _file.read()[7:].split('\nmask = ')

"""
    mask_operations_structured = []
    for mask_operations in mask_operations:
        x = mask_operations.split('\nmem[')  # [mask, op, op2,...]
        mask = [(i, y) for i, y in enumerate(x[0]) if y != 'X']  # [(bit, index), (bit2, index2), ..]
        operations = []
        for operation in x[1:]:
            index, write_int = operation.split('] = ')
            # Adds leading zeroes if bin representation is shorter than 36 bit
            index, write_bin_formatted = int(index), bin(int(write_int))[2:].zfill(36)
            operations.append((index, write_bin_formatted))
        mask_operations_structured.append((mask, operations))

    mem = {}
    for mask, operations in mask_operations_structured:
        for mem_index, write_bin in operations:
            write_list = list(write_bin)
            for index, bit in mask:
                write_list[index] = bit
            mem[mem_index] = int(''.join(map(str, write_list)), 2)
    print(sum(mem.values()))
"""
mask_operations_structured = []
for mask_operations in mask_operations:
    x = mask_operations.split('\nmem[')  # [mask, op, op2,...]
    mask = [(i, y) for i, y in enumerate(x[0])]  # [(bit, index), (bit2, index2), ..]
    operations = []
    for operation in x[1:]:
        index, write_int = operation.split('] = ')
        # Adds leading zeroes if bin representation is shorter than 36 bit
        index, write_bin_formatted = bin(int(index))[2:].zfill(36), int(write_int)
        operations.append((index, write_bin_formatted))
    mask_operations_structured.append((mask, operations))

mem = {}
for mask, operations in mask_operations_structured:
    for mem_index, write_int in operations:
        index_list = list(mem_index)
        x_indices = []
        for index, bit in mask:  # Go through mask bits, and change adress if 1 or X
            if(bit in '1X'):
                index_list[index] = bit
                if(bit == 'X'):
                    x_indices.append(index)
        perm = list(itertools.product([0, 1], repeat=len(x_indices)))
        for bits in perm:
            for i, x_index in enumerate(x_indices):
                index_list[x_index] = bits[i]
            mem_index = int(''.join(map(str, index_list)), 2)
            mem[mem_index] = write_int
print(sum(mem.values()))
