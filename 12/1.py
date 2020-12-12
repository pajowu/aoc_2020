import argparse
from pprint import pprint
import itertools
import enum
import copy

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

pos_x = 0
pos_y = 0
# 0 = E, 1 = S, 2 = W, 3 = N
direction = 0

for line in args.input_file:
    ins = line[0]
    num = int(line[1:])
    if ins == "N":
        pos_x += num

    elif ins == "S":
        pos_x -= num

    elif ins == "E":
        pos_y += num

    elif ins == "W":
        pos_y -= num

    elif ins == "L":
        direction = (direction - (num / 90)) % 4

    elif ins == "R":
        direction = (direction + (num / 90)) % 4

    elif ins == "F":
        if direction == 3:
            pos_x += num

        elif direction == 1:
            pos_x -= num

        elif direction == 0:
            pos_y += num

        elif direction == 2:
            pos_y -= num

man_dist = abs(pos_x) + abs(pos_y)
print(man_dist)