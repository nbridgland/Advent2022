from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)


class Rope:
    def __init__(self, name='A'):
        self.head_position = [0, 0]
        self.tail_position = [0, 0]
        self.visited = {'0,0': 1}
        self.name = name

    def follow_instruction(self, instruction):
        parsed = instruction.split(' ')
        for k in range(int(parsed[1])):
            self.move_head(parsed[0])
            self.move_tail(parsed[0])


    def move_head(self, direction):
        if direction == 'R':
            self.head_position[0] += 1
        if direction == 'L':
            self.head_position[0] -= 1
        if direction == 'U':
            self.head_position[1] += 1
        if direction == 'D':
            self.head_position[1] -= 1

    def move_tail(self, direction):
        if direction == 'R':
            if self.head_position[0] > self.tail_position[0] + 1:
                self.tail_position[0] += 1
                if self.head_position[1] > self.tail_position[1]:
                    self.tail_position[1] += 1
                elif self.head_position[1] < self.tail_position[1]:
                    self.tail_position[1] -= 1
        if direction == 'L':
            if self.head_position[0] < self.tail_position[0] - 1:
                self.tail_position[0] -= 1
                if self.head_position[1] > self.tail_position[1]:
                    self.tail_position[1] += 1
                elif self.head_position[1] < self.tail_position[1]:
                    self.tail_position[1] -= 1
        if direction == 'U':
            if self.head_position[1] > self.tail_position[1] + 1:
                self.tail_position[1] += 1
                if self.head_position[0] > self.tail_position[0]:
                    self.tail_position[0] += 1
                elif self.head_position[0] < self.tail_position[0]:
                    self.tail_position[0] -= 1
        if direction == 'D':
            if self.head_position[1] < self.tail_position[1] - 1:
                self.tail_position[1] -= 1
                if self.head_position[0] > self.tail_position[0]:
                    self.tail_position[0] += 1
                elif self.head_position[0] < self.tail_position[0]:
                    self.tail_position[0] -= 1
        if direction == 'DUR':
            if self.head_position[0] > self.tail_position[0] + 1:
                self.tail_position[0] += 1
                if self.head_position[1] > self.tail_position[1]:
                    self.tail_position[1] += 1
            elif self.head_position[1] > self.tail_position[1] + 1:
                self.tail_position[1] += 1
                if self.head_position[0] > self.tail_position[0]:
                    self.tail_position[0] += 1
        if direction == 'DUL':
            if self.head_position[0] < self.tail_position[0] - 1:
                self.tail_position[0] -= 1
                if self.head_position[1] > self.tail_position[1]:
                    self.tail_position[1] += 1
            elif self.head_position[1] > self.tail_position[1] + 1:
                self.tail_position[1] += 1
                if self.head_position[0] < self.tail_position[0]:
                    self.tail_position[0] -= 1
        if direction == 'DDR':
            if self.head_position[0] > self.tail_position[0] + 1:
                self.tail_position[0] += 1
                if self.head_position[1] < self.tail_position[1]:
                    self.tail_position[1] -= 1
            elif self.head_position[1] < self.tail_position[1] - 1:
                self.tail_position[1] -= 1
                if self.head_position[0] > self.tail_position[0]:
                    self.tail_position[0] += 1
        if direction == 'DDL':
            if self.head_position[0] < self.tail_position[0] - 1:
                self.tail_position[0] -= 1
                if self.head_position[1] < self.tail_position[1]:
                    self.tail_position[1] -= 1
            elif self.head_position[1] < self.tail_position[1] - 1:
                self.tail_position[1] -= 1
                if self.head_position[0] < self.tail_position[0]:
                    self.tail_position[0] -= 1
        string_tail = ','.join([str(position) for position in self.tail_position])
        if string_tail not in self.visited:
            self.visited[string_tail] = 1


class BigRope:
    def __init__(self):
        self.ropes = [Rope(k) for k in range(9)]  # only 9 cause 10 knots total
        self.step = 0

    @staticmethod
    def determine_direction(old_position, new_position):
        if old_position[0] < new_position[0]:
            if old_position[1] < new_position[1]:
                return 'DUR'
            if old_position[1] > new_position[1]:
                return 'DDR'
            return 'R'
        if old_position[0] > new_position[0]:
            if old_position[1] < new_position[1]:
                return 'DUL'
            if old_position[1] > new_position[1]:
                return 'DDL'
            return 'L'
        if old_position[1] > new_position[1]:
            return 'D'
        if old_position[1] < new_position[1]:
            return 'U'
        return None

    def follow_instruction(self, instruction):
        parsed = instruction.split(' ')
        for k in range(int(parsed[1])):
            self.step += 1
            direction = parsed[0]
            for j in range(9):
                old_position = [self.ropes[j].tail_position[0], self.ropes[j].tail_position[1]]  # stupid pointers
                if j == 0:
                    self.ropes[j].move_head(direction)
                else:
                    # probaby only really need to do this once because of stupid pointers but whatever
                    self.ropes[j].head_position = self.ropes[j-1].tail_position
                self.ropes[j].move_tail(direction)
                direction = self.determine_direction(old_position, self.ropes[j].tail_position)


if __name__ == "__main__":
    # Part 1
    rope = Rope()
    for instruction in puzzle_input:
        rope.follow_instruction(instruction)
    print(len(rope.visited))

    # Part 2
    ropes = BigRope()
    for instruction in puzzle_input:
        print(instruction)
        ropes.follow_instruction(instruction)
        for rope in ropes.ropes:
            print("Name:", rope.name, "head:", rope.head_position, "tail:", rope.tail_position)

    print(len(ropes.ropes[8].visited))
