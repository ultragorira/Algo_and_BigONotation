#O(nlog(n)+mlog(m)) Time O(1) Spoce
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer_one = 0
    pointer_two = 0
    smallest_pair = []
    shortest_distance = float('inf')
    current_distance = float('inf')

    while pointer_one < len(arrayOne) and pointer_two < len(arrayTwo):
        array_one_value = arrayOne[pointer_one]
        array_two_value = arrayTwo[pointer_two]
        if array_one_value < array_two_value:
            current_distance = array_two_value - array_one_value
            pointer_one +=1
        elif array_two_value < array_one_value:
            current_distance = array_one_value - array_two_value
            pointer_two +=1
        else:
            return[array_one_value, array_two_value] #This means they are the same so zero
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            smallest_pair = [array_one_value, array_two_value]
            
    return smallest_pair
