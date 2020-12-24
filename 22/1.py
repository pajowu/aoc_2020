import argparse
import itertools
import math
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

next(args.input_file)
player_one = []
for line in args.input_file:
	if not line.strip():
		break
	player_one.append(int(line))

next(args.input_file)
player_two = []
for line in args.input_file:
	if not line.strip():
		break
	player_two.append(int(line))

print(player_one, player_two)
while player_one and player_two:
	card_one, card_two = player_one.pop(0), player_two.pop(0)
	if card_one > card_two:
		player_one.extend([card_one, card_two])
	elif card_one < card_two:
		player_two.extend([card_two, card_one])
	else:
		assert False
	print(player_one, player_two)

print(player_one, player_two)
if player_one:
	winner = player_one
else:
	winner = player_two


acc = 0
for m,v in enumerate(winner[::-1], 1):
	acc += m*v

print(acc)
