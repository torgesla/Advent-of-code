import sys
import os
import re
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    instructions = _file.read().split('\n')
indices_of_jmp_nop = [i for i, line in enumerate(instructions) if(line.split()[0] in ('jmp', 'nop'))]
for index in indices_of_jmp_nop:
    visited = []
    acc, i = 0, 0
    isCorrect = True
    modified = instructions[:]  # Shallow copy orig.list
    if('nop' in modified[index]):
        modified[index] = modified[index].replace('nop', 'jmp')
    else:
        modified[index] = modified[index].replace('jmp', 'nop')
    try:
        while(True):
            if(i in visited):
                isCorrect = False
                break
            ins = modified[i]
            visited.append(i)
            number = int(ins.split()[-1])
            if('acc' in ins):
                acc += number
            elif('jmp' in ins):
                i += number
                continue
            i += 1
    except IndexError:
        pass

    if(isCorrect):
        print(acc)
        break
