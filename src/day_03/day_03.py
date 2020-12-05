# https://adventofcode.com/2020/day/3

from day import Day


class Day3(Day):
    def __init__(self, file_name):
        super().__init__(3, file_name)

    def part_1(self):
        slope = (1, 3)
        answer = self._traverse_slope(slope)

        return answer

    def part_2(self):
        answer = 1

        trees = []
        slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

        for slope in slopes:
            trees_this_run = self._traverse_slope(slope)
            trees.append(trees_this_run)

        for x in trees:
            answer *= x

        return answer

    def _traverse_slope(self, slope):
        trees_this_run = 0
        y_index = slope[0]
        x_index = slope[1]
        repeat_edge = len(self.input_data[0])

        while y_index < len(self.input_data):
            if x_index >= repeat_edge:
                x_index -= repeat_edge
            if self.input_data[y_index][x_index] == "#":
                trees_this_run += 1
            y_index += slope[0]
            x_index += slope[1]
        return trees_this_run
