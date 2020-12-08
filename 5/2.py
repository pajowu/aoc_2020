import argparse
import math
import enum
parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def decode(boarding_pass):
	seat_b = boarding_pass.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
	return int(seat_b, 2)

map = 0
for line in args.input_file:
	sid = decode(line.strip())
	map |= (1 << sid)

"""
The following implements a simple FSM with 5 states:
It reads every bit in the map.

Start -0-> Start
Start -1-> Ones

Ones -0-> Zero
Ones -1-> Ones

Zero -0-> Err
Zero -1-> Halt

The Machine starts in start.
Ones it saw it's first 1, it reads 1 until a 0 is found and the machine switches to zero.
It then checks that the next is a 1 again and if so succeeds.
"""
class State(enum.Enum):
	START = "start"
	ONES = "ones"
	ZERO = "zero"
	ERR = "err"
	HALT = "halt"
found_sid = 0
sid = 0
state = State.START
while state not in [state.ERR, state.HALT]:
	if state == State.START:
		if map & 0b1 == 1:
			state = State.ONES
	elif state == State.ONES:
		if map & 0b1 == 0:
			state = State.ZERO
			found_sid = sid
	elif state == State.ZERO:
		if map & 0b1 == 0:
			print("ERR, double 0 found")
			state = state.ERR
		if map & 0b1 == 1:
			print(f"HALT, your seat is {found_sid}")
			state = state.HALT
	map >>= 1
	sid += 1
