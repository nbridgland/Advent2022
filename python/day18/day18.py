from python.util import read_file
import numpy as np

filename = 'input.txt'

puzzle_input = read_file(filename)
points = [[int(number) for number in entry.split(',')] for entry in puzzle_input]
points = [tuple(point) for point in points]
max_value = max([max(point) for point in points])

drop = np.zeros(shape=(max_value + 2, max_value + 2, max_value + 2))
for point in points:
    drop[point] = 1


def count_adjacent_sides(x, y, z):
    count = 0
    if x != 0:
        if drop[x - 1, y, z] == 1:
            count += 1
    if x != len(drop) - 1:
        if drop[x + 1, y, z] == 1:
            count += 1
    if y != 0:
        if drop[x, y - 1, z] == 1:
            count += 1
    if y != len(drop) - 1:
        if drop[x, y + 1, z] == 1:
            count += 1
    if z != 0:
        if drop[x, y, z - 1] == 1:
            count += 1
    if z != len(drop) - 1:
        if drop[x, y, z + 1] == 1:
            count += 1
    return count


def outline_exterior(x, y, z):
    drop[x, y, z] = 2
    adjusted = 0
    if x != 0:
        if drop[x - 1, y, z] == 0:
            drop[(x - 1, y, z)] = 2
            adjusted += 1
    if x < max_value + 1:
        if drop[x + 1, y, z] == 0:
            drop[(x + 1, y, z)] = 2
            adjusted += 1
    if y != 0:
        if drop[x, y - 1, z] == 0:
            drop[(x, y - 1, z)] = 2
            adjusted += 1
    if y < max_value + 1:
        if drop[x, y + 1, z] == 0:
            drop[(x, y + 1, z)] = 2
            adjusted += 1
    if z != 0:
        if drop[x, y, z - 1] == 0:
            drop[(x, y, z - 1)] = 2
            adjusted += 1
    if z < max_value + 1:
        if drop[x, y, z + 1] == 0:
            drop[(x, y, z + 1)] = 2
            adjusted += 1
    return adjusted


if __name__ == "__main__":
    # Part 1
    output = 0
    for point in points:
        x, y, z = point
        output += 6 - count_adjacent_sides(x, y, z)
    print(output)

    # Part 2
    drop[(0, 0, 0)] = 2
    changed = 1
    while changed > 0:
        changed = 0
        for x in range(len(drop)):
            for y in range(len(drop[0])):
                for z in range(len(drop[0][0])):
                    if drop[x, y, z] == 2:
                        changed += outline_exterior(x, y, z)

    output = 0
    for x in range(len(drop)):
        for y in range(len(drop[0])):
            for z in range(len(drop[0][0])):
                if drop[x, y, z] == 2:
                    output += count_adjacent_sides(x, y, z)
    print(output)
