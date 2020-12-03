listOfNumbers = [line.rstrip().split(' ') for line in open('input.txt', 'r')]
part1 = 0
part2 = 0
for x in listOfNumbers:
    limits = x[0].split('-')
    minimum = int(limits[0])
    maximum = int(limits[1])
    char = x[1][:1]

    count = 0
    for y in x[2]:
        if y == char:
            count = count + 1
    if minimum <= count <= maximum:
        part1 = part1 + 1

    # --------part2
    if (x[2][minimum-1] == char) ^ (x[2][maximum-1] == char):
        part2 = part2 + 1

print(part1)
print(part2)
