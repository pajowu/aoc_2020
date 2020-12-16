import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def parse_file(file):
	rules = {}
	for line in file:
		if not line.strip():
			break
		rule_name, rule = line.split(": ")
		rule1, rule2 = rule.split(" or ")
		rule1 = [int(x) for x in rule1.split("-")]
		rule2 = [int(x) for x in rule2.split("-")]
		rules[rule_name] = (rule1, rule2)

	next(file)
	own_ticket = next(file)
	next(file)

	next(file)
	tickets = []
	for line in file:
		tickets.append([int(x) for x in line.split(",")])

	return rules, own_ticket, tickets

rules, own_ticket, tickets = parse_file(args.input_file)
invalid = False
for ticket in tickets:
	for field in ticket:
		for ((rule1_1, rule1_2),(rule2_1, rule2_2)) in rules.values():
			if rule1_1 <= field <= rule1_2 or rule2_1 <= field <= rule2_2:
				break
		else:
			invalid += field
			break

print(invalid)
