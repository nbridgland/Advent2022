from python.util import read_file
filename = 'input.txt'

puzzle_input = read_file(filename)

directory_info = {}
current_path = ['/']
for line in puzzle_input:
    parsed = line.split(' ')
    if parsed[0] == '$':
        command = parsed[1:]
        if command[0] == 'cd':
            if command[1] == '/':
                current_path = ['/']
            elif command[1] == '..':
                current_path.pop()
            else:
                current_path.append(command[1]+'/')
        if command[0] == 'ls':
            pass
    else:
        path = ''.join(current_path)
        if path not in directory_info:
            directory_info[path] = {}
        if parsed[0] == 'dir':
            directory_info[path][parsed[1]] = {}
        else:
            directory_info[path][parsed[1]] = int(parsed[0])

size_info = {}

def size_count(info, path='/'):
    size = 0
    for entry in info:
        if type(info[entry]) == dict:
            if entry.startswith('/'):
                new_path = entry
            else:
                new_path = path+entry+'/'
            size_info[entry] = size_count(directory_info[new_path], path=new_path)
            size += size_info[entry]
        else:
            size += info[entry]
    return size

size_count(directory_info)

# Part 1
output = 0
for entry in size_info:
    if not entry.startswith('/'):
        continue
    if size_info[entry] <= 100000:
        output += size_info[entry]
print(output)

# Part 2
total_disk_space = 70000000
needed_disk_space = 30000000
to_free = needed_disk_space - (total_disk_space - size_info['/'])

possible_min = total_disk_space
for entry in size_info:
    if not entry.startswith('/'):
        continue
    if size_info[entry] >= to_free:
        if size_info[entry] < possible_min:
            possible_min = size_info[entry]
print(possible_min)
