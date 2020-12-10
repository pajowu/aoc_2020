import argparse
from pprint import pprint
import itertools
import functools

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

adapters = []
for line in args.input_file:
	if line:
		adapters.append(int(line))

largest_adapter = max(adapters)
phone_adapter = largest_adapter + 3
print(f"Largest adapter: {largest_adapter}")
print(f"Phone adapter: {phone_adapter}")
adapters.append(phone_adapter)
adapters.sort()

@functools.lru_cache
def adapter_chains(start, adapters):
	if len(adapters) == 0:
		return 1

	possible_adapters = []
	for adapter in adapters:
		if adapter < start:
			continue

		possible_adapters.append(adapter)

	chains = 0

	for i, adapter in enumerate(possible_adapters):
		if start + 3 < adapter:
			continue

		next_adapters = tuple(possible_adapters[i+1:])
		next_chains = adapter_chains(adapter, next_adapters)
		chains += next_chains

	return chains

chains = adapter_chains(0, tuple(adapters))
print(chains)
