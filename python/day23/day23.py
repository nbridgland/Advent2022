from python.util import read_file


filename = 'input.txt'

puzzle_input = read_file(filename)
steps = 10
expansion = 100
field_map = [[0 for x in range(len(puzzle_input[0]) + 100)] for y in range(len(puzzle_input) + 100)]
elf_locations = []
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[0])):
        if puzzle_input[y][x] == '#':
            field_map[y+10][x+10] = 1
            elf_locations.append((x+10, y+10))


def is_adjacent_elf(location):
    x,y = location
    if field_map[y-1][x-1]:
        return True
    if field_map[y-1][x]:
        return True
    if field_map[y-1][x+1]:
        return True
    if field_map[y][x-1]:
        return True
    if field_map[y][x+1]:
        return True
    if field_map[y+1][x-1]:
        return True
    if field_map[y+1][x]:
        return True
    if field_map[y+1][x+1]:
        return True
    return False


def make_proposal(location, first_proposal_index):
    x,y = location
    proposal_order = ['north', 'south', 'west', 'east']
    for k in range(4):
        proposal_direction = proposal_order[(first_proposal_index + k) % 4]
        if proposal_direction == 'south':
            if field_map[y+1][x-1] or field_map[y+1][x] or field_map[y+1][x+1]:
                continue
            return (x, y+1)
        if proposal_direction == 'north':
            if field_map[y-1][x-1] or field_map[y-1][x] or field_map[y-1][x+1]:
                continue
            return (x, y-1)
        if proposal_direction == 'west':
            if field_map[y-1][x-1] or field_map[y][x-1] or field_map[y+1][x-1]:
                continue
            return (x-1, y)
        if proposal_direction == 'east':
            if field_map[y-1][x+1] or field_map[y][x+1] or field_map[y+1][x+1]:
                continue
            return (x+1, y)
    return (x,y)



first_proposal_index = 0
for k in range(steps):
    proposal_map = [[0 for x in range(len(field_map[0]))] for y in range(len(field_map))]
    proposals = {}
    for location in elf_locations:
        if is_adjacent_elf(location):
            proposal = make_proposal(location, first_proposal_index)
            proposals[location] = proposal
            proposal_map[proposal[1]][proposal[0]] += 1
        else:
            proposals[location] = location
    new_map = [[0 for x in range(len(field_map[0]))] for y in range(len(field_map))]
    elf_locations = []
    for proposal in proposals:
        new_loc = proposals[proposal]
        if proposal_map[new_loc[1]][new_loc[0]] < 2:
            new_map[new_loc[1]][new_loc[0]] = 1
            elf_locations.append(new_loc)
        else:
            new_map[proposal[1]][proposal[0]] = 1
            elf_locations.append(proposal)
    field_map = new_map
    first_proposal_index += 1

min_x = min([x for x in range(len(field_map[0])) if max([field_map[y][x] for y in range(len(field_map))])>0])
max_x = max([x for x in range(len(field_map[0])) if max([field_map[y][x] for y in range(len(field_map))])>0])
min_y = min([y for y in range(len(field_map)) if max([field_map[y][x] for x in range(len(field_map[0]))])>0])
max_y = max([y for y in range(len(field_map)) if max([field_map[y][x] for x in range(len(field_map[0]))])>0])


print("Part 1:", (max_x - min_x + 1)*(max_y - min_y + 1) - len(elf_locations))
elf_moved = True
while elf_moved:
    elf_moved = False
    proposal_map = [[0 for x in range(len(field_map[0]))] for y in range(len(field_map))]
    proposals = {}
    for location in elf_locations:
        if is_adjacent_elf(location):
            proposal = make_proposal(location, first_proposal_index)
            proposals[location] = proposal
            proposal_map[proposal[1]][proposal[0]] += 1
        else:
            proposals[location] = location
    new_map = [[0 for x in range(len(field_map[0]))] for y in range(len(field_map))]
    elf_locations = []
    for proposal in proposals:
        new_loc = proposals[proposal]
        if proposal_map[new_loc[1]][new_loc[0]] < 2:
            if new_loc[1] != proposal[1]:
                elf_moved = True
            if new_loc[0] != proposal[0]:
                elf_moved = True
            new_map[new_loc[1]][new_loc[0]] = 1
            elf_locations.append(new_loc)
        else:
            new_map[proposal[1]][proposal[0]] = 1
            elf_locations.append(proposal)
    field_map = new_map
    first_proposal_index += 1
    steps += 1

print("Part 2", steps)