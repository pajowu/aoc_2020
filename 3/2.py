import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

map = []
for line in args.input_file:
	row = []
	for char in line:
		if char == "#":
			row.append(True)
		else:
			row.append(False)
	map.append(row)

col_count = len(map[0]) - 1

def test_slope(slope_row, slope_col):
	position_row = 0
	position_col = 0

	trees_encountered = 0
	while position_row < len(map):
		if map[position_row][position_col]:
			trees_encountered += 1
		position_row += slope_row
		position_col = (position_col + slope_col) % col_count
	return trees_encountered

tree_product = 1
for sr, sl in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
	tree_product *= test_slope(sr, sl)

print(f"Tree Product: {tree_product}")