import argparse
import itertools
import math
import re

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()


def parse_file(file):
    tiles = {}
    tile = None
    for line in file.read().splitlines():
        if tile is None:
            tile = re.match(r"Tile (\d+):", line).group(1)
            tiles[tile] = []

        elif not line:
            tile = None

        else:
            tiles[tile].append(list(line))

    return tiles


def print_tile(tile):
    for row in tile:
        print("".join(row))
    print("")


def rotations(tile):
    tile_len = len(tile)
    yield tile
    yield [[tile[x][y] for x in range(tile_len - 1, -1, -1)] for y in range(tile_len)]
    yield [[tile[x][y] for x in range(tile_len)] for y in range(tile_len - 1, -1, -1)]
    yield [row[::-1] for row in tile[::-1]]


def flipped(tile):
    yield tile
    yield tile[::-1]
    yield [row[::-1] for row in tile]


def match(tile1, tile2):
    if tile1[0] == tile2[-1]:
        return 0, -1

    if tile1[-1] == tile2[0]:
        return 0, 1

    if [row[0] for row in tile1] == [row[-1] for row in tile2]:
        return -1, 0

    if [row[-1] for row in tile1] == [row[0] for row in tile2]:
        return 1, 0


def place_tile(tile_name, layout, layered_tiles):
    for mod in mods[tile_name]:
        for placed_tile, tile_data in layered_tiles.items():
            if (m := match(tile_data["value"], mod)) is not None:
                tile_x, tile_y = tile_data["position"]
                new_tile_x, new_tile_y = tile_x + m[0], tile_y + m[1]
                layout[(new_tile_x, new_tile_y)] = tile_name
                layered_tiles[tile_name] = {
                    "position": (new_tile_x, new_tile_y),
                    "value": mod,
                }
                return True
    return False


def remove_border(tile):
    return [[row[y] for y in range(1, 9)] for row in tile[1:-2]]


def is_monster(map, monster, x, y):
    if len(map[y:]) < len(monster):
        return False
    for row, monster_row in zip(map[y:], monster):
        if len(row[x:]) < len(monster_row):
            return False
        for col, monster_col in zip(row[x:], monster_row):
            if monster_col != " " and (monster_col != col):
                return False
    return True


def find_monster(map, monster):
    for x in range(len(map[0])):
        for y in range(len(map)):
            if is_monster(map, monster, x, y):
                return True
    return False


def remove_monster(map, monster, x, y):
    for x_o in range(len(monster[0])):
        for y_o in range(len(monster)):
            if monster[x][y] == "#":
                map[x+x_o][y+y_o] = "."
    return map

def count_monsters(map, monster):
    monsters = 0
    for x in range(len(map[0])):
        for y in range(len(map)):
            if is_monster(map, monster, x, y):
                monsters += 1
                # map = remove_monster(map, monster, x, y)
    return monsters


tiles = parse_file(args.input_file)
mods = {
    tile_name: [r for f in flipped(tile) for r in rotations(f)]
    for tile_name, tile in tiles.items()
}
tile = list(tiles)[0]
layout = {(0, 0): tile}
layered_tiles = {tile: {"position": (0, 0), "value": tiles[tile]}}
del tiles[tile]
to_place = list(tiles.keys())

while to_place:
    tile_name = to_place.pop(0)
    if not place_tile(tile_name, layout, layered_tiles):
        to_place.append(tile_name)

max_x = max(layout.keys(), key=lambda x: x[0])[0]
min_x = min(layout.keys(), key=lambda x: x[0])[0]

max_y = max(layout.keys(), key=lambda x: x[1])[1]
min_y = min(layout.keys(), key=lambda x: x[1])[1]

total_map = []
for y in range(min_y, max_y + 1):
    for row in range(1, 9):
        total_row = []
        for x in range(min_x, max_x + 1):
            tile_name = layout[x, y]
            total_row.extend(layered_tiles[tile_name]["value"][row][1:-1])
        total_map.append(total_row)

print(total_map)

print_tile(total_map)

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
print(monster)

found = False
for flip in flipped(total_map):
    for rot in rotations(flip):
        if find_monster(rot, monster):
            monster_count = count_monsters(rot, monster)
            sharp_count = sum(x.count("#") for x in rot)
            sharp_in_monster_count = sum(x.count("#") for x in monster)
            print(sharp_count - sharp_in_monster_count*monster_count)
