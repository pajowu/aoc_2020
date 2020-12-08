import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

input_data = args.input_file.read()

group_num = 0
for group in input_data.split("\n\n"):
	for letter in string.ascii_lowercase:
		if all(letter in member for member in group.split()):
			group_num += 1

print(f"Group sum: {group_num}")