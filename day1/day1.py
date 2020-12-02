listOfNumbers = [int(line) for line in open('input.txt', 'r')]
print([(x*y)for x in listOfNumbers for y in listOfNumbers if x + y == 2020][0])
print([(x*y*z)for x in listOfNumbers for y in listOfNumbers for z in listOfNumbers if x + y + z == 2020][0])
