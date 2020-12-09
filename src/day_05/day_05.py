# https://adventofcode.com/2020/day/5

from day import Day
import re


class Day5(Day):
    def __init__(self, file_name: str):
        super().__init__(5, file_name)
        self.pattern = re.compile(r'^([FB]{7})([RL]{3})$')

    def part_1(self):
        answer = -999999999
        for line in self.input_data:
            match = self.pattern.match(line)
            if match:
                seat_id = (self.parse_row(match.group(1)) * 8 +
                           self.parse_col(match.group(2)))
                answer = max(answer, seat_id)
        return answer

    def part_2(self):
        answer = None
        seats = []
        for line in self.input_data:
            match = self.pattern.match(line)
            if match:
                row = self.parse_row(match.group(1))
                col = self.parse_col(match.group(2))
                seat_id = (row * 8 + col)
                seats.append(seat_id)
        # we have all the seats (other than our own) so order them
        seats.sort()
        # now our seat will be between the two seats with a gap of 2
        for i, seat in enumerate(seats):
            if i == len(seats) - 1:
                break
            if seats[i + 1] - seat == 2:
                answer = seat + 1
        return answer

    # these row/cols are just other ways of representing binary
    def parse_row(self, string: str):
        return int(string.replace('B', '1').replace('F', '0'), 2)

    def parse_col(self, string: str):
        return int(string.replace('R', '1').replace('L', '0'), 2)
