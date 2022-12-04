from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

count = 0
for pair in puzzle_input:
    split_pair = pair.split(',')
    pair1 = split_pair[0].split('-')
    pair2 = split_pair[1].split('-')
    if int(pair1[0]) <= int(pair2[0]):
        if int(pair1[1]) >= int(pair2[1]):
            count += 1
        elif int(pair1[0]) == int(pair2[0]):
            if int(pair1[1]) <= int(pair2[1]):
                count += 1
    elif int(pair1[0]) >= int(pair2[0]):
        if int(pair1[1]) <= int(pair2[1]):
            count += 1
print(count)


count = 0
for pair in puzzle_input:
    split_pair = pair.split(',')
    pair1 = split_pair[0].split('-')
    pair2 = split_pair[1].split('-')
    if int(pair1[0]) < int(pair2[0]):
        if int(pair1[1]) >= int(pair2[0]):
            count += 1
        elif int(pair1[0]) == int(pair2[0]):
            count += 1
    elif int(pair1[0]) >= int(pair2[0]):
        if int(pair2[1]) >= int(pair1[0]):
            count += 1
print(count)
