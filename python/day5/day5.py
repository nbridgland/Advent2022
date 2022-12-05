from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

if filename == 'testinput.txt':
    label_line = 4
else:
    label_line = 9

def clean_starting_position(input_list):
    columns = len(input_list[-1])//3
    output = [[] for k in range(columns)]
    for line in input_list[-2::-1]:
        for k in range(columns):
            if 1+4*k < len(line):
                if line[1+4*k] != ' ':
                    output[k].append(line[1+4*k])
    return output


def clean_instructions(input_list):
    output = []
    for line in input_list:
        split = line.split(' ')
        output.append({'quantity': int(split[1]),
                       'start': int(split[3])-1,
                       'destination': int(split[5])-1})
    return output


# Part 1
positions = clean_starting_position(puzzle_input[:label_line])
instructions = clean_instructions(puzzle_input[label_line+1:])
for line in instructions:
    k = 0
    while k < line['quantity']:
        positions[line['destination']].append(positions[line['start']].pop())
        k += 1

output = ''
for stack in positions:
    if len(stack) > 0:
        output += stack[-1]
    else:
        output += ' '
print(output)


# Part 2
positions = clean_starting_position(puzzle_input[:label_line])
instructions = clean_instructions(puzzle_input[label_line+1:])
for line in instructions:
    k = 0
    in_between = []
    while k < line['quantity']:
        in_between.append(positions[line['start']].pop())
        k += 1
    k = 0
    while k < line['quantity']:
        positions[line['destination']].append(in_between.pop())
        k += 1
output = ''
for stack in positions:
    if len(stack) > 0:
        output += stack[-1]
    else:
        output += ' '
print(output)