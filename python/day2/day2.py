from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

elf_dict = {'A': 0, 'B': 1, 'C': 2}
me_dict = {'X': 0, 'Y': 1, 'Z': 2}

def check_score(string):
    elf = elf_dict[string[0]]
    me = me_dict[string[2]]
    if elf == me:
        return 4 + me
    if (elf + 1) % 3 == me:
        return 7 + me
    return 1 + me


def score_choose_play(string):
    elf = elf_dict[string[0]]
    outcome = string[2]
    if outcome == 'X':
        return 1 + ((elf-1) % 3)
    if outcome == 'Y':
        return 4 + (elf % 3)
    if outcome == 'Z':
        return 7 + ((elf+1) % 3)

if __name__ == "__main__":
    total = 0
    for entry in puzzle_input:
        total += check_score(entry)
    print(f"Part 1: {total}")

    total = 0
    for entry in puzzle_input:
        total += score_choose_play(entry)
    print(f"Part 2: {total}")
