import argparse
import itertools
import math
import re
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


cups = [int(x) for x in next(args.input_file)]
cup_count = len(cups)
cur_cup_idx = 0
for _  in range(args.iterations):
	cur_cup = cups[cur_cup_idx]
	selected_cups = get_cups(cups, cur_cup_idx+1, 3)
	destination = ((cur_cup - 2) % cup_count) + 1
	while destination in selected_cups:
		destination = ((destination - 2) % cup_count) + 1

	destination_idx = cups.index(destination)
	cups[destination_idx+1:destination_idx+1] = selected_cups
	cur_cup_idx = (cups.index(cur_cup) + 1 ) % len(cups)

one_idx = cups.index(1)
cups_after_one = cups[one_idx+1:] + cups[:one_idx]
print("".join(str(x) for x in cups_after_one))
