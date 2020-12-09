# https://adventofcode.com/2020/day/9

from day import Day


class Day9(Day):
    def __init__(self, file_name: str):
        super().__init__(9, file_name)
        self.input_data = [int(x) for x in self.input_data]
        self.part_1_preamble = 25

    def part_1(self):
        answer = None
        index = self.part_1_preamble
        while index < len(self.input_data):
            check_range = self.input_data[index - self.part_1_preamble:index]
            full_check = []
            for num in check_range:
                pair = Day9.find_pair(num, self.input_data[index])
                full_check.append(pair in check_range)
            if not any(full_check):
                answer = self.input_data[index]
                break
            index += 1
        return answer

    def part_2(self):
        part_1 = self.part_1()
        contiguous_range = self.find_contiguous_range(part_1)
        answer = min(contiguous_range) + max(contiguous_range)
        return answer

    @staticmethod
    def find_pair(number: int, sum_goal: int):
        return sum_goal - number

    def find_contiguous_range(self, number: int):
        contiguous_range = []
        start = 0
        while start < len(self.input_data):
            answer = 0
            end = start + 1
            while answer < number and end < len(self.input_data):
                answer = sum(self.input_data[start:end])
                if answer == number:
                    contiguous_range = self.input_data[start:end]
                    break
                end += 1
            if contiguous_range:
                break
            start += 1
        return contiguous_range
