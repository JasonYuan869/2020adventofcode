with open('./input.txt', 'r') as f:
    lines = [x.strip('\n') for x in f.readlines()]


def parse_seat_id(line):
    current_col = range(128)
    current_row = range(8)
    for char in line:
        min_col = current_col.start
        max_col = current_col.stop
        half_col = len(current_col) // 2

        min_row = current_row.start
        max_row = current_row.stop
        half_row = len(current_row) // 2
        if char == 'F':
            current_col = range(min_col, max_col - half_col)
        elif char == 'B':
            current_col = range(half_col + min_col, max_col)
        elif char == 'R':
            current_row = range(half_row + min_row, max_row)
        elif char == 'L':
            current_row = range(min_row, max_row - half_row)
    return current_col[0] * 8 + current_row[0]


try:
    assert (s := parse_seat_id('FBFBBFFRLR')) == 357
except AssertionError:
    print(s)


def part1():
    global lines
    max_id = 0
    for line in lines:
        if (x := parse_seat_id(line)) > max_id:
            max_id = x
    return max_id


def part2():
    global lines
    ids = []
    for line in lines:
        ids.append(parse_seat_id(line))
    ids.sort()
    for index in range(1, len(ids) - 1):
        if ids[index] + 2 == ids[index + 1]:
            return ids[index] + 1


print(part1())
print(part2())
