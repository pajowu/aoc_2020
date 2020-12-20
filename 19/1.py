"""
The problem today is to decide whether words are in a context-free grammer.

The solution has two steps: first we transform the given grammer into chomsky normal form. Then we use the CYK algorithm to check if a word is in the language. 

This implementation is neither pretty nor fast, but it works :)
"""
import argparse
import copy
import operator
import re
from collections import defaultdict
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
parser.add_argument("start_symbol")
args = parser.parse_args()

def parse_file(file):
	rules, words = {}, []
	for line in file:
		line = line.strip()
		if not line:
			break

		rule_name, rule = line.split(": ")
		if match := re.match(r"\"(\w)\"", rule):
			rules[rule_name] = [match.group(1)]
		else:
			subrules = []
			for subrule in rule.split("|"):
				subrules.append(tuple(subrule.split()))
			rules[rule_name] = subrules

	for line in file:
		words.append(line.strip())
	return rules, words

def to_cnf(rules, start_symbol):
	""" This implementation is based on the wikipedia article on chompsky normal form."""
	# START: Eliminate the start symbol from right-hand sides
	cnf_rules = copy.deepcopy(rules)
	cnf_rules["S_0"] = [(start_symbol,)]
	# TERM: Eliminate rules with nonsolitary terminals
	# This is not possible in the input grammar
	# BIN: Eliminate right-hand sides with more than 2 nonterminals
	for rule, subrules in rules.items():
		for i, subrule in enumerate(subrules):
			if isinstance(subrule, tuple) and len(subrule) > 2:
				for n, x_n in enumerate(subrule[1:-2], 1):
					cnf_rules[f"{i}_{n}"] = [(x_n, f"{i}_{n+1}")]

				cnf_rules[f"{i}_{len(subrule)-2}"] = [tuple(subrule[-2:])]
				cnf_rules[rule][i] = (subrule[0], f"{i}_1")
	# DEL: Eliminate ε-rules
	# This is not possible in the input grammar
	# UNIT: Eliminate unit rules
	unit_rules = []
	for rule_name, rule in cnf_rules.items():
		for subrule in rule:
			if isinstance(subrule, tuple) and len(subrule) == 1:
				unit_rules.append((rule_name, subrule[0]))

	for a, b in unit_rules:
		print(a, b, cnf_rules[b])
		assert isinstance(cnf_rules[b], list)
		cnf_rules[a].extend(cnf_rules[b])
		cnf_rules[a].remove((b,))
	return cnf_rules

def cyk(grammar, start_symbol, word):
	flipped_grammar = defaultdict(list)
	for rule_name, rule in grammar.items():
		for subrule in rule:
			flipped_grammar[subrule].append(rule_name)

	# The following part is based on wikipedia pseudo code for the cyk algorithm
	P = defaultdict(bool)
	n = len(word)
	for s in range(1, n+1):
		for v in flipped_grammar[word[s-1]]:
			P[1, s, v] = True

	for l in range(2, len(word)+1):
		for s in range(1, n-l+2):
			for p in range(1, l):
				for res in flipped_grammar:
					if not isinstance(res, tuple):
						continue
					b, c = res
					if P[p, s, b] and P[l-p, s+p, c]:
						for a in flipped_grammar[res]:
							P[l, s, a] = True
							if l == n and s == 1 and a == start_symbol:
								return True

	return False
rules, words = parse_file(args.input_file)
cnf_rules = to_cnf(rules, args.start_symbol)
valid_words = 0
for i, word in enumerate(words):
	if cyk(cnf_rules, "S_0", word):
		valid_words += 1
	print(i)
print(valid_words)
