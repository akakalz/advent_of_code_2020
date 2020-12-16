# https://adventofcode.com/2020/day/15

from day import Day


class Day15(Day):
    def __init__(self, file_name: str):
        super().__init__(15, file_name)

    def part_1(self):
        nums = [int(x) for x in self.input_data[0].split(',')]
        turn = len(nums)
        memory = {}
        spoken = -1
        for i, num in enumerate(nums):
            memory[num] = [i + 1]
            spoken = num
        while turn < 2020:
            turn += 1
            prev_turns = memory.get(spoken)
            if prev_turns is not None:
                memory[spoken].append(turn - 1)
                spoken = memory[spoken][-1] - memory[spoken][-2]
            else:
                memory[spoken] = [turn - 1]
                spoken = 0
        return spoken

    def part_2(self):
        nums = [int(x) for x in self.input_data[0].split(',')]
        turn = len(nums)
        memory = {}
        spoken = -1
        for i, num in enumerate(nums):
            memory[num] = [i + 1]
            spoken = num
        while turn < 30000000:
            turn += 1
            prev_turns = memory.get(spoken)
            if prev_turns is not None:
                memory[spoken].append(turn - 1)
                if len(memory[spoken]) > 2:
                    memory[spoken].pop(0)
                spoken = memory[spoken][-1] - memory[spoken][-2]
            else:
                memory[spoken] = [turn - 1]
                spoken = 0
        return spoken
