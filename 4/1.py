import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

input_data = args.input_file.read()


required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
}
valid_passports = 0
for passport_str in input_data.split("\n\n"):
    passport = {}
    for field in passport_str.split():
        k, v = field.split(":")
        passport[k] = v
    if passport.keys() >= required_fields:
    		valid_passports += 1

print(f"Valid passports: {valid_passports}")