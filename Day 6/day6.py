with open('./input.txt', 'r') as f:
    all_answers = [line.split('\n') for line in f.read().split('\n\n')]


def unique_responses(answers):
    responses = set()
    for answer in answers:
        for char in answer:
            responses.add(char)
    return len(responses)


def all_answered(answers):
    counts = {}
    sum = 0
    for answer in answers:
        for char in answer:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    for char in counts:
        if counts[char] == len(answers):
            sum += 1
    # print(sum)
    return sum


def part1(all_answers):
    sum = 0
    for answers in all_answers:
        sum += unique_responses(answers)
    return sum


def part2(all_answers):
    sum = 0
    for answers in all_answers:
        sum += all_answered(answers)
    return sum


test = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
assert part1(test) == 11
assert part2(test) == 6

print(part1(all_answers))
# NOTE REMOVE TRAILING NEWLINE FROM INPUT FILE OTHERWISE IT WILL NOT WORK
print(part2(all_answers))
