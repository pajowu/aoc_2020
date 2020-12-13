import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

earliest = int(next(args.input_file))
bus_intervals = next(args.input_file).strip()

best_inverval = None
best_departure = None
for bus_interval in bus_intervals.split(","):
	if bus_interval == "x":
		continue

	bus_interval = int(bus_interval)
	earliest_departure = math.ceil(earliest / bus_interval) * bus_interval
	if best_departure is None or earliest_departure < best_departure:
		best_departure = earliest_departure
		best_inverval = bus_interval

waiting_time = best_departure - earliest
print(f"{best_inverval} * {waiting_time} = {best_inverval * waiting_time}")