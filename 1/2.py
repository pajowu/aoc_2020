import itertools
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("n", help="How many numbers need to match up", type=int)
args = parser.parse_args()

with open(args.input_file) as f:
	input_data = [int(x) for x in f]

for nums in itertools.combinations(input_data, r=args.n):
	if sum(nums) == 2020:
		print(f'Found match: {math.prod(nums)}')
		break