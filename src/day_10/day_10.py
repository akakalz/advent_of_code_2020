# https://adventofcode.com/2020/day/10

from day import Day


class Day10(Day):
    def __init__(self, file_name: str):
        super().__init__(10, file_name)
        self.input_data = [int(x) for x in self.input_data]

    def part_1(self):
        diffs = self.get_jolt_diffs()
        answer = diffs[1] * diffs[3]
        return answer

    def part_2(self):
        self.input_data.sort()
        self.input_data.insert(0, 0)
        self.input_data.append(self.input_data[-1] + 3)
        size = len(self.input_data)

        combos_up_to_index = [1] * size
        for i in range(1, size):
            combos_up_to_index[i] = combos_up_to_index[i - 1]
            if i > 1 and self.input_data[i] - self.input_data[i - 2] <= 3:
                combos_up_to_index[i] += combos_up_to_index[i - 2]
            if i > 2 and self.input_data[i] - self.input_data[i - 3] <= 3:
                combos_up_to_index[i] += combos_up_to_index[i - 3]
        return combos_up_to_index[-1]

    def get_jolt_diffs(self):
        prev_adapter = 0
        diffs = {1: 0, 2: 0, 3: 0}
        self.input_data.sort()
        for x in self.input_data:
            diffs[x - prev_adapter] += 1
            prev_adapter = x
        diffs[3] += 1  # device is a 3 jolt diff
        return diffs
