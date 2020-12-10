import argparse
from pprint import pprint
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

adapters = [0]
for line in args.input_file:
	adapters.append(int(line))

largest_adapter = max(adapters)
phone_adapter = largest_adapter + 3
print(f"Largest adapter: {largest_adapter}")
print(f"Phone adapter: {phone_adapter}")

adapters.append(phone_adapter)

adapter_chain = sorted(adapters)
diffs = []
for i in range(len(adapter_chain)-1):
	diffs.append(adapter_chain[i+1] - adapter_chain[i])
print(diffs)
one_count = diffs.count(1)
three_count = diffs.count(3)
print(f"{one_count} ones, {three_count} threes, product: {one_count * three_count}")