#O(n) time O(n) space 
def kadanesAlgorithm(array):
    # Write your code here.
	sums_array = [float('-inf') for _ in range(len(array))]
	sums_array[0] = array[0]
	for number in range(1, len(array)):
		summed_number = array[number] + sums_array[number-1]
		sums_array[number] = max(summed_number, array[number])
	
	return max(sums_array)

#O(n) time O(1) space
def kadanesAlgorithm(array):
	current_sum, max_sum =array[0], array[0]
	for value in array[1:]:
		current_sum = max(value, current_sum+value)
		max_sum = max(current_sum, max_sum)
		
	return max_sum