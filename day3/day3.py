listOfGeology = [list(line.rstrip()) for line in open('input.txt', 'r')]


def tree_counter(right: int, down: int):
    trees, traverse, down2 = 0, 0, 0
    for x in listOfGeology:
        down2 = down2 - 1
        if down2 > 0:
            continue
        if x[(traverse % (len(x)))] == '#':
            trees = trees + 1
        traverse = traverse + right
        down2 = down
    return trees


print(tree_counter(3, 1))
print(tree_counter(1, 1) * tree_counter(3, 1) * tree_counter(5, 1) * tree_counter(7, 1) * tree_counter(1, 2))
