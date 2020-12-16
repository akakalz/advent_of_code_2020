# https://adventofcode.com/2020/day/14

from day import Day
import re
import itertools


mask_pat = re.compile(r'^mask = (.{36})$')
mem_pat = re.compile(r'^mem\[(\d+)\] = (\d+)$')


class Day14(Day):
    def __init__(self, file_name: str):
        super().__init__(14, file_name)

    def part_1(self):
        mask = ''
        memory = {}
        for line in self.input_data:
            mask_match = mask_pat.match(line)
            mem_match = mem_pat.match(line)
            if mask_match:
                mask = mask_match.group(1)
            elif mem_match:
                address = int(mem_match.group(1))
                value = int(mem_match.group(2))
                value = Day14.apply_mask_part_1(mask, value)
                memory[address] = value
            else:
                continue
        return sum([i for i in memory.values()])

    def part_2(self):
        mask = ''
        memory = {}
        for line in self.input_data:
            mask_match = mask_pat.match(line)
            mem_match = mem_pat.match(line)
            if mask_match:
                mask = mask_match.group(1)
            elif mem_match:
                address = int(mem_match.group(1))
                value = int(mem_match.group(2))
                addresses = Day14.apply_mask_part_2(mask, address)
                for addr in addresses:
                    memory[addr] = value
            else:
                continue
        return sum([i for i in memory.values()])

    @staticmethod
    def apply_mask_part_1(mask, value):
        powers = [2 ** i for i, _ in enumerate(mask[::-1]) if _ == 'X']
        new_value = int(mask.replace('X', '0'), 2)
        for power in powers:
            if value & power == power:
                new_value += power
        return new_value

    @staticmethod
    def apply_mask_part_2(mask, address):
        powers = [2 ** i for i, _ in enumerate(mask[::-1]) if _ == 'X']
        base_value = int(mask.replace('X', '0'), 2) | address
        addresses = []
        for power in powers:
            if base_value & power == power:
                base_value -= power
        for n in range(0, len(powers) + 1):
            for subset in itertools.combinations(powers, n):
                addresses.append(base_value + (sum(subset) if subset else 0))
        return addresses
