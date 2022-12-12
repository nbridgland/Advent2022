from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)

columns = len(puzzle_input[0])
rows = len(puzzle_input)
steps_matrix = [[rows*columns for k in range(columns)] for j in range(rows)]


# Set start, end
for row in range(rows):
    for column in range(columns):
        if puzzle_input[row][column] == 'S':
            start_row, start_column = row, column
        elif puzzle_input[row][column] == 'E':
            end_row, end_column = row, column


def find_shortest_path(cur_row, cur_col, step):
    for k in [-1, 1]:
        if 0 <= cur_row + k < rows and (ord(puzzle_input[cur_row+k][cur_col]) - ord(puzzle_input[cur_row][cur_col]) >= -1):
            if step < steps_matrix[cur_row+k][cur_col]:
                steps_matrix[cur_row+k][cur_col] = step
        if 0 <= cur_col + k < columns and (ord(puzzle_input[cur_row][cur_col+k]) - ord(puzzle_input[cur_row][cur_col]) >= -1):
            if step < steps_matrix[cur_row][cur_col+k]:
                steps_matrix[cur_row][cur_col+k] = step


if __name__ == "__main__":
    puzzle_input = [list(row) for row in puzzle_input]
    puzzle_input[start_row][start_column] = 'a'
    puzzle_input[end_row][end_column] = 'z'
    steps_matrix[end_row][end_column] = 0

    for k in range(rows * columns):
        if k % 1000 == 0:
            print(k)
        for row in range(rows):
            for column in range(columns):
                if steps_matrix[row][column] == k:
                    find_shortest_path(row, column, k + 1)  # Marks adjacent things as the next length

    print(steps_matrix[start_row][start_column])

    # Part 2:
    minimum = 423
    for row in range(rows):
        for column in range(columns):
            if puzzle_input[row][column] == 'a':
                if steps_matrix[row][column] < minimum:
                    minimum = steps_matrix[row][column]
    print(minimum)
