import argparse
import copy
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

def recursive_combat(player_one, player_two):
	player_one = copy.deepcopy(player_one)
	player_two = copy.deepcopy(player_two)
	previous_cardstacks = set()
	while player_one and player_two:
		if (tuple(player_one), tuple(player_two)) in previous_cardstacks:
			return 1, player_one
		previous_cardstacks.add((tuple(player_one), tuple(player_two)))
		card_one, card_two = player_one.pop(0), player_two.pop(0)
		if len(player_one) >= card_one and len(player_two) >= card_two:
			winner, _ = recursive_combat(player_one[:card_one], player_two[:card_two])
			if winner == 1:
				player_one.extend([card_one, card_two])
			else:
				player_two.extend([card_two, card_one])
		elif card_one > card_two:
			player_one.extend([card_one, card_two])
		elif card_one < card_two:
			player_two.extend([card_two, card_one])
		else:
			assert False
		# print(player_one, player_two)
	if not player_two:
		return 1, player_one
	else:
		return 2, player_two

winner, winning_cards = recursive_combat(player_one, player_two)


acc = 0
for m,v in enumerate(winning_cards[::-1], 1):
	acc += m*v

print(acc)
