# https://adventofcode.com/2020/day/8

from day import Day
import re


cmd_pattern = re.compile(r'^(...) ([+-])(\d+)$')


class Day8(Day):
    def __init__(self, file_name: str):
        super().__init__(8, file_name)

    def part_1(self):
        accumulator, _ = self.process_commands()
        return accumulator

    def part_2(self):
        infinite = True
        potential_fixes = [
            (i, Day8.parse_command_string(x))
            for i, x in enumerate(self.input_data) if "nop" in x or "jmp" in x
        ]
        for fix in potential_fixes:
            index = fix[0]
            original_cmd = fix[1][0]
            replacement_cmd = "nop" if original_cmd == "jmp" else "jmp"
            self.input_data[index] = \
                self.input_data[index].replace(original_cmd, replacement_cmd)
            accumulator, infinite = self.process_commands()
            self.input_data[index] = \
                self.input_data[index].replace(replacement_cmd, original_cmd)
            if not infinite:
                break
        else:
            raise AssertionError(
                "ran out of fixes and cmds were still infinite"
            )
        return accumulator

    @staticmethod
    def parse_command_string(string: str):
        match = cmd_pattern.match(string)
        if match:
            cmd = match.group(1)
            sign = match.group(2)
            amount = int(match.group(3))
            return cmd, sign, amount
        else:
            raise ValueError(f"cmd {string} was not recognized")

    def process_commands(self):
        accumulator = 0
        index = 0
        commands = {}

        infinite = False

        while index not in commands and index < len(self.input_data):
            cur_cmd = self.input_data[index]
            commands[index] = cur_cmd
            cmd, sign, amount = Day8.parse_command_string(cur_cmd)
            if cmd == "nop":
                index += 1
            elif cmd == "jmp":
                index += (amount if sign == "+" else (-1 * amount))
            elif cmd == "acc":
                accumulator += (amount if sign == "+" else (-1 * amount))
                index += 1
            if index in commands:
                infinite = True

        return accumulator, infinite
