import argparse
import itertools
import math
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("iterations", type=int)
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


def active_neighbour_count(tiles, x, y):
	active = 0
	for t in ["w", "e", "nw", "ne", "sw", "se"]:
		x_o, y_o = get_tile(t)
		if tiles[(x+x_o, y+y_o)]:
			active += 1

	return active

def step(tiles):
	max_x = max(tiles.keys(), key=lambda x: x[0])[0]
	min_x = min(tiles.keys(), key=lambda x: x[0])[0]

	max_y = max(tiles.keys(), key=lambda x: x[1])[1]
	min_y = min(tiles.keys(), key=lambda x: x[1])[1]

	new_tiles = defaultdict(bool)

	for x in range(min_x-1, max_x+2):
		for y in range(min_y-1, max_y+2):
			active_neighbours = active_neighbour_count(tiles, x, y)
			if tiles[x, y]:
				if active_neighbours in [1, 2]:
					new_tiles[x, y] = True

			else:
				if active_neighbours == 2:
					new_tiles[x, y] = True

	return new_tiles

tiles = defaultdict(bool)
for line in args.input_file:
	tile_x, tile_y = get_tile(line.strip())
	val = tiles[tile_x, tile_y]
	tiles[tile_x, tile_y] = not val

for i in range(args.iterations):
	tiles = step(tiles)

black_count = 0
for v in tiles.values():
	if v:
		black_count += 1

print(black_count)
