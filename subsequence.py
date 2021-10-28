#O(n) time and O(1) space
def isValidSubsequence(array, sequence):
    
	idx_seq = 0
	
	for item in array:
		if idx_seq == len(sequence):
			break
		if sequence[idx_seq] == item:
			idx_seq +=1
		
	return idx_seq == len(sequence)


#O(n) Time, O (n)? or O(1) space since saving values to array
def isValidSubsequence_2(array, sequence):
    
	combined_list = []
	idx_sub = 0
	for i in array:
		if i == sequence[idx_sub]:
			combined_list.append(i)
			if idx_sub < len(sequence)-1:
				idx_sub +=1
			else: 
				break
				
	return combined_list == sequence


isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])