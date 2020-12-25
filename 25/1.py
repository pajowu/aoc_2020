import argparse
import itertools
import math
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

card_public_key = int(next(args.input_file))
door_public_key = int(next(args.input_file))

def brute_force_loopsize(subject_number, output):
	loop_count = 0
	value = 1
	while True:
		value = (value * subject_number) % 20201227
		loop_count += 1
		if value == output:
			return loop_count

def calculate(subject_number, loop_count):
	value = 1
	for _ in range(loop_count):
		value = (value * subject_number) % 20201227
	return value

card_private_key = brute_force_loopsize(7, card_public_key)
door_private_key = brute_force_loopsize(7, door_public_key)

print(calculate(door_public_key, card_private_key))
