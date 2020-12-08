import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

input_data = args.input_file.read()

group_num = 0
for group in input_data.split("\n\n"):
	group_num += len(set(filter(lambda x: x in string.ascii_lowercase, set(group))))

print(f"Group sum: {group_num}")