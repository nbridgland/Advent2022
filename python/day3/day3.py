from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

def find_duplicates(line1, line2):
    duplicates = []
    for k in range(len(line1)):
        for j in range(len(line2)):
            if line1[k] == line2[j]:
                duplicates.append(line1[k])
    return duplicates

def score(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-64 + 26

if __name__ == "__main__":
    print("Part 1:", sum([score(find_duplicates(line[:len(line)//2], line[len(line)//2:])[0]) for line in puzzle_input]))

    # Part 2:
    total=0
    for k in range(len(puzzle_input)//3):
        dup1 = find_duplicates(puzzle_input[3*k], puzzle_input[3*k+1])
        dup2 = find_duplicates(puzzle_input[3*k+1], puzzle_input[3*k+2])
        total += score(find_duplicates(dup1, dup2)[0])
    print("Part 2:", total)

