import argparse
import pprint
parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

rules = {}
for line in args.input_file:
	line = line.strip().strip(".")
	start_str, result_str = line.split(" contain ")
	start = tuple(start_str.split(" ")[:2])
	if result_str == "no other bags":
		result = []
	else:
		result = []
		bag_strs = result_str.split(",")
		for bag_str in bag_strs:
			bag_str = bag_str.strip()
			count = int(bag_str.split(" ")[0])
			res = tuple(bag_str.split(" ")[1:3])
			result.append((count, res))
	rules[start] = result

rules_reversed = {k: [] for k in rules.keys()}
for k, v in rules.items():
	for bag in v:
		rules_reversed[bag[1]].append(k)

def bag_count(bag_type):
	cnt = 1
	for count, child_type in rules[bag_type]:
		print(count, child_type, cnt)
		cnt += count * bag_count(child_type)

	return cnt

print(bag_count(("shiny", "gold")) - 1)