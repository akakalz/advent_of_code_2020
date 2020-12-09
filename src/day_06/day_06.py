# https://adventofcode.com/2020/day/6

from day import Day


class Day6(Day):
    def __init__(self, file_name: str):
        super().__init__(6, file_name)

    @property
    def new_group(self):
        return {"people": 0}

    def part_1(self):
        return sum(self.part_1_counts(x) for x in self.parse_groups())

    def part_2(self):
        return sum(self.part_2_counts(x) for x in self.parse_groups())

    def parse_groups(self):
        group = self.new_group
        for line in self.input_data:
            if line == "":
                yield group
                group = self.new_group
            else:
                group["people"] += 1
                for char in line:
                    if char in group:
                        group[char] += 1
                    else:
                        group[char] = 1

    @staticmethod
    def part_1_counts(group: dict):
        result = 0
        for key in group:
            if key != "people":
                result += 1
        return result

    @staticmethod
    def part_2_counts(group: dict):
        result = 0
        for key in group:
            if key == "people":
                continue
            if group[key] == group["people"]:
                result += 1
        return result
