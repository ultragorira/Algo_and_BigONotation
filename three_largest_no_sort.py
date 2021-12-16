#O (n) time O(1) space
def findThreeLargestNumbers(array):
	sorted_array = [None for _ in range(3)]
	
	for item in array:
		if sorted_array[2] is None or item > sorted_array[2]:
			sorted_array[0] = sorted_array[1]
			sorted_array[1] = sorted_array[2]
			sorted_array[2] = item
		elif sorted_array[1] is None or item > sorted_array[1]:
			sorted_array[0] = sorted_array[1]
			sorted_array[1] = item
		elif sorted_array[0] is None or item > sorted_array[0]:
			sorted_array[0] = item
			
	return sorted_array

print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, 541, -8, -7, 7]))