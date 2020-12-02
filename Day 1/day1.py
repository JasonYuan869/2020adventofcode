with open("./input.txt", "r") as f:
    report = f.readlines()
    report = [int(x.strip('\n')) for x in report]


def part1(r):
    for a in r:
        b = 2020 - a
        if b in r:
            return a * b


def part2(r):
    for a in r:
        b = 2020 - a
        for c in r:
            if c == a: continue
            d = b - c
            if d in r:
                return a * c * d


print(part1(report))
print(part2(report))
