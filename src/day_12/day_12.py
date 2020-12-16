# https://adventofcode.com/2020/day/12

from day import Day
import re


dir_pattern = re.compile(r'^(.)(\d+)$')


class Day12(Day):
    def __init__(self, file_name: str):
        super().__init__(12, file_name)

    def part_1(self):
        x = y = 0
        facing = 'east'
        for line in self.input_data:
            match = dir_pattern.match(line)
            if match:
                move = match.group(1)
                magnitude = int(match.group(2))
                if move in ['L', 'R']:
                    facing = Day12.process_facing(facing, move, magnitude)
                elif move == 'F':
                    x, y = Day12.process_forward(x, y, facing, magnitude)
                else:
                    x, y = Day12.process_cardinal(x, y, move, magnitude)

        return abs(x) + abs(y)

    def part_2(self):
        x = y = 0
        wp_x = 10
        wp_y = 1

        for line in self.input_data:
            match = dir_pattern.match(line)
            if match:
                move = match.group(1)
                magnitude = int(match.group(2))
                if move in ['L', 'R']:
                    wp_x, wp_y = Day12.rotate_waypont(
                        wp_x, wp_y, move, magnitude
                    )
                elif move == 'F':
                    x, y = Day12.move_to_waypoint(x, y, wp_x, wp_y, magnitude)
                else:
                    wp_x, wp_y = Day12.process_cardinal(
                        wp_x, wp_y, move, magnitude
                    )

        return abs(x) + abs(y)

    @staticmethod
    def process_facing(facing, move, magnitude):
        while magnitude > 0:
            if facing == 'east':
                if move == 'L':
                    facing = 'north'
                else:
                    facing = 'south'
            elif facing == 'south':
                if move == 'L':
                    facing = 'east'
                else:
                    facing = 'west'
            elif facing == 'west':
                if move == 'L':
                    facing = 'south'
                else:
                    facing = 'north'
            elif facing == 'north':
                if move == 'L':
                    facing = 'west'
                else:
                    facing = 'east'
            magnitude -= 90
        return facing

    @staticmethod
    def rotate_waypont(wp_x, wp_y, _dir, magnitude):
        while magnitude > 0:
            magnitude -= 90
            diff_x = wp_x
            diff_y = wp_y
            if _dir == 'L':
                if diff_x == 0 and diff_y == 0:
                    pass
                elif diff_x > 0 and diff_y == 0:
                    wp_y += diff_x
                    wp_x -= diff_x
                elif diff_x > 0 and diff_y > 0:
                    # (2, 1) -> (-1, 2)
                    wp_x -= diff_x + diff_y
                    wp_y += diff_x - diff_y
                elif diff_x > 0 and diff_y < 0:
                    # (2, -1) -> (1, 2)
                    wp_x -= diff_x - abs(diff_y)
                    wp_y += diff_x + abs(diff_y)
                elif diff_x == 0 and diff_y > 0:
                    wp_x -= diff_y
                    wp_y -= diff_y
                elif diff_x == 0 and diff_y < 0:
                    wp_x -= diff_y
                    wp_y += abs(diff_y)
                elif diff_x < 0 and diff_y < 0:
                    # (-2, -1) -> (1, -2)
                    wp_x += abs(diff_x) + abs(diff_y)
                    wp_y -= abs(diff_x) - abs(diff_y)
                elif diff_x < 0 and diff_y == 0:
                    wp_x += abs(diff_x)
                    wp_y -= abs(diff_x)
                elif diff_x < 0 and diff_y > 0:
                    # (-2, 1) -> (-1, -2)
                    wp_x += abs(diff_x) - abs(diff_y)
                    wp_y -= abs(diff_x) + abs(diff_y)
                else:
                    pass
            else:
                if diff_x == 0 and diff_y == 0:
                    pass
                elif diff_x > 0 and diff_y == 0:
                    wp_y -= diff_x
                    wp_x -= diff_x
                elif diff_x > 0 and diff_y > 0:
                    # (2, 1) - > (1, -2)
                    wp_x -= abs(diff_x) - abs(diff_y)
                    wp_y -= abs(diff_x) + abs(diff_y)
                elif diff_x > 0 and diff_y < 0:
                    # (2, -1) - > (-1, -2)
                    wp_x -= abs(diff_x) + abs(diff_y)
                    wp_y -= abs(diff_x) - abs(diff_y)
                elif diff_x == 0 and diff_y > 0:
                    # (0, 2) -> (2, 0)
                    wp_x += diff_y
                    wp_y -= diff_y
                elif diff_x == 0 and diff_y < 0:
                    # (0, -2) -> (-2, 0)
                    wp_x -= abs(diff_y)
                    wp_y += abs(diff_y)
                elif diff_x < 0 and diff_y < 0:
                    # (-2, -1) -> (-1, 2)
                    wp_x += abs(diff_x) - abs(diff_y)
                    wp_y += abs(diff_x) + abs(diff_y)
                elif diff_x < 0 and diff_y == 0:
                    # (-2, 0) -> (0, 2)
                    wp_x += abs(diff_x)
                    wp_y += abs(diff_x)
                elif diff_x < 0 and diff_y > 0:
                    # (-2, 1) -> (1, 2)
                    wp_x += abs(diff_x) + abs(diff_y)
                    wp_y += abs(diff_x) - abs(diff_y)
                else:
                    pass
        return wp_x, wp_y

    @staticmethod
    def move_to_waypoint(x, y, wp_x, wp_y, magnitude):
        return (x + (wp_x * magnitude)), (y + (wp_y * magnitude))

    @staticmethod
    def process_forward(x, y, facing, magnitude):
        if facing == 'east':
            x += magnitude
        elif facing == 'south':
            y -= magnitude
        elif facing == 'west':
            x -= magnitude
        elif facing == 'north':
            y += magnitude
        return x, y

    @staticmethod
    def process_cardinal(x, y, move, magnitude):
        if move == 'E':
            x += magnitude
        elif move == 'S':
            y -= magnitude
        elif move == 'W':
            x -= magnitude
        elif move == 'N':
            y += magnitude
        return x, y
