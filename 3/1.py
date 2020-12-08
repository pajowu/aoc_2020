import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def print_map(map, pos_row, pos_col):
	for i, row in enumerate(map):
		for j, col in enumerate(row):
			if i == pos_row and j == pos_col:
				print("O", end="")
			elif col:
				print("#", end="")	
			else:
				print(".", end="")
		print()
	print()
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

position_row = 0
position_col = 0

trees_encountered = 0
while position_row < len(map):
	# print_map(map, position_row, position_col)
	if map[position_row][position_col]:
		trees_encountered += 1
		print(f"tree at {position_row}, {position_col}")
	position_row += 1
	position_col = (position_col + 3) % col_count
	print(position_col, position_row)
print(f"{trees_encountered} trees were encountered")