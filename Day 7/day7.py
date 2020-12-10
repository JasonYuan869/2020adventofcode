import re

with open('./input.txt', 'r') as f:
    directory = [x.strip('\n') for x in f.readlines()]

outer_dict = {}

for entry in directory:
    match = re.search(r'^(\w+ \w+) bags contain ([^.]+)', entry)
    outer_bag = match.group(1)
    inner_list = [x.strip() for x in match.group(2).split(',')]
    inner_dict = {}

    for bag in inner_list:
        match = re.search(r'^(\d+) (\w+ \w+) bag', bag)
        try:
            inner_dict[match.group(2)] = int(match.group(1))
        except AttributeError:
            break

    outer_dict[outer_bag] = inner_dict

# Test case:
# outer_dict = {
#     'light red': {
#         'bright white': 1,
#         'muted yellow': 2,
#     },
#     'dark orange': {
#         'bright white': 3,
#         'muted yellow': 4,
#     },
#     'bright white': {
#         'shiny gold': 1,
#     },
#     'muted yellow': {
#         'shiny gold': 2,
#         'faded blue': 9,
#     },
#     'shiny gold': {
#         'dark olive': 1,
#         'vibrant plum': 2,
#     },
#     'dark olive': {
#         'faded blue': 3,
#         'dotted black': 4,
#     },
#     'vibrant plum': {
#         'faded blue': 5,
#         'dotted black': 6,
#     },
#     'faded blue': {},
#     'dotted black': {},
# }
# Expect: 4 part 1

# Test Case 2
# outer_dict = {
#     'shiny gold': {
#         'dark red': 2
#     },
#     'dark red': {
#         'dark orange': 2
#     },
#     'dark orange': {
#         'dark yellow': 2
#     },
#     'dark yellow': {
#         'dark green': 2
#     },
#     'dark green': {
#         'dark blue': 2
#     },
#     'dark blue': {
#         'dark violet': 2
#     },
#     'dark violet': {}
# }
# Expect: 32 part 2


# Brute force approach that iterates through every single bag option
def recursive_part1(b):
    global outer_dict
    if b == 'shiny gold':
        return 1
    else:
        for q in outer_dict[b]:
            if not (x := recursive_part1(q)):
                continue
            else:
                return x
    return 0


def recursive_part2(b):
    global outer_dict
    c = 0
    if not outer_dict[b]:
        return 0
    else:
        for q, v in outer_dict[b].items():
            x = recursive_part2(q)
            c += v + v * x
    return c


def part1():
    global outer_dict
    c = 0
    for b in outer_dict:
        if b != 'shiny gold':
            c += recursive_part1(b)
    return c


def part2():
    global outer_dict
    c = 0
    for k, v in outer_dict['shiny gold'].items():
        c += v
        c += v * recursive_part2(k)
    return c


print(part1())
print(part2())
