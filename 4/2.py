import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

input_data = args.input_file.read()

def validate_passport(passport):
	if int(passport['byr']) < 1920 or int(passport['byr']) > 2003:
		print("byr")
		return False

	if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
		print("iyr")
		return False

	if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
		print("eyr")
		return False

	if passport['hgt'].endswith("cm"):
		height = int(passport['hgt'][:-2])
		if height < 150 or height > 193:
			print("hgtcm")
			return False
	elif passport['hgt'].endswith("in"):
		height = int(passport['hgt'][:-2])
		if height < 59 or height > 76:
			print("hgtin")
			return False
	else:
		return False

	if re.match(r'#[0-9a-f]{6}', passport['hcl']) is None:
		return False

	if passport['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return False

	if not passport['pid'].isdigit() or len(passport['pid']) != 9:
		print("pid")
		return False

	return True

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
    	if validate_passport(passport):
    		valid_passports += 1

print(f"Valid passports: {valid_passports}")