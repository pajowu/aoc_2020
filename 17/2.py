import argparse
import copy
import itertools
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("iterations", type=int)
args = parser.parse_args()


def pprint_z(dimension,  z, min_x, max_x, min_y, max_y):
	print(f"z = {z}")
	# for x in range(min_x, max_x+1):
	# 	for y in range(min_y, max_y+1):
	# 		if dimension[(x, y, z)]:
	# 			print("#", end="")
	# 		else:
	# 			print(".", end="")
	# 	print()

def pprint_dimension(dimension):
	max_x = max(dimension.keys(), key=lambda x: x[0])[0]
	min_x = min(dimension.keys(), key=lambda x: x[0])[0]

	max_y = max(dimension.keys(), key=lambda x: x[1])[1]
	min_y = min(dimension.keys(), key=lambda x: x[1])[1]

	max_z = max(dimension.keys(), key=lambda x: x[2])[2]
	min_z = min(dimension.keys(), key=lambda x: x[2])[2]

	max_w = max(dimension.keys(), key=lambda x: x[3])[3]
	min_w = min(dimension.keys(), key=lambda x: x[3])[3]
	print(min_x, max_x, min_y, max_y)
	for z in range(min_z, max_z+1):
		pprint_z(dimension, z, min_x, max_x, min_y, max_y)

def active_neighbour_count(dimension, x, y, z, w):
	active = 0
	for x_o, y_o, z_o, w_o in itertools.product([-1,0,1], repeat=4):
		if x_o == y_o == z_o == w_o == 0:
			continue

		if dimension[(x+x_o, y+y_o, z+z_o, w+w_o)]:
			active += 1

	return active

def step(dimension):
	max_x = max(dimension.keys(), key=lambda x: x[0])[0]
	min_x = min(dimension.keys(), key=lambda x: x[0])[0]

	max_y = max(dimension.keys(), key=lambda x: x[1])[1]
	min_y = min(dimension.keys(), key=lambda x: x[1])[1]

	max_z = max(dimension.keys(), key=lambda x: x[2])[2]
	min_z = min(dimension.keys(), key=lambda x: x[2])[2]

	max_w = max(dimension.keys(), key=lambda x: x[3])[3]
	min_w = min(dimension.keys(), key=lambda x: x[3])[3]

	new_dimension = defaultdict(bool)

	for x in range(min_x-1, max_x+2):
		for y in range(min_y-1, max_y+2):
			for z in range(min_z-1, max_z+2):
				for w in range(min_w-1, max_w+2):
					active_neighbours = active_neighbour_count(dimension, x, y, z, w)
					if dimension[(x, y, z, w)]:
						if active_neighbours in [2,3]:
							new_dimension[(x, y, z, w)] = True

					else:
						if active_neighbours == 3:
							new_dimension[(x, y, z, w)] = True

	return new_dimension
dimension = defaultdict(bool)
for x, line in enumerate(args.input_file):
	for y, cell in enumerate(line.strip()):
		if cell == "#":
			dimension[(x, y, 0, 0)] = True
		else:
			dimension[(x, y, 0, 0)] = False

pprint_dimension(dimension)
for i in range(args.iterations):
	dimension = step(dimension)
	pprint_dimension(dimension)

active_cubes = list(dimension.values()).count(True)

print(f"{active_cubes} active cubes")
