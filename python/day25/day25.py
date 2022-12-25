from python.util import read_file

filename = 'input.txt'
puzzle_input = read_file(filename)


def translate_from_snafu(string):
    output = 0
    max_power = len(string)
    for k in range(max_power):
        if string[k] == '=':
            output -= 2*5**(max_power-k-1)
        if string[k] == '-':
            output -= 5**(max_power-k-1)
        if string[k] == '1':
            output += 5**(max_power-k-1)
        if string[k] == '2':
            output += 2*5**(max_power-k-1)
    return output


def translate_to_snafu(number):
    if number == 0:
        return ''
    if number % 5 == 0:
        return translate_to_snafu(number//5) + '0'
    if number % 5 == 1:
        return translate_to_snafu((number-1)//5) + '1'
    if number % 5 == 2:
        return translate_to_snafu((number-2)//5) + '2'
    if number % 5 == 3:
        return translate_to_snafu((number+2)//5) + '='
    if number % 5 == 4:
        return translate_to_snafu((number+1)//5) + '-'


output_number = sum([translate_from_snafu(line) for line in puzzle_input])
print(translate_to_snafu(output_number))
