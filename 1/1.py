import itertools

with open("input_1") as f:
	input_data = [int(x) for x in f]

for num1, num2 in itertools.combinations(input_data, r=2):
	if num1 + num2 == 2020:
		print(f'Found match, {num1} + {num2} = 2020; {num1} * {num2} = {num1 * num2}')
		break