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

    def part_1(self):
        answer = 0

        passports = []
        passport = {}

        for line in self.input_data:
            if line == "":
                passports.append(passport)
                passport = {}
            else:
                pairs = line.split(" ")
                for pair in pairs:
                    passport.update(**{k: v for (k, v) in [x.split(":") for x in pairs]})
                

        answer += sum([1 for x in passports if self.valid_passport_part_1(x)])

        return answer

    def part_2(self):
        answer = 0

        passports = []
        passport = {}

        for line in self.input_data:
            if line == "":
                passports.append(passport)
                passport = {}
            else:
                pairs = line.split(" ")
                for pair in pairs:
                    passport.update(**{k: v for (k, v) in [x.split(":") for x in pairs]})
                

        answer += sum([1 for x in passports if self.valid_passport_part_2(x)])

        return answer

    def parse_kv(self):
        pass

    def valid_passport_part_1(self, passport):
        if 'byr' in passport and \
            'iyr'  in passport and \
            'eyr'  in passport and \
            'hgt'  in passport and \
            'hcl'  in passport and \
            'ecl'  in passport and \
            'pid'  in passport:
            return True
        else:
            return False

    def valid_passport_part_2(self, passport):
        '''
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
        '''
        if 1920 <= int(passport.get('byr', 0)) <= 2002 and \
            2010 <= int(passport.get('iyr', 0)) <= 2020 and \
            2020 <= int(passport.get('eyr', 0)) <= 2030 and \
            self.valid_hgt(passport.get('hgt', '')) and \
            self.valid_hcl(passport.get('hcl', '')) and \
            self.valid_ecl(passport.get('ecl', '')) and \
            self.valid_pid(passport.get('pid', '')):
            return True
        else:
            return False

    def valid_hgt(self, hgt):
        match = hgt_pattern.match(hgt)
        if match:
            if match.group(2) == 'in' and (59 <= int(match.group(1)) <= 76):
                return True
            elif match.group(2) == 'cm' and (150 <= int(match.group(1)) <= 193):
                return True
        return False
    
    def valid_hcl(self, hcl):
        match = hcl_pattern.match(hcl)
        if match:
            return True
        else:
            return False

    def valid_ecl(self, ecl):
        match = ecl_pattern.match(ecl)
        if match:
            return True
        else:
            return False

    def valid_pid(self, pid):
        match = pid_pattern.match(pid)
        if match:
            return True
        else:
            return False
        