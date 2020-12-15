import argparse
import math
from collections import defaultdict
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def apply_mask(val, mask):
	val_str = format(val, '036b')
	val_res = ""
	for v,m in zip(val_str, mask):
		if m == "X":
			val_res += m
		elif m == "0":
			val_res += v
		else:
			val_res += "1"
	return val_res

def addresses(mask):
	x_pos = [i for i,v in enumerate(mask) if v == "X" ]
	x_count = len(x_pos)
	mask_l = list(mask)
	pos = []
	for it in itertools.product(("0","1"), repeat=x_count):
		for i,v in zip(x_pos, it):
			mask_l[i] = v
		pos.append(int("".join(mask_l), 2))
	return pos

mask = None
values = defaultdict(int)
for line in args.input_file:
	key, val = [x.strip() for x in line.split(" = ")]
	if key == "mask":
		mask = val
	else:
		idx = int(key.split("[")[1].split("]")[0])
		idx_mask = apply_mask(int(idx), mask)
		idxs = addresses(idx_mask)
		for idx in idxs:
			values[idx] = int(val)

print(sum(values.values()))