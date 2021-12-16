#Best O(n) time O(1) space
#Average O(n^2) time O(1) space
#Worst: O(n^2) time O(1) space
	
def bubbleSort(array):
	
	sorted = False
	
	while not sorted:
		sorted = True
		for idx, item in enumerate(array):
			if idx < len(array)-1:
				if item > array[idx+1]:
					array[idx] = array[idx+1]
					array[idx+1] = item
					sorted = False
				
	return array



print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))

#here we keep track of counter which goes up by 1 for each time we went through one full Iteration 
#since the last item is for sure sorted
#it will not impact in the time complexity but in practice makes the algorithm better
def bubbleSort_optimized(array):
	
	sorted = False
	counter =0

	while not sorted:
		sorted = True
		for idx in range(len(array) - 1 - counter):
			if array[idx] > array[idx+1]:
				array[idx], array[idx+1] = array[idx+1], array[idx]
				sorted = False
	counter +=1		
	return array

print(bubbleSort_optimized([8, 5, 2, 9, 5, 6, 3]))