import argparse
from pprint import pprint
import copy
parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

code = []
for line in args.input_file:
	if not line.strip():
		continue
	op, off = line.split()
	code.append([op, int(off)])

def check_terminates(code):
	accumulator = 0
	line = 0
	visited_lines = set()

	while True:
		visited_lines.add(line)

		op, off = code[line]

		if op == "acc":
			accumulator += off
			line += 1
		elif op == "jmp":
			line += off
		elif op == "nop":
			line += 1
		else:
			print("ERR", op, off)

		if line in visited_lines:
			# print("Loop detected, accumulator:", accumulator)
			return False, accumulator

		if line >= len(code):
			return True, accumulator

for i in range(len(code)):
	new_code = copy.deepcopy(code)
	if new_code[i][0] == "nop":
		new_code[i][0] = "jmp"
	elif new_code[i][0] == "jmp":
		new_code[i][0] = "nop"
	terms, acc = check_terminates(new_code)
	if terms:
		print(acc)
		break