import pathlib
import os

path = pathlib.Path('.').parent / "inputs/3.txt"
with open(path, "r") as f:
    input_map = f.read().splitlines()

n_cols = len(input_map[0])

def count_trees(increment_col, increment_row):
    i = 0
    j = 0
    count = 0
    while(i < len(input_map)):
        mapp = input_map[i]
        if mapp[j] == '#':
            count += 1
        j = (j+increment_col) % n_cols
        i += increment_row
    return count


count_1 = count_trees(1, 1)
count_2 = count_trees(3, 1)
count_3 = count_trees(5, 1)
count_4 = count_trees(7, 1)
count_5 = count_trees(1, 2)

print(count_1)
print(count_2)
print(count_3)
print(count_4)
print(count_5)

print(count_1 * count_2 * count_3 * count_4 * count_5)
