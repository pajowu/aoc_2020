import argparse
import itertools
import math
import re
import timeit
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("iterations", type=int)
args = parser.parse_args()

def get_cups(list, start, count):
	end = start + count
	list_len = len(list)
	cups = list[start:end]
	list[start:end] = []
	if end >= list_len:
		cups += list[:end%list_len]
		list[:end%list_len] = []
	return cups


# @profile
def main():
	cups_l = [int(x) for x in next(args.input_file)]
	cups_l.extend(range(len(cups_l)+1, 1_000_001))
	cup_count = len(cups_l)

	cups = {cup: next_cup for cup, next_cup in zip(cups_l, cups_l[1:] + cups_l[:1])}

	cur_cup = cups_l[0]
	for i in range(args.iterations):
		first_picked_up = cups[cur_cup]
		scnd_picked_up = cups[first_picked_up]
		last_picked_up = cups[scnd_picked_up]

		selected_cups = [first_picked_up, scnd_picked_up, last_picked_up]
		destination = ((cur_cup - 2) % cup_count) + 1
		while destination in selected_cups:
			destination = ((destination - 2) % cup_count) + 1

		# print(destination)

		cups[cur_cup] = cups[last_picked_up]
		cups[last_picked_up] = cups[destination]
		cups[destination] = first_picked_up

		cur_cup = cups[cur_cup]

		if i % 100_000 ==  0:
			print(i)

	next_to_one = cups[1]
	next_next_to_one = cups[next_to_one]
	print(next_to_one, next_next_to_one, next_to_one * next_next_to_one)
	# cup_count = len(cups)
	# cur_cup_idx = 0
	# for i  in range(args.iterations):
	# 	cur_cup = cups[cur_cup_idx]
	# 	selected_cups = get_cups(cups, cur_cup_idx+1, 3)
	# 	destination = ((cur_cup - 2) % cup_count) + 1
	# 	while destination in selected_cups:
	# 		destination = ((destination - 2) % cup_count) + 1
	# 	destination_idx = cups.index(destination)
	# 	print(destination, destination_idx)
	# 	cups[destination_idx+1:destination_idx+1] = selected_cups
	# 	cur_cup_idx = (cur_cup_idx + 1 ) % len(cups)
	# 	print(i)

	# print(len(cups))
	# one_idx = cups.index(1)
	# next_cups = get_cups(cups, one_idx+1, 2)
	# print(next_cups)

if __name__ == '__main__':
	main()
