from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

visibility = [[0 for k in range(len(puzzle_input[0]))] for j in range(len(puzzle_input))]


def mark_visibility(line, index, direction='row'):
    if direction == 'row':
        max_height = '-1'
        for k in range(len(line)):
            if line[k] > max_height:
                visibility[index][k] = 1
                max_height = line[k]
        max_height = '-1'
        for k in range(len(line)-1, -1, -1):
            if line[k] > max_height:
                visibility[index][k] = 1
                max_height = line[k]
    if direction == 'column':
        max_height = '-1'
        for k in range(len(line)):
            if line[k] > max_height:
                visibility[k][index] = 1
                max_height = line[k]
        max_height = '-1'
        for k in range(len(line)-1, -1, -1):
            if line[k] > max_height:
                visibility[k][index] = 1
                max_height = line[k]


def find_scenic_score(row, column):
    if row == 0 or column == 0 or row==len(puzzle_input)-1 or column == len(puzzle_input[0])-1:
        return 0
    score = 1
    tree_height = puzzle_input[row][column]
    k = 1
    while row-k > 0:
        if puzzle_input[row-k][column] >= tree_height:
            break
        k += 1
    score *= k
    k = 1
    while row+k < len(puzzle_input)-1:
        if puzzle_input[row+k][column] >= tree_height:
            break
        k += 1
    score *= k
    k = 1
    while column-k > 0:
        if puzzle_input[row][column-k] >= tree_height:
            break
        k += 1
    score *= k
    k=1
    while column+k < len(puzzle_input[0])-1:
        if puzzle_input[row][column+k] >= tree_height:
            break
        k += 1
    score *= k
    return score



if __name__ == "__main__":
    # Part 1
    k = 0
    while k < len(puzzle_input):
        mark_visibility(puzzle_input[k], index=k, direction='row')
        k+=1
    k=0
    while k < len(puzzle_input[0]):
        mark_visibility([row[k] for row in puzzle_input], index=k, direction='column')
        k+=1
    print(sum([sum(row) for row in visibility]))

    # Part 2
    print(max([max(find_scenic_score(k,j) for j in range(len(puzzle_input))) for k in range(len(puzzle_input))]))
