
def isMonotonic(array):
    if len(array) <=2:
        return True

    first_element = array[0]
    second_element = array[1]
    id = 1
    while second_element == first_element:
        id+=1
        if id <= len(array)-1:
            second_element = array[id]
        else:
            return True


    if second_element < first_element:
        for i in range(1,len(array)):
            if array[i] <= array[i-1]:
                pass
            else:
                return False
        return True
    elif second_element > first_element:
        for i in range(1,len(array)):
            if array[i] >= array[i-1]:
                pass
            else:
                return False
        return True

#Better version of isMonotonic
#O(n) Time, O(1) space
def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True
	
	for i in range(1, len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False
			
	return isNonDecreasing or isNonIncreasing