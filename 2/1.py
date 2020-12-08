import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def is_valid(policy, password):
	min, max, char = policy
	if int(min) <= password.count(char) <= int(max):
		return True
	return False

valid_passwords = 0
for line in args.input_file:
	policy_str, password = line.split(": ")
	policy = re.match(r'(\d+)-(\d+) (\w)', policy_str).groups()
	if is_valid(policy, password):
		valid_passwords += 1

print(f"{valid_passwords} valid passwords found")