# Python3 program to calculate
# discrete logarithm
import math

def discreteLogarithm(a, b, m):

	n = int(math.sqrt (m) + 1)

	# Calculate a ^ n
	an = 1
	for i in range(n):
		an = (an * a) % m

	value = [0] * m

	# Store all values of a^(n*i) of LHS
	cur = an
	for i in range(1, n + 1):
		if (value[ cur ] == 0):
			value[ cur ] = i
		cur = (cur * an) % m
	
	cur = b
	for i in range(n + 1):
		
		# Calculate (a ^ j) * b and check
		# for collision
		if (value[cur] > 0):
			ans = value[cur] * n - i
			if (ans < m):
				return ans
		cur = (cur * a) % m

	return -1

# Driver code
b = 20
a = 5
m = 97
print(discreteLogarithm(a, b, m))
