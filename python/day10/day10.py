from python.util import read_file
import numpy as np

filename = 'input.txt'

puzzle_input = read_file(filename)


class Widget:
    def __init__(self):
        self.cycles = 0
        self.X = 1
        self.output = 0
        self.crt_drawing = [['.' for k in range(40)] for j in range(6)]

    def cycle(self):
        self.draw_pixel()
        self.cycles += 1
        if (self.cycles - 20) % 40 == 0:
            self.output += self.cycles * self.X
            print(self.cycles*self.X)

    def draw_pixel(self):
        row = self.cycles//40
        column = self.cycles % 40
        if np.abs((self.cycles % 40) -self.X) <= 1:
            self.crt_drawing[row][column] = '#'

    def noop(self):
        self.cycle()

    def add(self, value):
        self.cycle()
        self.cycle()
        self.X += value


if __name__ == "__main__":
    # Part 1
    widget = Widget()
    for instruction in puzzle_input:
        if instruction == 'noop':
            widget.noop()
        else:
            widget.add(int(instruction.split(' ')[1]))
    print(widget.output)


    # Part 2
    for line in widget.crt_drawing:
        print(line)