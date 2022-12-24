from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)


class MapWalker:
    def __init__(self, puzzle_input):
        self.map = [[char for char in line] for line in puzzle_input[:-2]]
        self.row = 0
        self.column = min([k for k in range(len(self.map[0])) if self.map[0][k] == '.'])
        self.dimension = 'row'
        self.direction = 1
        self.directions = [['row', 1], ['column', 1], ['row', -1], ['column', -1]]

    def walk(self, steps: int):
        if self.dimension == 'row':
            if self.direction == 1:
                for k in range(steps):
                    if self.column + self.direction == len(self.map[self.row]) or \
                            self.map[self.row][self.column+self.direction] == ' ':
                        potential_column = min([j for j in range(len(self.map[self.row])) if self.map[self.row][j] != ' '])
                        if self.map[self.row][potential_column] == '#':
                            break
                        self.column = potential_column
                        continue
                    elif self.map[self.row][self.column+self.direction] == '#':
                        break
                    else:
                        self.column += self.direction
            if self.direction == -1:
                for k in range(steps):
                    if self.column + self.direction < 0 or self.map[self.row][self.column+self.direction] == ' ':
                        potential_column = max([j for j in range(len(self.map[self.row])) if self.map[self.row][j] != ' '])
                        if self.map[self.row][potential_column] == '#':
                            break
                        self.column = potential_column
                        continue
                    elif self.map[self.row][self.column+self.direction] == '#':
                        break
                    else:
                        self.column += self.direction
        if self.dimension == 'column':
            if self.direction == 1:
                for k in range(steps):
                    if self.row + self.direction == len(self.map) or \
                            self.column >= len(self.map[self.row + self.direction]) or \
                            self.map[self.row+self.direction][self.column] == ' ':
                        potential_row = min([j for j in range(len(self.map))
                                             if self.column < len(self.map[j]) and self.map[j][self.column] != ' '])
                        if self.map[potential_row][self.column] == '#':
                            break
                        else:
                            if self.map[potential_row][self.column] != '.':
                                print(self.map[potential_row][self.column])
                                print("ahlp")
                                raise
                            self.row = potential_row
                            continue
                    elif self.map[self.row + self.direction][self.column] == '#':
                        break
                    else:
                        self.row += self.direction
            if self.direction == -1:
                for k in range(steps):
                    if self.row + self.direction < 0 or \
                            self.column >= len(self.map[self.row + self.direction]) or \
                            self.map[self.row+self.direction][self.column] == ' ':
                        potential_row = max([j for j in range(len(self.map))
                                             if self.column < len(self.map[j]) and self.map[j][self.column] != ' '])
                        if self.map[potential_row][self.column] == '#':
                            break
                        else:
                            if self.map[potential_row][self.column] != '.':
                                print(self.map[potential_row][self.column])
                                print("halp")
                                raise
                            self.row = potential_row
                            continue
                    elif self.map[self.row+self.direction][self.column] == '#':
                        break
                    else:
                        self.row += self.direction

    def turn(self, rotation: str):
        if rotation == 'R':
            self.dimension, self.direction = self.directions[(self.directions.index([self.dimension, self.direction]) + 1) % 4]
        if rotation == 'L':
            self.dimension, self.direction = self.directions[(self.directions.index([self.dimension, self.direction]) - 1) % 4]
            

if __name__ == "__main__":
    walker = MapWalker(puzzle_input)
    directions = puzzle_input[-1]
    k = 0
    string = ''
    while k < len(directions):
        try:
            int(directions[k])
            string += directions[k]
        except:
            walker.walk(int(string))
            walker.turn(directions[k])
            string = ''
        k += 1
    walker.walk(int(string))
    print(1000*(walker.row+1) + 4*(walker.column+1)+walker.directions.index([walker.dimension, walker.direction]))
