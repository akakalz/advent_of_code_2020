# https://adventofcode.com/2020/day/4

from day import Day
import re


hgt_pattern = re.compile(r'^(\d+)(cm|in)$')
hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
ecl_pattern = re.compile(r'^(?:amb|blu|brn|gry|grn|hzl|oth)$')
pid_pattern = re.compile(r'^\d{9}$')


class Day4(Day):
    def __init__(self, file_name):
        super().__init__(4, file_name)
        self.required_fields = {
            'byr': Day4.valid_byr,
            'iyr': Day4.valid_iyr,
            'eyr': Day4.valid_eyr,
            'hgt': Day4.valid_hgt,
            'hcl': Day4.valid_hcl,
            'ecl': Day4.valid_ecl,
            'pid': Day4.valid_pid,
        }

    def part_1(self):
        return sum([1 for x in self.parse_passports() if self.valid_passport_part_1(x)])

    def part_2(self):
        return sum([1 for x in self.parse_passports() if self.valid_passport_part_2(x)])

    def parse_passports(self):
        passport = {}

        for line in self.input_data:
            if line == "":
                yield passport
                passport = {}
            else:
                pairs = line.split(" ")
                for pair in pairs:
                    passport.update(**{k: v for (k, v) in [x.split(":") for x in pairs]})

    def valid_passport_part_1(self, passport):
        missing = []
        for field in self.required_fields:
            if field not in passport:
                missing.append(field)
        return not missing

    def valid_passport_part_2(self, passport):
        return all([validate(passport.get(field))
                    for field, validate in self.required_fields.items()])

    @staticmethod
    def valid_byr(byr):
        return 1920 <= (int(byr) if byr is not None else 0) <= 2002

    @staticmethod
    def valid_iyr(iyr):
        return 2010 <= (int(iyr) if iyr is not None else 0) <= 2020

    @staticmethod
    def valid_eyr(eyr):
        return 2020 <= (int(eyr) if eyr is not None else 0) <= 2030

    @staticmethod
    def valid_hgt(hgt):
        match = hgt_pattern.match(hgt if hgt is not None else '')
        if match:
            if match.group(2) == 'in' and (59 <= int(match.group(1)) <= 76):
                return True
            elif match.group(2) == 'cm' and (150 <= int(match.group(1)) <= 193):
                return True
        return False

    @staticmethod
    def valid_hcl(hcl):
        match = hcl_pattern.match(hcl if hcl is not None else '')
        return bool(match)

    @staticmethod
    def valid_ecl(ecl):
        match = ecl_pattern.match(ecl if ecl is not None else '')
        return bool(match)

    @staticmethod
    def valid_pid(pid):
        match = pid_pattern.match(pid if pid is not None else '')
        return bool(match)
