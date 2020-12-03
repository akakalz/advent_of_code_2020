from common import get_input, pad_left


class Day:
    def __init__(self, number, input_file):
        self.number = number
        self.input_data = get_input(input_file)

    def part_1(self):
        return None

    def part_2(self):
        return None

    def __repr__(self):
        return f"Day {pad_left(str(self.number), 2, char='0')}"
