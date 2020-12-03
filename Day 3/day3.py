with open('./input.txt', 'r') as f:
    geography = [x.strip('\n') for x in f.readlines()]


def wrap(i, l):
    while i >= l:
        i -= l
    return i


def part2(right, down, arr):
    l = len(arr[0])  # Get length of repeating pattern
    x = 0
    c = 0
    i = 0
    while i < len(arr):
        if arr[i][wrap(x, l)] == '#': c += 1
        x += right
        i += down
    return c


print(part2(3, 1, geography))
print(part2(1, 1, geography) *
      part2(3, 1, geography) *
      part2(5, 1, geography) *
      part2(7, 1, geography) *
      part2(1, 2, geography))
