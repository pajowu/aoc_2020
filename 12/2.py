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
wayp_x = 10
wayp_y = 1


for line in args.input_file:
    ins = line[0]
    num = int(line[1:])
    if ins == "N":
        wayp_y += num

    elif ins == "S":
        wayp_y -= num

    elif ins == "E":
        wayp_x += num

    elif ins == "W":
        wayp_x -= num

    elif ins == "L":
        if num == 90:
            wayp_x, wayp_y = -wayp_y, wayp_x
        elif num == 180:
            wayp_x, wayp_y = -wayp_x, -wayp_y
        elif num == 270:
            wayp_x, wayp_y = wayp_y, -wayp_x

    elif ins == "R":
        if num == 270:
            wayp_x, wayp_y = -wayp_y, wayp_x
        elif num == 180:
            wayp_x, wayp_y = -wayp_x, -wayp_y
        elif num == 90:
            wayp_x, wayp_y = wayp_y, -wayp_x

    elif ins == "F":
        pos_x += wayp_x * num
        pos_y += wayp_y * num

    print(wayp_x, wayp_y, pos_x, pos_y)
man_dist = abs(pos_x) + abs(pos_y)
print(man_dist)