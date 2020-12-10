# Convert input to a list of lists sorted by instruction
# Inner list is organized by [instruction: str, argument: int]
with open('./input.txt', 'r') as f:
    asm = [x.strip('\n') for x in f.readlines()]
    asm = [x.split(' ') for x in asm]
    asm = [[x[0], int(x[1])] for x in asm]


def part1(code):
    i = 0
    a = 0
    d = []
    while i < len(code):
        if i in d:
            return a, True
        else:
            d.append(i)
        inst = code[i][0]
        arg = code[i][1]
        if inst == 'nop':
            pass
        elif inst == 'acc':
            a += arg
        elif inst == 'jmp':
            i += arg - 1
        i += 1
    return a, False


def part2(code):
    i = 0
    d = []
    while i < len(code):
        d.append(i)
        inst = code[i][0]
        arg = code[i][1]
        if inst == 'nop':
            if i + arg == len(code):
                code[i][0] = 'jmp'
                return part1(code)
        elif inst == 'jmp':
            if i + arg in d:  # Upon hindsight, this is actually incorrect (but I was lucky enough that it worked)
                code[i][0] = 'nop'
                if not (x := part1(code))[1]:
                    return x[0]
                else:
                    code[i][0] = 'jmp'
        i += 1


print(part1(asm)[0])
print(part2(asm))
