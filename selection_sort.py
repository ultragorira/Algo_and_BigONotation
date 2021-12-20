#O(n^2) time O(1) Space

def selectionSort(array):
	
	current_idx = 0
	while current_idx < len(array)-1:
		smallest_idx = current_idx
		for i in range(current_idx +1, len(array)):
			if array[smallest_idx] > array[i]:
				smallest_idx = i
		array[current_idx], array[smallest_idx] = array[smallest_idx], array[current_idx]
		current_idx +=1
	
	return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))