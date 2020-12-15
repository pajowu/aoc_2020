import argparse
import math
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def apply_mask(val, mask):
	val_str = format(val, '036b')
	val_res = ""
	for v,m in zip(val_str, mask):
		if m == "X":
			val_res += v
		else:
			val_res += m
	return int(val_res, 2)

mask = None
values = defaultdict(int)
for line in args.input_file:
	key, val = [x.strip() for x in line.split(" = ")]
	if key == "mask":
		mask = val
	else:
		idx = int(key.split("[")[1].split("]")[0])
		values[idx] = apply_mask(int(val), mask)

print(sum(values.values()))