"""
Explanation:
This puzzle is solved using the chinese remainer theorem.
The puzzle input is a number of values (the bus intervals) m_0, ..., m_n and the puzzle is to find the smallest value for x that solves:

m_i * v_i = x + i

m_0 * v_0 = x
m_1 * v_1 = x + 1
...
m_n * v_n = x + n

This can be rewritten as to find the smallest x, that satisfies:

x mod m_i = -1 * i

e.g.

x mod m_0 = 0
x mod m_1 = -1
...
x mod m_n = -n

This can be solved using the chinese remainder theorem and extended euclidian algorithm

Note: when implementing this I did not get the correct result in the beginning, because the result of the division in line 51 was saved as a float, which lead to wrong calculations. Using an integer round lead to the correct results.
"""
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=argparse.FileType("r"))
args = parser.parse_args()

next(args.input_file)
bus_intervals = [
    (-i, int(x)) for i, x in enumerate(next(args.input_file).strip().split(",")) if x != "x" 
]

# This is a dirty implementation of the chinese remainder theorem
def extended_euclediean_algorithm(a, b):
	if b == 0:
		return (a, 1, 0)
	d_, s_, t_ = extended_euclediean_algorithm(b, a % b)
	d, s, t = d_, t_, s_ - ((a // b) * t_)
	return d, s, t

M = math.prod(x[1] for x in bus_intervals)
x = 0
for a_i, m_i in bus_intervals:
	M_i = M // m_i
	_, r, s = extended_euclediean_algorithm(m_i, M_i)
	e_i = s * M_i
	x += a_i * e_i
print(x % M)