import argparse
from pprint import pprint
import itertools
import enum
import copy

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

class Position(enum.Enum):
	FLOOR = "floor"
	EMPTY_SEAT = "empty"
	OCCUPIED_SEAT = "occupied"

area = []
for line in args.input_file:
	row = []
	for char in line:
		if char == ".":
			row.append(Position.FLOOR)
		elif char == "L":
			row.append(Position.EMPTY_SEAT)
		elif char == "#":
			row.append(Position.OCCUPIED_SEAT)
	if row:
		area.append(row)

def is_occupied(row_idx, col_idx, area):
	if row_idx < 0 or row_idx >=  len(area):
		return 0
	row = area[row_idx]
	if col_idx < 0 or col_idx >= len(row):
		return 0

	return 1 if row[col_idx] == Position.OCCUPIED_SEAT else 0
def count_occupied_adjacent(row, col, area):
	occupied = 0
	for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
		occupied += is_occupied(row+row_offset, col + col_offset, area)

	return occupied

changed = True
i = 0
while changed:
	changed = False
	new_area = copy.deepcopy(area)
	for row_idx, row in enumerate(area):
		for col_idx, seat in enumerate(row):
			occ_adj = count_occupied_adjacent(row_idx, col_idx, area)
			if seat == Position.EMPTY_SEAT and occ_adj == 0:
				new_area[row_idx][col_idx] = Position.OCCUPIED_SEAT
				changed = True
			elif seat == Position.OCCUPIED_SEAT and occ_adj >= 4:
				new_area[row_idx][col_idx] = Position.EMPTY_SEAT
				changed = True
	i += 1
	area = new_area

occupied_seats = 0
for row in area:
	for seat in row:
		if seat == Position.OCCUPIED_SEAT:
			occupied_seats += 1

print(occupied_seats)

