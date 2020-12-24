import argparse
import itertools
import math
import re
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

def parse_file(file):
	dishes = []
	for line in file:
		match = re.match(r'^(.*?) \(contains (.*?)\)', line)
		dishes.append({"ingredients":match.group(1).split(), "allergens": match.group(2).split(", ")})
	return dishes

dishes = parse_file(args.input_file)

all_ingredients = set(a for x in dishes for a in x['ingredients'])

dish_allergens = defaultdict(lambda: all_ingredients)

for dish in dishes:
	for allergen in dish['allergens']:
		dish_allergens[allergen] = dish_allergens[allergen] & set(dish['ingredients'])

done = False
while not done:
	done = True
	for allergen, ingredients in dish_allergens.items():
		if len(ingredients) == 1:
			ingredient, = ingredients
			for all in dish_allergens.keys():
				if allergen == all:
					continue
				dish_allergens[all] -= {ingredient, }
		else:
			done = False

for allergen, (ingredient, ) in dish_allergens.items():
	dish_allergens[allergen] = ingredient

allergic_ingredients = set(dish_allergens.values())
non_allergic_ingredients = all_ingredients - allergic_ingredients

count = 0
for dish in dishes:
	for ingredient in dish['ingredients']:
		if ingredient in non_allergic_ingredients:
			count += 1


print(count)
