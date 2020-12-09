import argparse
from pprint import pprint
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("preamble_length", type=int)
args = parser.parse_args()

read_numbers = []
for line_number, line in enumerate(args.input_file):
	line_int = int(line)
	if line_number < args.preamble_length:
		pass

	else:
		candidates = read_numbers[-args.preamble_length:]
		for comb in itertools.combinations(candidates, r=2):
			if sum(comb) == line_int:
				break
		else:
			print(f"Found: {line_int}")
			break

	read_numbers.append(line_int)