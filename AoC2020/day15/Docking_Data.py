puzzle_input = [2, 0, 6, 12, 1, 3]
mod_input = puzzle_input.copy()
mem = {e: i+1 for i, e in enumerate(mod_input[:-1])}
last_number = mod_input[-1]
for i in range(len(mod_input), 30_000_000):
    if(last_number in mem):
        num = i - mem[last_number]
    else:
        num = 0
    mem[last_number] = i
    mod_input.append(num)
    last_number = num
print(mod_input[-1])
