import re

fin = open("input.txt", "r")

passports = [data.replace('\n', ' ').strip() for data in fin.read().split("\n\n")]


class Passport(object):
    def __init__(self, data: str):
        self.valid = False
        self.polar = False
        self.part2=False
        elements = data.lower().split(' ')
        self.features = {}
        for element in elements:
            key, value = element.split(':')
            self.features[key] = value
        if {'byr', "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(self.features.keys()):
            self.valid = True
        if 'cid' in self.features.keys():
            self.polar = True
            self.features.pop('cid')

        if self.valid:
            byr_valid = 1920 <= int(self.features.get('byr')) <= 2002
            ihr_valid = 2010 <= int(self.features.get('iyr')) <= 2020
            eyr_valid = 2020 <= int(self.features.get('eyr')) <= 2030
            hgt_valid = (
                                self.features.get('hgt').endswith('cm') and 150 <= int(
                            self.features.get('hgt')[:-2]) <= 193) \
                        or (self.features.get('hgt').endswith('in') and 59 <= int(self.features.get('hgt')[:-2]) <= 76)
            hcl_valid = bool(re.fullmatch(r'#[0-9a-f]{6}', self.features.get('hcl')))
            ecl_valid = self.features.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            pid_valid = bool(re.fullmatch(r'\d{9}', self.features.get('pid')))
            self.part2 = all([byr_valid, ihr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid])

print(f"Part 1: {sum([Passport(elem).valid for elem in passports])}")
print(f"Part 2: {sum([Passport(elem).part2 for elem in passports])}")
