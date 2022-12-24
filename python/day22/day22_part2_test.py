from python.util import read_file

filename = 'testinput.txt'

puzzle_input = read_file(filename)


class CubeMap:
    def __init__(self, faces):
        self.faces = faces
        self.face = 0
        self.size = len(self.faces[0])
        self.x = 0
        self.y = 0
        self.dimension = 'row'
        self.direction = 1
        self.directions = [['row', 1], ['column', 1], ['row', -1], ['column', -1]]

    def get_adjacent_cube_coordinates(self):
        """Return face number, x, y, dimension, direction"""
        if self.face == 0:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 5, self.size-1, self.size - self.y - 1, 'row', -1
                if self.direction == -1:
                    return 2, self.y, 0, 'column', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 3, self.x, 0, 'column', 1
                if self.direction == -1:
                    return 1, self.size - self.x - 1, 0, 'column', 1
        if self.face == 1:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 2, 0, self.y, 'row', 1
                if self.direction == -1:
                    return 5, self.size - self.y - 1, self.size - 1, 'column', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 4, self.size - self.x - 1, self.size - 1, 'column', -1
                if self.direction == -1:
                    return 0, self.size - self.x - 1, 0, 'column', 1
        if self.face == 2:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 3, 0, self.y, 'row', 1
                if self.direction == -1:
                    return 1, self.size - 1, self.y, 'row', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 4, 0, self.size - self.x - 1, 'row', 1
                if self.direction == -1:
                    return 0, 0, self.x, 'row', 1
        if self.face == 3:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 5, self.size - self.y - 1, 0, 'column', 1
                if self.direction == -1:
                    return 2, self.size - 1, self.y, 'row', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 4, self.x, 0, 'column', 1
                if self.direction == -1:
                    return 0, self.x, self.size - 1, 'column', -1
        if self.face == 4:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 5, 0, self.y, 'row', 1
                if self.direction == -1:
                    return 2, self.size - self.y - 1, self.size - 1, 'column', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 1, self.size - self.x - 1, self.size - 1, 'column', -1
                if self.direction == -1:
                    return 3, self.x, self.size - 1, 'column', -1
        if self.face == 5:
            if self.dimension == 'row':
                if self.direction == 1:
                    return 0, self.size - 1, self.size - self.y - 1, 'row', -1
                if self.direction == -1:
                    return 4, self.size - 1, self.y, 'row', -1
            if self.dimension == 'column':
                if self.direction == 1:
                    return 1, self.size - 1, self.size - self.x - 1, 'row', 1
                if self.direction == -1:
                    return 3, self.size - 1, self.size - self.x - 1, 'row', -1

    def walk(self, steps):
        for k in range(steps):
            if self.dimension == 'row':
                if self.direction == 1:
                    if self.x == self.size - 1:
                        face, x, y, dimension, direction = self.get_adjacent_cube_coordinates()
                        if self.faces[face][y][x] == '#':
                            break
                        else:
                            self.face, self.x, self.y, self.dimension, self.direction = face, x, y, dimension, direction
                    elif self.faces[self.face][self.y][self.x + 1] == '#':
                        break
                    else:
                        if self.faces[self.face][self.y][self.x + 1] != '.':
                            raise
                        self.x += 1

                elif self.direction == -1:
                    if self.x == 0:
                        face, x, y, dimension, direction = self.get_adjacent_cube_coordinates()
                        if self.faces[face][y][x] == '#':
                            break
                        else:
                            self.face, self.x, self.y, self.dimension, self.direction = face, x, y, dimension, direction
                    elif self.faces[self.face][self.y][self.x - 1] == '#':
                        break
                    else:
                        if self.faces[self.face][self.y][self.x - 1] != '.':
                            raise
                        self.x -= 1

            elif self.dimension == 'column':
                if self.direction == 1:
                    if self.y == self.size - 1:
                        face, x, y, dimension, direction = self.get_adjacent_cube_coordinates()
                        if self.faces[face][y][x] == '#':
                            break
                        else:
                            self.face, self.x, self.y, self.dimension, self.direction = (face, x, y, dimension, direction)
                    elif self.faces[self.face][self.y + 1][self.x] == '#':
                        break
                    else:
                        self.y += 1

                elif self.direction == -1:
                    if self.y == 0:
                        face, x, y, dimension, direction = self.get_adjacent_cube_coordinates()
                        if self.faces[face][y][x] == '#':
                            break
                        else:
                            self.face, self.x, self.y, self.dimension, self.direction = face, x, y, dimension, direction
                    elif self.faces[self.face][self.y - 1][self.x] == '#':
                        break
                    else:
                        self.y -= 1

    def turn(self, rotation: str):
        if rotation == 'R':
            self.dimension, self.direction = self.directions[
                (self.directions.index([self.dimension, self.direction]) + 1) % 4]
        if rotation == 'L':
            self.dimension, self.direction = self.directions[
                (self.directions.index([self.dimension, self.direction]) - 1) % 4]





if __name__ == "__main__":
    size = 4
    f0 = [string.strip() for string in puzzle_input[:size]]
    f1 = [string[:size] for string in puzzle_input[size:2*size]]
    f2 = [string[size:2*size] for string in puzzle_input[size:2*size]]
    f3 = [string[2*size:3*size] for string in puzzle_input[size:2*size]]
    f4 = [string.strip()[:size] for string in puzzle_input[2*size:-2]]
    f5 = [string.strip()[size:] for string in puzzle_input[2*size:-2]]


    cube = CubeMap([f0, f1, f2, f3, f4, f5])
    directions = puzzle_input[-1]
    k = 0
    string = ''
    while k < len(directions):
        try:
            int(directions[k])
            string += directions[k]
        except:
            cube.walk(int(string))
            cube.turn(directions[k])
            string = ''
        k += 1
    cube.walk(int(string))
    if cube.face == 2:
        column = cube.x + size
        row = cube.y + size
        print(1000 * (row+ 1) + 4 * (column + 1) + cube.directions.index(
            [cube.dimension, cube.direction]))


