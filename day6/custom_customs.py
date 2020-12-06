import sys
import os
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    groups = _file.read().split('\n\n')
unique = [len(set(group.replace('\n', ''))) for group in groups]
groups_as_sets = [[set(entry) for entry in group.split('\n')] for group in groups]
common = [len(set.intersection(*group)) for group in groups_as_sets]
print(sum(unique), sum(common))
