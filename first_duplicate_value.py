#O(n) time O(n) space
def firstDuplicateValue(array):
    indeces = set()

    for i in array:
        if i in indeces:
            return i
        else:
            indeces.add(i)
            
    return -1

#O(n) time, O(1) space
def firstDuplicateValue(array):
	for item in array:
		abs_value = abs(item)
		if array[abs_value -1] < 0:
			return abs_value
		array[abs_value -1] *=-1
	
	return -1