with open('./input.txt', 'r') as f:
    serial = [int(x.strip('\n')) for x in f.readlines()]


def part1(ser_input):
    for i in range(25, len(ser_input)):
        subset = [ser_input[q] for q in range(i - 25, i)]
        sums = []
        for a in range(25):
            for b in range(a + 1, 25):
                sums.append(subset[a] + subset[b])
        if ser_input[i] not in sums:
            return ser_input[i]


def part2(ser_input):
    n = part1(ser_input)
    for a in range(len(ser_input)):
        csum = ser_input[a]
        for b in range(a + 1, len(ser_input)):
            csum += ser_input[b]
            if csum > n:
                break
            if csum == n:
                subset = [ser_input[q] for q in range(a, b + 1)]
                return max(subset) + min(subset)


print(part1(serial))
print(part2(serial))
