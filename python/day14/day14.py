from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)


class Map:
    def __init__(self, parsed_input):
        self.min_x = min([min([entry[0] for entry in line]) for line in parsed_input])
        self.max_x = max([max([entry[0] for entry in line]) for line in parsed_input])
        self.min_y = 0
        self.max_y = max([max([entry[1] for entry in line]) for line in parsed_input])
        self.map = [['.' for x in range(self.min_x, self.max_x+1)] for y in range(self.min_y, self.max_y+1)]
        for line in parsed_input:
            for k in range(len(line)-1):
                entry1 = line[k]
                entry2 = line[k+1]
                if entry1[0] > entry2[0]:
                    j = 0
                    while entry2[0] + j <= entry1[0]:
                        self.map[entry2[1]-self.min_y][entry2[0] - self.min_x + j] = '#'
                        j += 1
                elif entry1[1] < entry2[1]:
                    j = 0
                    while entry1[1] + j <= entry2[1]:
                        self.map[entry1[1]-self.min_y+j][entry2[0] - self.min_x] = '#'
                        j += 1
                elif entry1[1] > entry2[1]:
                    j = 0
                    while entry1[1] - j >= entry2[1]:
                        self.map[entry1[1]-self.min_y-j][entry2[0] - self.min_x] = '#'
                        j += 1
                elif entry1[0] < entry2[0]:
                    j = 0
                    while entry2[0] - j >= entry1[0]:
                        self.map[entry2[1]-self.min_y][entry2[0] - self.min_x - j] = '#'
                        j += 1

    def drop_sand(self):
        last_pos = None
        new_pos = [0, 500 - self.min_x]
        while new_pos != last_pos:
            last_pos = new_pos
            try:
                if self.map[new_pos[0] + 1][new_pos[1]] == '.':
                    new_pos = [new_pos[0] + 1, new_pos[1]]
                elif self.map[new_pos[0] + 1][new_pos[1] - 1] == '.':
                    new_pos = [new_pos[0] + 1, new_pos[1] - 1]
                elif self.map[new_pos[0] + 1][new_pos[1] + 1] == '.':
                    new_pos = [new_pos[0] + 1, new_pos[1] + 1]
            except IndexError:
                return True
        self.map[new_pos[0]][new_pos[1]] = 'o'
        return False


class Map2:
    def __init__(self, parsed_input):
        self.min_x = min([min([entry[0] for entry in line]) for line in parsed_input]) - 200 # doesn't really matter (???)
        self.max_x = max([max([entry[0] for entry in line]) for line in parsed_input]) + 200 # doesn't really matter (???)
        self.min_y = 0
        self.max_y = max([max([entry[1] for entry in line]) for line in parsed_input]) + 2
        self.map = [['.' for x in range(self.min_x, self.max_x+1)] for y in range(self.min_y, self.max_y+1)]
        self.map[self.max_y] = ['#' for x in range(self.min_x, self.max_x+1)]
        for line in parsed_input:
            for k in range(len(line)-1):
                entry1 = line[k]
                entry2 = line[k+1]
                if entry1[0] > entry2[0]:
                    j = 0
                    while entry2[0] + j <= entry1[0]:
                        self.map[entry2[1]-self.min_y][entry2[0] - self.min_x + j] = '#'
                        j += 1
                elif entry1[1] < entry2[1]:
                    j = 0
                    while entry1[1] + j <= entry2[1]:
                        self.map[entry1[1]-self.min_y+j][entry2[0] - self.min_x] = '#'
                        j += 1
                elif entry1[1] > entry2[1]:
                    j = 0
                    while entry1[1] - j >= entry2[1]:
                        self.map[entry1[1]-self.min_y-j][entry2[0] - self.min_x] = '#'
                        j += 1
                elif entry1[0] < entry2[0]:
                    j = 0
                    while entry2[0] - j >= entry1[0]:
                        self.map[entry2[1]-self.min_y][entry2[0] - self.min_x - j] = '#'
                        j += 1


    def drop_sand(self):
        last_pos = None
        new_pos = [0, 500-self.min_x]
        while new_pos != last_pos:
            last_pos = new_pos
            try:
                if self.map[new_pos[0]+1][new_pos[1]] == '.':
                    new_pos = [new_pos[0]+1, new_pos[1]]
                elif self.map[new_pos[0]+1][new_pos[1]-1] == '.':
                    new_pos = [new_pos[0]+1, new_pos[1]-1]
                elif self.map[new_pos[0]+1][new_pos[1]+1] == '.':
                    new_pos = [new_pos[0]+1, new_pos[1]+1]
            except IndexError:
                raise "Out of map!"
        self.map[new_pos[0]][new_pos[1]] = 'o'


if __name__ == "__main__":
    #Part 1
    parsed = [[[int(entry) for entry in part.split(',')] for part in line.split(' -> ')] for line in puzzle_input]
    cave_map = Map(parsed)
    j = 0
    out_of_map = False
    while not out_of_map:
        out_of_map = cave_map.drop_sand()
        j += 1
        if j % 100 == 0:
            print(j)
    print("Part 1 units of sand: ", j-1)

    # Part 2
    cave_map = Map2(parsed)
    j = 0
    while cave_map.map[0][500-cave_map.min_x] != 'o':
        cave_map.drop_sand()
        j += 1
        if j % 100 == 0:
            print(j)
    print("Part 2 units of sand: ", j)


