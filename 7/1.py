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
			result.append(res)
	rules[start] = result

rules_reversed = {k: [] for k in rules.keys()}
for k, v in rules.items():
	for bag in v:
		rules_reversed[bag].append(k)
"""
Pseudocode:
Initialize a list: "next"
Initialize a list: "possible_bags"
next.extend(rules[("shiny", "golden")])
while next:
	bag = 
"""
next = []
possible_bags = []
next.extend(rules_reversed[("shiny", "gold")])
while next:
	bag = next.pop(0)
	for rule in rules_reversed[bag]:
		if rule not in next and rule not in possible_bags:
			next.append(rule)
		else:
			print(rule)
	possible_bags.append(bag)

print(possible_bags)
print(len(possible_bags))