"""
Lets build a calculator :)

This calculator uses dijktras shunting yard algorithm to convert the input, which is in infix notation, to a RPN and then evaluates this.
"""
import argparse
import operator

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

OPERATORS = {"*":operator.mul, "+": operator.add}

def tokenize(expression):
	tokens = []
	i = 0
	expression += " "
	while i < len(expression)-1:
		if expression[i] == " ":
			i+=1

		elif expression[i].isdigit():
			num = 0
			while expression[i].isdigit():
				num = num*10 + int(expression[i])
				i+=1

			tokens.append(num)

		elif expression[i] in ["*", "+", "(", ")"]:
			tokens.append(expression[i])
			i += 1

	return tokens

def to_rpn(expression):
	out_queue, op_stack = [], []
	for token in tokenize(expression):
		if isinstance(token, int):
			out_queue.append(token)
		elif token in ["*", "+"]:
			while op_stack and op_stack[-1] != "(" and ((token == "*" and op_stack[-1] == "+") or (token == op_stack[-1])):
				out_queue.append(op_stack.pop())
			op_stack.append(token)

		elif token == "(":
			op_stack.append(token)
		elif token == ")":
			while op_stack[-1] != "(":
				out_queue.append(op_stack.pop())
			if op_stack and op_stack[-1] == "(":
				op_stack.pop()
		else:
			print("Unexpected token:",token)
	while op_stack:
		out_queue.append(op_stack.pop())
	return out_queue

def evaluate(expression):
	rpn_exp = to_rpn(expression)
	stack = []
	for token in rpn_exp:
		if isinstance(token, int):
			stack.append(token)

		elif token in ["*", "+"]:
			right = stack.pop()
			left = stack.pop()
			stack.append(OPERATORS[token](left, right))
	assert len(stack) == 1
	return stack[0]

line_sums = 0
for line in args.input_file:
	line_sum = evaluate(line.strip())
	line_sums += line_sum
print(line_sums)
