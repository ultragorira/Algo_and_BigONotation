#O (nd) time and O(n) space
def numberOfWaysToMakeChange(n, denoms):
	total_ways = [0 for _ in range(n+1)]
	total_ways[0] = 1
	
	for denom in denoms:
		for amount in range(1, n+1):
			if denom <= amount:
				total_ways[amount]+= total_ways[amount - denom]
	return total_ways[n]