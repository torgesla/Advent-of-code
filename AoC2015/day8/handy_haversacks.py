import sys
import os

rule_dict = {}
with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    bag_rules = _file.read().split('\n')
for rule in bag_rules:
    parent_bag, children_string = rule.split(' bags contain ')  # ["color", "num1 color1 bag, num2 color2 bags."]
    children_array = []
    if('no other' not in children_string):
        for child in children_string.split(', '):
            splitted_child = child.split(' ')
            num, color = int(splitted_child[0]), ' '.join(splitted_child[1:-1])
            children_array.append((color, num))
    rule_dict[parent_bag] = children_array


def isAncestor(bag_color):
    if(bag_color in ancestors or bag_color == 'shiny gold'):
        return True
    isAncestor_bool = False
    for child in rule_dict.get(bag_color):
        isAncestor_bool = max(isAncestor_bool, isAncestor(child[0]))
    if(isAncestor_bool):
        ancestors.append(bag_color)
    return isAncestor_bool


def calcNumberOfDescendants(bag_color):
    total_bags = 1
    for child_bag in rule_dict[bag_color]:
        child_bag_color, child_bag_count = child_bag
        total_bags += child_bag_count * calcNumberOfDescendants(child_bag_color)
    return total_bags


ancestors = []
for bag_color in rule_dict.keys():
    isAncestor(bag_color)
print(len(ancestors))
gold_sum = calcNumberOfDescendants('shiny gold')
print(gold_sum - 1)  # Minus the gold one
