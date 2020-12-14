passPorts = []
list_number = 0
for count, line in enumerate(open('input.txt', 'r')):
    if count == 0:
        passPorts.append(line.split())
    elif line == '\n':
        list_number = list_number + 1
        passPorts.append([])
    else:
        passPorts[list_number].extend(line.split())
print(passPorts)

# Part1
valid = 0
count_fields = set()
contain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passPorts:
    for field in passport:
        if field[:3] in contain:
            count_fields.add(field[:3])
    if len(count_fields) >= 7:
        valid = valid + 1
    count_fields = set()
print('Valid passports part1: %d' % valid)
del contain

# Part2
valid = 0
count_fields = set()
for passport in passPorts:
    for field in passport:
        if field[:3] == 'byr' and 1920 <= int(field[4:8]) <= 2002:
            count_fields.add(field[:3])
        if field[:3] == 'iyr' and 2010 <= int(field[4:8]) <= 2020:
            count_fields.add(field[:3])
        if field[:3] == 'eyr' and 2020 <= int(field[4:8]) <= 2030:
            count_fields.add(field[:3])
        if field[:3] == 'hgt':
            if (field[7:9]) == 'cm' and 150 <= int(field[4:7]) <= 193:
                count_fields.add(field[:3])
            if (field[6:8]) == 'in' and 59 <= int(field[4:6]) <= 76:
                count_fields.add(field[:3])
        if field[:3] == 'hcl' and field[4] == '#':
            try:
                int(field[5:11], 16)
                count_fields.add(field[:3])
            except ValueError:
                print('fail')
                pass
        if (field[:3] == 'ecl') and (field[4:7] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            count_fields.add(field[:3])
        if field[:3] == 'pid' and len(field[4:]) == 9 and field[4:].isnumeric():
            count_fields.add(field[:3])
    if len(count_fields) >= 7:
        valid = valid + 1
    count_fields = set()
print('Valid passports part2: %d' % valid)
