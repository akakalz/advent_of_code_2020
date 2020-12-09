# https://adventofcode.com/2020/day/2

from day import Day
import re


class Day2(Day):
    def __init__(self, file_name: str):
        super().__init__(2, file_name)
        self.pattern = re.compile(r'^(\d+)-(\d+) ([a-z]): (.*)$')

    def part_1(self):
        answer = 0

        for line in self.input_data:
            match = self.pattern.match(line)
            if match:
                min_num = int(match.group(1))
                max_num = int(match.group(2))
                letter = match.group(3)
                password = match.group(4)
                if min_num <= password.count(letter) <= max_num:
                    answer += 1

        return answer

    def part_2(self):
        answer = 0

        for line in self.input_data:
            match = self.pattern.match(line)
            if match:
                min_num = int(match.group(1)) - 1
                max_num = int(match.group(2)) - 1
                letter = match.group(3)
                password = match.group(4)
                first = password[min_num] == letter
                second = password[max_num] == letter
                if first ^ second:
                    answer += 1

        return answer
