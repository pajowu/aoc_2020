import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def decode(boarding_pass):
	row_s = boarding_pass[:7]
	row_b = row_s.replace("F", "0").replace("B", "1")
	row = int(row_b, 2)

	col_s = boarding_pass[7:]
	col_b = col_s.replace("R", "1").replace("L", "0")
	col = int(col_b, 2)

	return row, col, (row*8+col)

highest_seat_id = 0
for line in args.input_file:
	_, _, sid = decode(line.strip())
	if sid > highest_seat_id:
		highest_seat_id = sid

print(f"Highest Seat Id: {highest_seat_id}")