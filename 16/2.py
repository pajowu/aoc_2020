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
	own_ticket = [int(x) for x in next(file).split(",")]
	next(file)

	next(file)
	tickets = []
	for line in file:
		tickets.append([int(x) for x in line.split(",")])

	return rules, own_ticket, tickets

rules, own_ticket, tickets = parse_file(args.input_file)
field_names = [set(rules.keys()) for _ in tickets[0]]
for ticket in tickets:
	for i, field in enumerate(ticket):
		for ((rule1_1, rule1_2),(rule2_1, rule2_2)) in rules.values():
			if rule1_1 <= field <= rule1_2 or rule2_1 <= field <= rule2_2:
				break
		else:
			break
	else:		
		for i, field in enumerate(ticket):
			candidates = set()
			for name, ((rule1_1, rule1_2),(rule2_1, rule2_2)) in rules.items():
				if rule1_1 <= field <= rule1_2 or rule2_1 <= field <= rule2_2:
					candidates.add(name)
			if not candidates:
				break

			field_names[i] = field_names[i] & candidates
			print(candidates)

done = False
while not done:
	done = True
	for i, names in enumerate(field_names):
		if len(names) == 1:
			name, = names
			for i in range(i) + range(i+1,len(field_names)):
				field_names[i] = field_names[i] - {name, }
		else:
			done = False

solution = 1
for names, val in zip(field_names, own_ticket):
	for name in names:
		if name.startswith("departure"):
			solution *= val
			break

print(solution)
