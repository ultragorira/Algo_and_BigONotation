#O(n) Time O(1) Space
def moveElementToEnd(array, toMove):

    left_pointer = 0
    right_pointer = len(array)-1

    while left_pointer < right_pointer:
        if array[left_pointer] == toMove:
            if array[right_pointer] != toMove:
                array[right_pointer], array[left_pointer] = array[left_pointer], array[right_pointer] 
            else:
                right_pointer -= 1
        elif array[left_pointer] != toMove:
            left_pointer += 1

    return array

#Cleaner Version
def moveElementToEnd(array, toMove):
	
	left = 0
	right = len(array)-1
	
	while left < right:
		while left < right and array[right]==toMove:
			right-=1
		if array[left] == toMove:
			array[left], array[right] = array[right], array[left]
		left+=1
		
	return array