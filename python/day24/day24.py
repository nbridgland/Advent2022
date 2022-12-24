from python.util import read_file
import numpy as np

filename = 'input.txt'

puzzle_input = read_file(filename)


class ValleyMap:
    def __init__(self, puzzle_input):
        self.map = [[[char] for char in line[1:-1]] for line in puzzle_input[1:-1]]
        self.ysize = len(self.map)
        self.xsize = len(self.map[0])

    def iterate(self):
        new_map = [[[] for k in range(self.xsize)] for j in range(self.ysize)]
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                for direction in self.map[y][x]:
                    if direction == '^':
                        if y == 0:
                            new_map[self.ysize-1][x].append('^')
                        else:
                            new_map[y-1][x].append('^')
                    if direction == 'v':
                        if y == self.ysize - 1:
                            new_map[0][x].append('v')
                        else:
                            new_map[y+1][x].append('v')
                    if direction == '>':
                        if x == self.xsize - 1:
                            new_map[y][0].append('>')
                        else:
                            new_map[y][x+1].append('>')
                    if direction == '<':
                        if x == 0:
                            new_map[y][self.xsize -1].append('<')
                        else:
                            new_map[y][x-1].append('<')
        self.map = new_map


if __name__ == "__main__":
    vmap = ValleyMap(puzzle_input)
    exited = False
    pos_dict = {(0,0): 1}
    steps = 0
    while not exited:
        new_pos_dict = {(0,0): 1}  # could still be waiting at the entrance!
        for pos in pos_dict:
            new_pos_dict[(pos)] = 1 # could wait
            if pos[0] > 0:
                new_pos_dict[(pos[0]-1, pos[1])] = 1
            if pos[0] < (vmap.xsize - 1):
                new_pos_dict[(pos[0]+1, pos[1])] = 1
            if pos[1] > 0:
                new_pos_dict[(pos[0], pos[1]-1)] = 1
            if pos[1] < (vmap.ysize - 1):
                new_pos_dict[(pos[0], pos[1]+1)] = 1
        vmap.iterate()
        for pos in list(new_pos_dict.keys()):
            if vmap.map[pos[1]][pos[0]]:
                del new_pos_dict[pos]
        for pos in new_pos_dict:
            if pos[0] == vmap.xsize - 1:
                if pos[1] == vmap.ysize - 1:
                    exited = True
                    vmap.iterate()
                    steps += 1
        pos_dict = new_pos_dict
        steps += 1
    print("part 1:", steps)
    while vmap.map[vmap.ysize-1][vmap.xsize-1]:
        steps += 1
        vmap.iterate()

    #Head back to start
    pos_dict = {(vmap.xsize - 1, vmap.ysize - 1): 1}
    exited = False
    while not exited:
        new_pos_dict = {(vmap.xsize - 1, vmap.ysize - 1): 1}
        for pos in pos_dict:
            new_pos_dict[(pos)] = 1
            if pos[0] > 0:
                new_pos_dict[(pos[0]-1, pos[1])] = 1
            if pos[0] < (vmap.xsize - 1):
                new_pos_dict[(pos[0]+1, pos[1])] = 1
            if pos[1] > 0:
                new_pos_dict[(pos[0], pos[1]-1)] = 1
            if pos[1] < (vmap.ysize - 1):
                new_pos_dict[(pos[0], pos[1]+1)] = 1
        vmap.iterate()
        for pos in list(new_pos_dict.keys()):
            if vmap.map[pos[1]][pos[0]]:
                del new_pos_dict[pos]
        for pos in new_pos_dict:
            if pos[0] == 0:
                if pos[1] == 0:
                    exited = True
                    steps += 1
                    vmap.iterate()
        pos_dict = new_pos_dict
        steps += 1
    print("Back to start:", steps)

    while vmap.map[0][0]:
        vmap.iterate()
        steps += 1

    exited = False
    pos_dict = {(0,0): 1}
    while not exited:
        new_pos_dict = {(0,0): 1}
        for pos in pos_dict:
            new_pos_dict[pos] = 1
            if pos[0] > 0:
                new_pos_dict[(pos[0]-1, pos[1])] = 1
            if pos[0] < (vmap.xsize - 1):
                new_pos_dict[(pos[0]+1, pos[1])] = 1
            if pos[1] > 0:
                new_pos_dict[(pos[0], pos[1]-1)] = 1
            if pos[1] < (vmap.ysize - 1):
                new_pos_dict[(pos[0], pos[1]+1)] = 1
        vmap.iterate()
        for pos in list(new_pos_dict.keys()):
            if vmap.map[pos[1]][pos[0]]:
                del new_pos_dict[pos]
        for pos in new_pos_dict:
            if pos[0] == vmap.xsize - 1:
                if pos[1] == vmap.ysize - 1:
                    exited = True
                    vmap.iterate()
        pos_dict = new_pos_dict
        steps += 1

print("part 2:", steps+1)
