#O(n^2) time since 2 for loops/ O(1) space
def twoNumberSum(array, targetSum):
    
	for i in range(len(array)-1):
		for k in range(i+1, len(array)):
			if array[i] + array[k] == targetSum:
				return [array[i], array[k]]
			
	return []


#O(n) time since one loop, O(n) space because storing values in hash table
def twoNumberSum_2(array, targetSum):
    
	full_list_numbers = {}
	
	for number in array:
		if targetSum - number in full_list_numbers:
			return [targetSum - number, number]
		else:
			full_list_numbers[number] = True
			
	return []


#O (nLog(n)) Time, O(1) Space
def twoNumberSum_3(array, targetSum):
	
	array.sort()
	left_pointer = 0
	right_pointer = len(array)-1
	
	while left_pointer < right_pointer:
		currSum = array[left_pointer] + array[right_pointer]
		if currSum == targetSum:
			return [array[left_pointer],array[right_pointer]]
		elif currSum < targetSum:
			left_pointer +=1
		elif currSum > targetSum:
			right_pointer -=1
		
	return []


twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
