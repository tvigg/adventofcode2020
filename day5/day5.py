listOfBoardingPasses = [line.rstrip() for line in open('input.txt', 'r')]
part2listOfBoardingPasses = listOfBoardingPasses.copy()


def smallest(first: str, second: str):
    for item in first:
        a = calc(first)
        b = calc(second)
        if a < b:
            return first
        else:
            return second


def calc(boarding_pass: str):
    a = int()
    for index, item in enumerate(boarding_pass):
        if item == 'B' or item == 'R':
            if index == 0:
                a = 1
            else:
                a = a << 1
                a = a ^ 1
        if item == 'F' or item == 'L':
            a = a << 1
    return a


def search_seat(big_list: list):
    sorted_list: list = ['']*814
    for item in big_list:
        sorted_list[calc(item)] = item
    before = 0
    for index, item in enumerate(sorted_list):
        c = calc(item)
        if c == 0 and before + 1 == index and index != 1:
            return index
        else:
            before = c
    return -1


while len(listOfBoardingPasses) != 1:
    for index, boarding_pass in enumerate(listOfBoardingPasses):
        if boarding_pass == listOfBoardingPasses[-1]:
            break
        temp = smallest(listOfBoardingPasses[index], listOfBoardingPasses[index + 1])
        listOfBoardingPasses.remove(temp)

print('part1: ', calc(listOfBoardingPasses[0][:7]) * 8 + calc(listOfBoardingPasses[0][7:10]))
print('part2: ', search_seat(part2listOfBoardingPasses))
