# https://adventofcode.com/2020/day/1

from day import Day


class Day1(Day):
    def __init__(self, file_name):
        super().__init__(1, file_name)
        self.input_data = [int(x) for x in self.input_data]

    def part_1(self):
        answer = None
        sum_goal = 2020

        for num in self.input_data:
            pair_num = self.find_pair(num, sum_goal)
            if pair_num in self.input_data:
                answer = num * pair_num
                break
        return answer

    def part_2(self):
        answer = None
        break_flag = False
        sum_goal = 2020

        for num in self.input_data:
            if break_flag:
                break
            middle_sum = self.find_pair(num, sum_goal)
            for second_num in self.input_data:
                third_num = self.find_pair(second_num, middle_sum)
                if third_num in self.input_data:
                    answer = num * second_num * third_num
                    break_flag = True
                    break
        return answer

    def find_pair(self, in_num, goal_num):
        pair_num = goal_num - in_num
        return pair_num
