#O(nd) time and O(n) space
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	min_length = [float('inf') for _ in range(n+1)]
	min_length[0] = 0
	
	for denom in denoms:
		for value in range(len(min_length)):
			if denom <= value: #can we use the denom for the value
			   min_length[value] = min(min_length[value], 1+min_length[value-denom])
	return min_length[n] if min_length[n] != float('inf') else -1
		