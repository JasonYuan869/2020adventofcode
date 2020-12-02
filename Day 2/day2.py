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

c = 0
for x in regex:
    q = 0
    char = x.group(3)
    for a in x.group(4):
        if a == char: q += 1
    if q in range(int(x.group(1)), int(x.group(2)) + 1): c += 1

print(c)
