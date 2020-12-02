import re

with open("./input.txt", "r") as f:
    passwords = [x.strip('\n') for x in f.readlines()]

    """
    Group 1: min occurrences
    2: max occurrences
    3: letter
    4: password
    """
    regex = [re.search(r'(\d+(?=-))-((?<=-)\d+) (\w): (\w+)', x) for x in passwords]


def part1(r):
    count = 0
    for match in r:
        frequency = 0
        char = match.group(3)
        for character in match.group(4):
            if character == char: frequency += 1
        if frequency in range(int(match.group(1)), int(match.group(2)) + 1): count += 1
    return count


def part2(r):
    count = 0
    for match in r:
        satisfied = False
        char = match.group(3)
        if match.group(4)[int(match.group(1)) - 1] == char: satisfied = not satisfied
        if match.group(4)[int(match.group(2)) - 1] == char: satisfied = not satisfied
        if satisfied: count += 1
    return count


print(part1(regex))
print(part2(regex))
