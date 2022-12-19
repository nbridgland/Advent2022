from python.util import read_file
import itertools
import time
from copy import deepcopy

time1 = time.time()

filename = 'input.txt'

puzzle_input = read_file(filename)

parsed_input = {entry.split(' ')[1]: {'flow_rate': int(entry.split('rate=')[1].split(';')[0]),
                                      'dest_nodes': [valve.split(',')[0] for valve in entry.split(' ')[9:]]} for entry in puzzle_input}

non_zero_flows = [valve for valve in parsed_input if parsed_input[valve]['flow_rate'] > 0]
cave_valves = {entry: parsed_input[entry]['flow_rate'] for entry in parsed_input if parsed_input[entry]['flow_rate']>0}

distance_map = {}


def find_min_distance(valve1, valve2, visited=[]):
    visited = [node for node in visited] + [valve1]
    if valve2 in parsed_input[valve1]['dest_nodes']:
        return 1
    elif (valve1, valve2) in distance_map:
        return distance_map[(valve1, valve2)]
    else:
        return 1 + min([find_min_distance(node, valve2, visited) for node in parsed_input[valve1]['dest_nodes'] if node not in visited]+[1000])


print("Establishing distances")
for valve_pair in itertools.combinations(parsed_input.keys(), 2):
    distance_map[valve_pair] = find_min_distance(valve_pair[0], valve_pair[1])
time2 = time.time()
print(f"Distances found in {time2 - time1} seconds")


def get_distance(valve1, valve2):
    if valve1 == valve2:
        return 0
    else:
        if (valve1, valve2) in distance_map:
            return distance_map[(valve1, valve2)]
        return distance_map[(valve2, valve1)]


class Thing:
    def __init__(self, current_location='AA', timer=-1, destination='AA'):
        self.current_location = current_location
        self.timer = timer
        self.destination = destination

    def iterate(self, steps):
        self.timer -= steps

    def complete_move(self):
        self.current_location = self.destination

    def update_path(self, timer, destination):
        return Thing(self.current_location, timer, destination)


class Map:
    def __init__(self, things, valves=deepcopy(cave_valves), flow_rate=0, time=0, relieved_pressure=0):
        self.closed_valves = valves
        self.flow_rate = flow_rate
        self.time = time
        self.relieved_pressure = relieved_pressure
        self.things = things

    def iterate(self, steps=1):
        self.relieved_pressure += self.flow_rate * steps
        self.time += steps
        for thing in self.things:
            thing.iterate(steps)

    def fast_forward(self):
        steps = min(thing.timer for thing in self.things)
        if steps < 0:
            raise
        self.iterate(steps + 1)
        for thing in self.things:
            if thing.timer <= 0:
                thing.complete_move()
            if thing.timer == -1:
                self.flow_rate += self.closed_valves[thing.destination]
                del self.closed_valves[thing.destination]

    def update(self, things):
        if len(things) == len(self.things):
            return Map(things, deepcopy(self.closed_valves), self.flow_rate, self.time, self.relieved_pressure)
        elif self.things[0].current_location == things[0].current_location:
            return Map([things[0], deepcopy(self.things[1])], deepcopy(self.closed_valves), self.flow_rate, self.time, self.relieved_pressure)
        elif self.things[1].current_location == things[0].current_location:
            return Map([things[0], deepcopy(self.things[0])], deepcopy(self.closed_valves), self.flow_rate, self.time, self.relieved_pressure)

    def drop_thing(self, thing, inplace=True):
        if inplace:
            self.things = [thing]
        else:
            return Map([thing], deepcopy(self.closed_valves), self.flow_rate, self.time, self.relieved_pressure)


def iterate_map(cave_map: Map, max_time=30):
    if cave_map.time > max_time:
        raise
    to_delete = [valve for valve in cave_map.closed_valves if max([get_distance(thing.destination, valve)
                                                                   for thing in cave_map.things]) > max_time - 1]
    for valve in to_delete:
        print(valve)
        del cave_map.closed_valves[valve]
    maps = []
    if sum([thing.current_location == thing.destination for thing in cave_map.things]) == 2:
        if sum([thing.timer == -1 for thing in cave_map.things]) == 2:
            return do_the_giant_pair_thing(cave_map)
    for thing in cave_map.things:
        if thing.current_location == thing.destination and thing.timer == -1:
            for valve in cave_map.closed_valves:
                if not max(thingie.destination == valve for thingie in cave_map.things):
                    timer = get_distance(thing.current_location, valve)
                    if timer + cave_map.time < max_time - 1:
                        new_thing = thing.update_path(timer, valve)
                        new_map = cave_map.update([new_thing])
                        if new_map.things[0].timer == -1:
                            raise
                        if len(new_map.things) > 1:
                            if new_map.things[1].timer == -1:
                                raise
                        new_map.fast_forward()
                        maps.append(new_map)
    if len(maps) > 0:
        return max([iterate_map(new_map, max_time) for new_map in maps])
    else:
        # either one thing still needs to finish
        for thing in cave_map.things:
            if thing.current_location != thing.destination:
                new_map = cave_map.drop_thing(thing, inplace=False)
                new_map.fast_forward()
                return iterate_map(new_map, max_time)
        # or it just needs to complete
        if max_time < cave_map.time:
            raise
        cave_map.iterate(steps=max_time-cave_map.time)
        return cave_map.relieved_pressure


def do_the_giant_pair_thing(cave_map, max_time=26):
    maps = []
    if len(cave_map.closed_valves) == 1:
        valve = list(cave_map.closed_valves.keys())[0]
        timer1 = get_distance(cave_map.things[0].current_location, valve)
        timer2 = get_distance(cave_map.things[1].current_location, valve)
        if timer1 < timer2:
            new_thing = cave_map.things[0].update_path(timer1, valve)
            new_map = cave_map.drop_thing(new_thing, inplace=False)
            new_map.fast_forward()
            return iterate_map(new_map, max_time)
        else:
            new_thing = cave_map.things[1].update_path(timer2, valve)
            new_map = cave_map.drop_thing(new_thing, inplace=False)
            new_map.fast_forward()
            return iterate_map(new_map, max_time)
    for combination in itertools.combinations(cave_map.closed_valves.keys(), 2):
        if cave_map.things[0].current_location == cave_map.things[1].current_location:
            combinations = [combination]  # can cut overall time by half here at least, since things are interchangeable
        else:
            combinations = [(combination[0], combination[1]), (combination[1], combination[0])]
        for valve_pair in combinations:
            timer1 = get_distance(cave_map.things[0].current_location, valve_pair[0])
            timer2 = get_distance(cave_map.things[1].current_location, valve_pair[1])
            if timer1 + cave_map.time < max_time - 1:
                newthing1 = cave_map.things[0].update_path(timer1, valve_pair[0])
                if timer2 + cave_map.time < max_time - 1:
                    newthing2 = cave_map.things[1].update_path(timer2, valve_pair[1])
                    new_map = cave_map.update([newthing1, newthing2])
                else:
                    new_map = cave_map.drop_thing(newthing1, inplace=False)
                new_map.fast_forward()
                maps.append(new_map)
            elif timer2 + cave_map.time < max_time - 1:
                newthing1 = cave_map.things[1].update_path(timer2, valve_pair[1])
                new_map = cave_map.drop_thing(newthing1, inplace=False)
                new_map.fast_forward()
                maps.append(new_map)
    if len(maps) > 0:  # happens in actual but not in test
        return max([iterate_map(new_map, max_time) for new_map in maps])
    else:
        if max_time < cave_map.time:
            raise
        cave_map.iterate(steps=max_time-cave_map.time)
        return cave_map.relieved_pressure


print("Running the real algorithm")
thing = Thing()
start_map = Map([thing])
print("Part 1: ", iterate_map(start_map))
time3 = time.time()
print(f"Part 1 run in {time3 - time2} seconds")
print("Running Part 2")
thing1 = Thing()
thing2 = Thing()
start_map = Map([thing1, thing2])
print("Part 2: ", iterate_map(start_map, max_time=26))
time4 = time.time()
print(f"Part 2 run in {time4 - time3} seconds")
