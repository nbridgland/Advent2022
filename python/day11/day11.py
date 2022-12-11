from python.util import read_file

filename = 'input.txt'

puzzle_input = read_file(filename)


class Monkey:
    def __init__(self, items, operation, test_number, throw1, throw2):
        self.items = [int(item) for item in items.split(': ')[1].split(', ')]
        self.operation = operation.split(': ')[1]
        self.test_number = int(test_number.split('by ')[1])
        self.throw1 = int(throw1[-1])
        self.throw2 = int(throw2[-1])
        self.inspected_items = 0

    def _adjust_worry(self):
        d = {'old': self.items[0]}
        exec(self.operation, d)
        self.items[0] = d['new']//3
        self.inspected_items += 1

    def throw_item(self):
        self._adjust_worry()
        item = self.items[0]
        self.items = self.items[1:]
        if item % self.test_number == 0:
            return item, self.throw1
        return item, self.throw2


class Monkey2:
    def __init__(self, number, items, operation, test, throw1, throw2, tests):
        self.number = int(number[-2:-1])
        parsed_items = [int(item) for item in items.split(': ')[1].split(', ')]
        self.items = [[item % test for test in tests] for item in parsed_items]
        self.operation = operation.split(': ')[1]
        self.throw1 = int(throw1[-1])
        self.throw2 = int(throw2[-1])
        self.tests = tests
        self.inspected_items = 0

    def _find_adjusted_worry(self, value):
        d = {'old': value}
        exec(self.operation, d)
        return d['new']

    def _adjust_worry(self):
        self.items[0] = [self._find_adjusted_worry(worry) for worry in self.items[0]]
        self.items[0] = [self.items[0][k] % self.tests[k] for k in range(len(self.tests))]
        self.inspected_items += 1

    def throw_item(self):
        self._adjust_worry()
        item = self.items[0]
        self.items = self.items[1:]
        if item[self.number] == 0:
            return item, self.throw1
        return (item, self.throw2)


if __name__ == "__main__":
    # Part 1
    monkeys = [Monkey(*puzzle_input[k*6+1+k:(k+1)*6+k]) for k in range(8)]
    for step in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item, throw = monkey.throw_item()
                monkeys[throw].items.append(item)
    for monkey in monkeys:
        print(monkey.inspected_items)

    # Part 2
    #tests = [23, 19, 13, 17]
    tests = [5, 17, 7, 13, 19, 3, 11, 2]
    monkeys = [Monkey2(*(puzzle_input[k*6+k:(k+1)*6+k]+[tests])) for k in range(len(tests))]
    for step in range(10000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item, throw = monkey.throw_item()
                monkeys[throw].items.append(item)
    for monkey in monkeys:
        print(monkey.inspected_items)

