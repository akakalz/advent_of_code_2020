# https://adventofcode.com/2020/day/7

from day import Day
import re
import logging


logger = logging.getLogger(__name__)


full_rule_pattern = re.compile(r'^(.*?) bags contain (.*?).$')
contains_pattern = re.compile(r'^(\d+) (.*?) bags?$')


class Day7(Day):
    def __init__(self, file_name):
        super().__init__(7, file_name)

    def part_1(self):
        rules = self.load_rules()
        return len(self.find_all_bags_that_contain_target(rules, 'shiny gold'))

    def part_2(self):
        rules = self.load_rules()
        return self.find_all_bags_under_target(rules, 'shiny gold')

    def load_rules(self):
        rules = {}
        for line in self.input_data:
            rule_match = full_rule_pattern.match(line)
            if rule_match:
                contains = {}
                container = rule_match.group(1)
                contains_part = rule_match.group(2)
                parts = contains_part.split(", ")
                for part in parts:
                    contains_match = contains_pattern.match(part)
                    if contains_match:
                        amount = int(contains_match.group(1))
                        color = contains_match.group(2)
                        contains[color] = amount
                rules[container] = contains
        return rules

    def find_all_bags_that_contain_target(self, rules, target_bag):
        searched_bags = {}
        for bag, contains in rules.items():
            if contains:
                if target_bag in contains:
                    searched_bags[bag] = True
                else:
                    for search_bag in contains:
                        found = Day7._find_target_in_bags_helper(
                            rules,
                            search_bag,
                            target_bag
                        )
                        searched_bags[bag] = searched_bags.get(bag) or found

        return [x for x in searched_bags if searched_bags.get(x)]

    @staticmethod
    def _find_target_in_bags_helper(
        rules,
        search_bag,
        target_bag
    ):
        if target_bag in rules.get(search_bag, []):
            return True
        elif not rules.get(search_bag, []):
            return False
        else:
            sub_search_found = []
            for sub_bag in rules.get(search_bag, []):
                found = Day7._find_target_in_bags_helper(
                    rules,
                    sub_bag,
                    target_bag
                )
                sub_search_found.append(found)
            return any(sub_search_found)

    def find_all_bags_under_target(self, rules, target_bag):
        counts = []
        contains = rules.get(target_bag, {})
        for color, count in contains.items():
            Day7._find_bags_under_target_helper(
                rules,
                color,
                1,
                count,
                counts
            )
        return sum(counts)

    @staticmethod
    def _find_bags_under_target_helper(
        rules,
        target_bag,
        count_of_parent,
        count,
        counts
    ):
        current_count = count * count_of_parent
        counts.append(current_count)
        contains = rules.get(target_bag, {})
        for color, count in contains.items():
            Day7._find_bags_under_target_helper(
                rules,
                color,
                current_count,
                count,
                counts
            )
