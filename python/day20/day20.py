from python.util import read_file
import time

time1 = time.time()

filename = 'input.txt'

puzzle_input = read_file(filename)


def mix(integers, order, move):
    current_index = order.index(move)
    new_index = current_index + integers[current_index]
    new_index = new_index % (len(integers) - 1)
    if new_index > current_index:
        integers = integers[:current_index] + integers[current_index+1: new_index + 1] + [integers[current_index]] + integers[
                                                                                                    new_index + 1:]
        order = order[:current_index] + order[current_index+1: new_index + 1] + [order[current_index]] + order[new_index+1:]
    if new_index < current_index:
        integers = integers[:new_index] + [integers[current_index]] + integers[new_index: current_index] + integers[
                                                                                current_index+1:]
        order = order[:new_index] + [order[current_index]] + order[new_index: current_index] + order[current_index+1:]
    return integers, order


if __name__ == "__main__":
    reference_list = [int(line) for line in puzzle_input]
    integer_list = [int(line) % (len(puzzle_input) - 1) for line in puzzle_input]
    order = [k for k in range(len(puzzle_input))]

    for k in range(len(puzzle_input)):
        integer_list, order = mix(integer_list, order, k)

    output = 0
    zero_index = integer_list.index(0)
    for k in [1000, 2000, 3000]:
        output += reference_list[order[(zero_index + k) % len(integer_list)]]
    print(f"Part 1: {output}")

    multiple = 811589153
    reference_list = [int(line)*multiple for line in puzzle_input]
    integer_list = [(int(line)*multiple) % (len(puzzle_input) - 1) for line in puzzle_input]
    order = [k for k in range(len(puzzle_input))]

    for j in range(10):
        for k in range(len(puzzle_input)):
            integer_list, order = mix(integer_list, order, k)

    output = 0
    zero_index = integer_list.index(0)
    for k in [1000, 2000, 3000]:
        output += reference_list[order[(zero_index + k) % len(integer_list)]]
    print(f"Part 2: {output}")
