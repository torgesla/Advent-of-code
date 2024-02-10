import sys
import os

def pipe(start, *funcs):
    res = start
    for func in funcs:
        res = func(res)
    return res
  
def part1():
    with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
        blocks = _file.read().split("\n\n")
        total_per_block = [sum(map(int, block.split("\n"))) for block in blocks]
        return max(total_per_block)

def part2():
    with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
        blocks = _file.read().split("\n\n")
        total_per_block = [sum(map(int, block.split("\n"))) for block in blocks]
        total_per_block = [pipe(block.split("\n"),lambda line: int(line), sum) for block in blocks]

        top3 = pipe(total_per_block, sorted, reversed, list)[:3]
        return sum(top3)

result = part2()
print(result)
