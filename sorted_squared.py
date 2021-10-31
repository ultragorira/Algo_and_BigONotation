# O (nLogn) => because of .sort time O(n) Space 
def sortedSquaredArray(array):
	squared_array = []
	for item in array:
		squared_array.append(item*item)
	squared_array.sort()	
	return squared_array
		

# O (nLogn) => because of .sort time O(n) Space, removing append which slows down
def sortedSquaredArray_2(array):

    squared_array = [0 for _ in array]

    for index in range(len(array)):
        value = array[index]
        squared_array[index] = value*value

    squared_array.sort()
    print(squared_array)


# O(n) Time an O(n) Space
def sortedSquaredArray(array):

	squared_array = [0 for _ in array]
	left_pointer = 0
	right_pointer = len(array)-1
	
	for index in reversed(range(len(array))):
		smaller_value = array[left_pointer]
		bigger_value = array[right_pointer]
		
		if abs(smaller_value) > abs(bigger_value):
			squared_array[index] = smaller_value*smaller_value
			left_pointer +=1
		else:
			squared_array[index] = bigger_value*bigger_value
			right_pointer -=1
		
		
	return squared_array

sortedSquaredArray_2([1, 2, 3, 5, 6, 8, 9])