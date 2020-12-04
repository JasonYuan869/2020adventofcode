import re

with open('./input.txt', 'r') as f:
    lines = re.split(r"\n\n", f.read())  # Split by empty lines

passports = []

for line in lines:
    regex_match = re.findall(r"(\S+)(?=:):(?<=:)(\S+)", line)
    passport = {}
    for match in regex_match:
        passport[match[0]] = match[1]
    passports.append(passport)

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
BYR = range(1920, 2002 + 1)
IYR = range(2010, 2020 + 1)
EYR = range(2020, 2031 + 1)
HGTCM = range(150, 193 + 1)
HGTIN = range(59, 76 + 1)
ECL = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def part1():
    c = 0
    global passports
    for passport in passports:
        if len(passport.keys()) < 8:
            if len(passport.keys()) == 7 and 'cid' not in passport:
                c += 1
            else:
                continue
        else:
            c += 1
    return c


def validity_check(passport):
    if int(passport['byr']) not in BYR:
        return 0
    if int(passport['iyr']) not in IYR:
        return 0
    if int(passport['eyr']) not in EYR:
        return 0
    if not re.fullmatch(r"#[a-f0-9]{6}", passport['hcl']):
        return 0
    if hgt := re.fullmatch(r"(\d+)(cm|in)", passport['hgt']):
        if hgt.group(2) == 'cm':
            if int(hgt.group(1)) not in HGTCM:
                return 0
        else:
            if int(hgt.group(1)) not in HGTIN:
                return 0
    else:
        return 0
    if passport['ecl'] not in ECL:
        return 0
    if not re.fullmatch(r"[0-9]{9}", passport['pid']):
        return 0
    return 1


def part2():
    c = 0
    global passports
    for passport in passports:
        if len(passport.keys()) < 8:
            if len(passport.keys()) == 7 and 'cid' not in passport:
                c += validity_check(passport)
            else:
                continue
        else:
            c += validity_check(passport)
    return c


print(part1())
print(part2())
