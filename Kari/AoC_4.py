import os
import sys
import re
#kommentar
with open(os.path.join(sys.path[0], 'input4.txt'), "r") as batchFile:
    lines = batchFile.read().split('\n\n')

passports = []
fields = []
required = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
validPassports = []
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valids = []

for line in lines:
    valid = True
    for field in required:
        if field not in line:
            valid = False
    if valid:
        validPassports.append(line)

result = 0
for passport in validPassports:
    validItem = True
    _sorted = re.split('\n| ', passport)
    for item in _sorted:
        splitItem = item.split(':')
        if splitItem[0] == 'byr' and (int(splitItem[1]) < 1920 or int(splitItem[1]) > 2002):
            validItem = False

        elif splitItem[0] == 'iyr' and (int(splitItem[1]) < 2010 or int(splitItem[1]) > 2020):
            validItem = False

        elif splitItem[0] == 'eyr' and (int(splitItem[1]) < 2020 or int(splitItem[1]) > 2030):
            validItem = False

        elif splitItem[0] == 'hgt':
            if len(splitItem[1]) < 4:
                validItem = False
            elif not (splitItem[1][-2:] == 'cm' or splitItem[1][-2:] == 'in'):
                validItem = False
            elif splitItem[1][-2:] == 'cm' and (int(splitItem[1][:-2]) < 150 or int(splitItem[1][:-2]) > 193):
                validItem = False
            elif splitItem[1][-2:] == 'in' and (int(splitItem[1][:-2]) < 59 or int(splitItem[1][:-2]) > 76):
                validItem = False

        elif splitItem[0] == 'hcl':
            if len(splitItem[1]) != 7:
                validItem = False
            elif splitItem[1][0] != '#':
                validItem = False
            elif not splitItem[1][1:].isalnum():
                validItem = False

        elif splitItem[0] == 'ecl' and splitItem[1] not in eyeColors:
            validItem = False

        elif splitItem[0] == 'pid':
            if len(splitItem[1]) != 9:
                validItem = False
            elif not splitItem[1].isdecimal():
                validItem = False
    if validItem:
        result += 1

print(result)

# print(len(validPassports))
# print(validPassports)
""" elif splitItem[1][0] != '0':
        validItem = False """
