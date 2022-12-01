from python.util import read_file
filename = 'input.txt'


puzzle_input = read_file(filename)

# part 1
max = 0
current_sum = 0
for entry in puzzle_input:
    if entry == '':
        if current_sum > max:
            max = current_sum
        current_sum = 0
    else:
        current_sum += int(entry)
print(max)


# part 2
max1 = 0
max2 = 0
max3 = 0
current_sum = 0
for entry in puzzle_input:
    if entry == '':
        print(current_sum)
        if current_sum >= max1:
            max3 = max2
            max2 = max1
            max1 = current_sum
        elif current_sum >= max2:
            max3 = max2
            max2 = current_sum
        elif current_sum >= max3:
            max3 = current_sum
        current_sum = 0
    else:
        current_sum += int(entry)
print(max1 + max2 + max3)