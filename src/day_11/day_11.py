# https://adventofcode.com/2020/day/11

from day import Day


class Day11(Day):
    def __init__(self, file_name: str):
        super().__init__(11, file_name)

    def part_1(self):
        previous_state = self.input_data.copy()
        new_state = self.process_round_part_1(previous_state)
        while new_state != previous_state:
            previous_state = new_state.copy()
            new_state = self.process_round_part_1(new_state)
        return self.count_seats(new_state)

    def part_2(self):
        previous_state = self.input_data.copy()
        new_state = self.process_round_part_2(previous_state)
        while new_state != previous_state:
            previous_state = new_state.copy()
            new_state = self.process_round_part_2(new_state)
        return self.count_seats(new_state)

    def count_seats(self, state):
        answer = 0
        for line in state:
            for space in line:
                if space == "#":
                    answer += 1
        return answer

    def process_round_part_1(self, state):
        new_state = state.copy()
        width = len(new_state[0])
        height = len(new_state)

        for i, line in enumerate(state):
            for j, space in enumerate(line):
                dirs = [
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j + 1),
                    (i + 1, j + 1),
                    (i + 1, j),
                    (i + 1, j - 1),
                    (i, j - 1),
                    (i - 1, j - 1)
                ]

                if space == ".":
                    continue
                elif space == "#":
                    valid = []
                    for _dir in dirs:
                        if 0 <= _dir[0] < height and \
                                0 <= _dir[1] < width:
                            valid.append(state[_dir[0]][_dir[1]] == "#")
                    if sum(1 for x in valid if x is True) >= 4:
                        new_state[i] = new_state[i][:j] + "L" + \
                            new_state[i][j + 1:]
                elif space == "L":
                    valid = []
                    for _dir in dirs:
                        if 0 <= _dir[0] < height and \
                                0 <= _dir[1] < width:
                            valid.append(state[_dir[0]][_dir[1]] != "#")
                    if all(valid):
                        new_state[i] = new_state[i][:j] + "#" + \
                            new_state[i][j + 1:]
        return new_state

    def process_round_part_2(self, state):
        new_state = state.copy()
        width = len(new_state[0])
        height = len(new_state)

        for i, line in enumerate(state):
            for j, space in enumerate(line):
                dirs = [
                    (-1, 0),
                    (-1, 1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, -1),
                    (-1, -1)
                ]

                if space == ".":
                    continue
                elif space == "#":
                    valid = []
                    for _dir in dirs:
                        seat = Day11.find_first_seat_in_view(
                            state, j, i, _dir, width, height
                        )
                        valid.append(seat == "#")
                    if sum(1 for x in valid if x is True) >= 5:
                        new_state[i] = new_state[i][:j] + \
                            "L" + new_state[i][j + 1:]
                elif space == "L":
                    valid = []
                    for _dir in dirs:
                        seat = Day11.find_first_seat_in_view(
                            state, j, i, _dir, width, height
                        )
                        valid.append(seat != "#")
                    if all(valid):
                        new_state[i] = new_state[i][:j] + "#" + \
                            new_state[i][j + 1:]
        return new_state

    @staticmethod
    def find_first_seat_in_view(state, x, y, direction, width, height):
        seat = None
        magnitude = 1
        y_view = y + direction[0] * magnitude
        x_view = x + direction[1] * magnitude
        while 0 <= y_view < height and 0 <= x_view < width:
            if state[y_view][x_view] == ".":
                pass
            elif state[y_view][x_view] != ".":
                seat = state[y_view][x_view]
                break
            magnitude += 1
            y_view = y + direction[0] * magnitude
            x_view = x + direction[1] * magnitude
        return seat
