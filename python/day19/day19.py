from python.util import read_file
import time
from copy import deepcopy
import numpy as np

time1 = time.time()

filename = 'input.txt'

puzzle_input = read_file(filename)


def inverse_triangle(n):
    output = 0
    k = 1
    while output < n:
        output += k
        k += 1
    return k - 1


class Blueprint:
    def __init__(self, line):
        instructions = line.split(':')[1].split('. ')
        self.ore = {instructions[0].split(' ')[-1]: int(instructions[0].split(' ')[-2])}
        self.clay = {instructions[1].split(' ')[-1]: int(instructions[1].split(' ')[-2])}
        self.obsidian = {instructions[2].split(' ')[-1]: int(instructions[2].split(' ')[-2]),
                         instructions[2].split(' ')[-4]: int(instructions[2].split(' ')[-5])}
        self.geode = {instructions[3].split(' ')[-1]: int(instructions[3].split(' ')[-2]),
                         instructions[3].split(' ')[-4]: int(instructions[3].split(' ')[-5])}
        self.min_obsidian_time = max_time - inverse_triangle(self.geode['obsidian.'])
        self.min_clay_time = self.min_obsidian_time - inverse_triangle(self.obsidian['clay'])
        # Maximum number of robots it reasonably makes sense to have
        self.max_ore = max(self.clay['ore'], self.obsidian['ore'], self.geode['ore'])
        self.max_clay = self.obsidian['clay']
        self.max_obsidian = self.geode['obsidian.']

    def get_cost(self, k):
        if k == 0:
            entry = self.ore
        if k == 1:
            entry = self.clay
        if k == 2:
            entry = self.obsidian
        if k == 3:
            entry = self.geode
        output = [0 for j in range(4)]
        output[0] = entry['ore']
        if 'clay' in entry:
            output[1] = entry['clay']
        if 'obsidian.' in entry:  # little silly to deal with data parsing issues this way
            output[2] = entry['obsidian.']
        return output


class Counter:
    def __init__(self, blueprint: Blueprint, time=0, resources=[0, 0, 0, 0], robots=[1, 0, 0, 0]):
        self.resources = resources
        self.robots = robots
        self.blueprint = blueprint
        self.time = time
        self.max_time = max_time

    def iterate(self):
        for k in range(4):
            self.resources[k] += self.robots[k]
        self.time += 1

    def buy(self, k):
        cost = self.blueprint.get_cost(k)
        for j in range(4):
            while cost[j] > self.resources[j]:
                if self.time == self.max_time:
                    return None
                self.iterate()
        for j in range(4):
            self.resources[j] -= cost[j]
        if self.time == self.max_time:
            return None
        self.iterate()
        self.robots[k] += 1

    def get_available_options(self):
        options = [0, 1]
        if self.robots[1] > 0:
            options = [0, 1, 2]
        if self.robots[2] > 0:
            options = [0, 1, 2, 3]
        return options

    def copy(self):
        return Counter(self.blueprint, time=self.time, robots=deepcopy(self.robots), resources=deepcopy(self.resources))


def find_max_geodes(counter, max_time):
    if counter.time == max_time:
        return counter.resources[3]
    if counter.time >= max_time:
        raise
    if counter.robots[0] > counter.blueprint.max_ore:
        return 0
    if counter.robots[1] > counter.blueprint.max_clay:
        return 0
    if counter.robots[2] > counter.blueprint.max_obsidian:
        return 0
    if counter.blueprint.min_obsidian_time < counter.time:
        if counter.robots[2] == 0:
            return 0
        if counter.blueprint.min_clay_time < counter.time:
            if counter.robots[1] == 0:
                return 0
    options = counter.get_available_options()
    counters = []
    for option in options:
        new_counter = counter.copy()
        new_counter.buy(option)
        counters.append(new_counter)
    return max(find_max_geodes(new_counter, max_time) for new_counter in counters)


if __name__ == "__main__":
    output = 0
    max_time = 24
    blueprints = [Blueprint(line) for line in puzzle_input]
    for k in range(len(blueprints)):
        print(k)
        init_counter = Counter(blueprints[k])
        max_output = find_max_geodes(init_counter, max_time)
        output += (k+1)*max_output
    print(output)

    time2 = time.time()
    print(time2 - time1, "seconds to run")

    # Part 2:
    output = 1
    max_time = 32
    blueprints = [Blueprint(line) for line in puzzle_input]
    for k in range(3):
        print(k)
        init_counter = Counter(blueprints[k])
        max_output = find_max_geodes(init_counter, max_time)
        print(max_output)
        time2 = time.time()
        print(time2-time1, "seconds to run iteration")
        time1 = time2
        output *= max_output
    print(output)
