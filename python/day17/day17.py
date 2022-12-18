from python.util import read_file
import itertools
import time
import numpy as np


filename = 'input.txt'
puzzle_input = read_file(filename)[0]


class Rock:
    def __init__(self, number):
        self.number = number % 5
        if self.number == 0:
            self.width, self.height = [4, 1]
        if self.number == 1:
            self.width, self.height = [3, 3]
        if self.number == 2:
            self.width, self.height = [3, 3]
        if self.number == 3:
            self.width, self.height = [1, 4]
        if self.number == 4:
            self.width, self.height = [2, 2]
        if self.number == 1:
            self.coord_list = [(1, 0), (1, 1), (1, 2), (2, 1), (0, 1)]
        elif self.number == 2:
            self.coord_list = [(2, 0), (2, 1), (2, 2), (0, 2), (1, 2)]
        else:
            self.coord_list = [(i, j) for i in range(self.height) for j in range(self.width)]


class Tower:
    def __init__(self, puzzle_input):
        self.map = [['.' for j in range(7)] for k in range(20000)]
        self.map[0] = ['#' for j in range(7)]
        self.highest_rock = 0
        self.jet_stream = puzzle_input
        self.rock_number = 0
        self.jet_stream_index = 0

    def draw_rock(self, rock:Rock, start_coordinate):
        for coordinates in rock.coord_list:
            self.map[start_coordinate[0] - coordinates[0]][start_coordinate[1] + coordinates[1]] = '#'
        self.highest_rock = max(self.highest_rock, start_coordinate[0])

    def check_space(self, rock:Rock, coordinate):
        for coordinates in rock.coord_list:
            if self.map[coordinate[0] - coordinates[0]][coordinate[1] + coordinates[1]] == '#':
                return False
        return True

    def check_down(self, rock: Rock, start_coordinate):
        if start_coordinate[0] - rock.height > self.highest_rock + 1:
            return True
        if start_coordinate[0] - rock.height == 0:
            return False
        else:
            return self.check_space(rock, (start_coordinate[0]-1, start_coordinate[1]))

    def get_jetstream(self):
        self.jet_stream_index = (self.jet_stream_index + 1) % len(self.jet_stream)
        return self.jet_stream[self.jet_stream_index - 1]

    def blow_rock(self, rock: Rock, start_coordinates, direction):
        if direction == '>':
            if start_coordinates[1] + rock.width == 7:
                return start_coordinates
            else:
                if self.check_space(rock, (start_coordinates[0], start_coordinates[1] + 1)):
                    return (start_coordinates[0], start_coordinates[1] + 1)
                return start_coordinates
        else:
            if start_coordinates[1] == 0:
                return start_coordinates
            else:
                if self.check_space(rock, (start_coordinates[0], start_coordinates[1] - 1)):
                    return (start_coordinates[0], start_coordinates[1] - 1)
                return start_coordinates

    def drop_rock(self, rock: Rock):
        direction = self.get_jetstream()
        if direction == '<':
            current_coordinate = (self.highest_rock + rock.height + 3, 1)
        else:
            current_coordinate = (self.highest_rock + rock.height + 3, 3)
        while self.check_down(rock, current_coordinate):
            current_coordinate = (current_coordinate[0] - 1, current_coordinate[1])
            current_coordinate = self.blow_rock(rock, current_coordinate, self.get_jetstream())
        self.draw_rock(rock, current_coordinate)


def get_column_height(column):
    j = 0
    while tower.map[tower.highest_rock - j][column] == '.':
        j += 1
    return j


if __name__ == "__main__":
    time1 = time.time()
    tower = Tower(puzzle_input)
    for k in range(2022):
        rock = Rock(k)
        tower.drop_rock(rock)
    print("Part 1:", tower.highest_rock)
    time2 = time.time()
    print("Part 1 execution time: ", time2-time1)

    # Part 2
    time1 = time.time()
    state_dict = {}
    tower = Tower(puzzle_input)
    k = 0
    found_state = False
    n_rocks = 1000000000000
    while k < n_rocks:
        rock = Rock(k)
        tower.drop_rock(rock)
        state = tuple([get_column_height(column) for column in range(7)])

        if not found_state:
            if state in state_dict:
                for entry in state_dict[state]:
                    if entry['rock_index'] == k % 5 and entry['jet_stream_index'] == tower.jet_stream_index:
                        found_state = True
                        height_diff = tower.highest_rock - entry['highest_rock']
                        rock_diff = k - entry['rock_number']
                        iterations_skipped = (n_rocks - k)//rock_diff
                        k += iterations_skipped*rock_diff
                        height_adjustment = iterations_skipped*height_diff
                state_dict[state].append({'rock_index': k % 5, 'jet_stream_index': tower.jet_stream_index,
                                          'rock_number': k, 'highest_rock': tower.highest_rock})
            else:
                state_dict[state] = [{'rock_index': k % 5, 'jet_stream_index': tower.jet_stream_index,
                                      'rock_number': k, 'highest_rock': tower.highest_rock}]
        k += 1
    time2 = time.time()
    print("Part 2 execution time: ", time2 - time1)
    print("Part 2: ", tower.highest_rock + height_adjustment)