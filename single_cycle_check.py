def hasSingleCycle(array):
	
	count_visited, current_idx = 0, 0
	while count_visited < len(array):
		if count_visited > 0 and current_idx == 0:
			return False
		count_visited += 1
		current_idx = getNext(current_idx, array)
	return current_idx == 0


def getNext(current_idx, array):
	jump = array[current_idx]
	nextIdx = (current_idx + jump) % len(array) #handling large integers
	return nextIdx if nextIdx >=0 else nextIdx + len(array) #handling negative integers
    