#O(log(n)) time | O(1)space
def binarySearch(array, target):
     return searchValue(array, target, 0, len(array)-1)

def searchValue(array, target, left, right):

	while left <= right:
		mid_index = (left + right)//2
		mid_value = array[mid_index]
		if mid_value == target:
			return mid_index
		elif target < mid_value:
			right = mid_index -1
		else:
			left = mid_index + 1
	
	return -1

binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33)

