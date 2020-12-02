import re

with open("./input.txt", "r") as f:
    passwords = f.readlines()
    passwords = [x.strip('\n') for x in passwords]

    """
    Group 1: min occurrences
    2: max occurrences
    3: letter
    4: password
    """
    regex = [re.search(r'(\d+(?=-))-((?<=-)\d+) (\w): (\w+)', x) for x in passwords]


def part1(r):
    c = 0
    for x in r:
        q = 0
        char = x.group(3)
        for a in x.group(4):
            if a == char: q += 1
        if q in range(int(x.group(1)), int(x.group(2)) + 1): c += 1
    return c


def part2(r):
    c = 0
    for x in r:
        b = False
        char = x.group(3)
        if x.group(4)[int(x.group(1)) - 1] == char: b = not b
        if x.group(4)[int(x.group(2)) - 1] == char: b = not b
        if b: c += 1
    return c


print(part1(regex))
print(part2(regex))
