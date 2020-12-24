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
    yield tile
    yield [[tile[x][y] for x in range(9, -1, -1)] for y in range(10)]
    yield [[tile[x][y] for x in range(10)] for y in range(9, -1, -1)]
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
                # layout[tile_name]["neighbours"][(m + 2) % 4] = placed_tile
                return True
    return False


tiles = parse_file(args.input_file)
mods = {
    tile_name: [r for f in flipped(tile) for r in rotations(f)]
    for tile_name, tile in tiles.items()
}
tile = list(tiles)[0]
# layout = defaultdict(lambda: {"neighbours":[None, None, None, None], "value":None})
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
print(sorted(layout.items(), key=lambda x: x[0]))
print(math.prod(int(layout[x,y]) for x,y in itertools.product([min_x, max_x], [min_y, max_y])))
