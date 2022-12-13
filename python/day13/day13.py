from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)


def compare_items(item1, item2):
    if type(item1) == list:
        if type(item2) == list:
            return compare_lists(item1, item2)
        return compare_lists(item1, [item2])
    if type(item2) == list:
        return compare_lists([item1], item2)
    if item1 < item2:
        return "<"
    if item1 > item2:
        return ">"
    return "="


def compare_lists(list1, list2):
    if len(list1) > 0:
        if len(list2) > 0:
            comparison = compare_items(list1[0], list2[0])
            if comparison == "=":
                return compare_lists(list1[1:], list2[1:])
            return comparison
        return ">"
    if len(list2) == 0:
        return "="
    return "<"


if __name__ == "__main__":
    output = 0
    for k in range(len(puzzle_input)//3+1):
        if compare_lists(eval(puzzle_input[3*k]), eval(puzzle_input[3*k+1])) == '<':
            output += k+1
    print(output)

    # Part 2:
    packet1 = [[2]]
    packet2 = [[6]]
    loc1=0
    loc2=0
    for entry in puzzle_input:
        if entry:
            if compare_lists(eval(entry), packet1) == '<':
                loc1 += 1
                loc2 += 1
            elif compare_lists(eval(entry), packet2) == '<':
                loc2 += 1

    print((loc1+1)*(loc2+2))
