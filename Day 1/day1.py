with open("./input.txt", "r") as f:
    report = f.readlines()
    report = [int(x.strip('\n')) for x in report]


def part1(r):
    for first_expense in r:
        second_expense = 2020 - first_expense
        if second_expense in r:
            return first_expense * second_expense


def part2(r):
    for first_expense in r:
        second_expense = 2020 - first_expense
        for third_expense in r:
            if third_expense == first_expense: continue
            difference = second_expense - third_expense
            if difference in r:
                return first_expense * difference * third_expense


print(part1(report))
print(part2(report))
