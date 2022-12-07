from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)[0]

def check_sequence(string):
    for k in range(len(string)):
        for j in range(k+1, len(string)):
            if string[k] == string[j]:
                return False
    return True

# Part 1

k=0
input_sequence_found = False
while not input_sequence_found:
    input_sequence_found = check_sequence(puzzle_input[k:k+4])
    k+=1

print("Input Sequence: ", puzzle_input[k-1:k-1+4])
print(k-1+4)


#Part 2
input_sequence_found = False
while not input_sequence_found:
    input_sequence_found = check_sequence(puzzle_input[k:k+14])
    k+=1

print("Input Sequence: ", puzzle_input[k-1:k-1+14])
print(k-1+14)