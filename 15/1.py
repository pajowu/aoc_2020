import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("iterations", type=int)
args = parser.parse_args()

starting_nums = [int(x) for x in next(args.input_file).split(",")]

spoken_nums = {}
for i, num in enumerate(starting_nums[:-1]):
	spoken_nums[num] = i

last_num = starting_nums[-1]
turn = len(spoken_nums)
while turn < args.iterations:
	if last_num not in spoken_nums:
		next_num = 0
	else:
		next_num = turn - spoken_nums[last_num]

	spoken_nums[last_num] = turn
	print(last_num)
	last_num = next_num
	turn += 1
	# break
print(last_num)
