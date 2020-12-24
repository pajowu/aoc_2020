import argparse
import itertools
import math
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def offset(op):
	if op == "w":
		return 1, 0
	elif op == "e":
		return -1, 0
	elif op == "nw":
		return 1, 1
	elif op == "ne":
		return 0, 1
	elif op == "sw":
		return 0, -1
	elif op == "se":
		return -1, -1

def get_tile(steps):
	steps = list(steps)
	tile_x, tile_y = 0, 0
	while steps:
		op = steps.pop(0)
		if op in ["s", "n"]:
			op += steps.pop(0)

		o_x, o_y = offset(op)
		tile_x += o_x
		tile_y += o_y

	return tile_x, tile_y


tiles = defaultdict(bool)
for line in args.input_file:
	tile_x, tile_y = get_tile(line.strip())
	val = tiles[tile_x, tile_y]
	tiles[tile_x, tile_y] = not val

black_count = 0
for v in tiles.values():
	if v:
		black_count += 1

print(black_count)

print(get_tile("nwwswee"))
