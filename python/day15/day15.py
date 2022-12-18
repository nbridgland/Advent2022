from python.util import read_file
import numpy as np

filename = 'input.txt'
y_val = 2000000
max_val = 4000000
puzzle_input = read_file(filename)

parsed_input = [{'sensor': [int(entry.split('x=')[1].split(',')[0]),
                      int(entry.split('y=')[1].split(':')[0])],
           'beacon': [int(entry.split('x=')[2].split(',')[0]),
                      int(entry.split('y=')[2])]} for entry in puzzle_input]


def find_overlap(interval1, interval2):
    if interval1[1] >= interval2[0]:
        if interval1[0] <= interval2[0]:
            return True, [min(interval1[0], interval2[0]), max(interval2[1], interval1[1])]
    if interval2[1] >= interval1[0]:
        if interval2[0] <= interval1[0]:
            return True, [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
    if interval2[0] == interval1[1] + 1:
        return True, [interval1[0], max(interval1[1], interval2[1])]
    if interval1[0] == interval2[1] + 1:
        return True, [interval2[0], max(interval1[1], interval2[1])]
    return False, []


def merge_intervals(interval_list):
    k = 0
    while k < len(interval_list):
        j = k+1
        while j < len(interval_list):
            is_overlap, interval = find_overlap(interval_list[k], interval_list[j])
            if is_overlap:
                interval_list = interval_list[:k] + [interval] + interval_list[k+1:j] + interval_list[j+1:]
            else:
                j += 1
        k += 1
    return interval_list


def find_impossible_intervals(y_val, parsed):
    impossible_intervals = []
    current_places = []
    for sensor in parsed:
        max_distance = np.abs(sensor['sensor'][1] - sensor['beacon'][1]) + np.abs(
            sensor['sensor'][0] - sensor['beacon'][0])
        if sensor['beacon'][1] == y_val:
            if sensor['beacon'][0] not in current_places:
                current_places.append(sensor['beacon'][0])
        interval_width = max_distance - np.abs(y_val - sensor['sensor'][1])
        if interval_width > 0:
            impossible_intervals.append([sensor['sensor'][0] - interval_width, sensor['sensor'][0] + interval_width])
    old_len = 0
    while len(impossible_intervals) != old_len:
        old_len = len(impossible_intervals)
        impossible_intervals = merge_intervals(impossible_intervals)
    return impossible_intervals, current_places

if __name__ == "__main__":
    # Part 1
    intervals, current_places = find_impossible_intervals(y_val, parsed_input)
    all_intervals = sum([interval[1] - interval[0] + 1 for interval in intervals])
    for entry in current_places:
        for interval in intervals:
            if entry >= interval[0] and entry <= interval[1]:
                all_intervals -= 1
    print(all_intervals)

    # Part 2:
    for y_val in range(0, max_val):
        if y_val % 100000 == 0:
            print(y_val)
        intervals, current_places = find_impossible_intervals(y_val, parsed_input)
        for interval in intervals:
            if interval[0] <= 0 and interval[1] < max_val or interval[0] > 0:
                print(interval, y_val)
                print(intervals)
                break

    # So didn't feel like identifying this via code
    x_coord = 2706598
    y_val = 3253551
    print(x_coord*4000000 + y_val)