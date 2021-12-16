#Time O(n) => number of elements + number of special arrays | Space O(D) where D is depth of special arrays
def productSum(array, multiplier=1):

    total_sum = 0
    for el  in array:
        if type(el) is list:
            total_sum += productSum(el, multiplier +1) #Recursive call
        else:
            total_sum += el
            
    return total_sum*multiplier

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))


