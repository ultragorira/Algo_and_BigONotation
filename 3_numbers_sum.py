#O(n^2) Time O(n) Spoace

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets_found = []
	
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left<right:
            currentSum = array[i]+array[left]+array[right]
            if currentSum == targetSum:
                triplets_found.append([array[i], array[left], array[right]])
                left+=1
                right-=1
            elif currentSum < targetSum:
                left+=1
            else:
                right-=1
	
									   
    return triplets_found


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))