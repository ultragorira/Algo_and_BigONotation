def arrayOfProducts(array):

    j=0
    mult = 1 
    total = 0
    output = []
    while j < len(array):
        for i in range(1, len(array)):
            mult = mult * array[i]
            total+= mult
        output.append(mult)
        mult=1
        total = 0
        if j==0:
            j=1
        array[0], array[j] = array[j], array[0]
        j+=1
    
    for i in range(1, len(array)):
        mult = mult * array[i]
        total+= mult
    output.append(mult) 

    return output

#O (n^2) Time O(n Space)
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))]
	
	leftRunningP = 1
	for i in range(len(array)):
		products[i] = leftRunningP
		leftRunningP *=array[i]
		
	rightRunningP = 1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningP
		rightRunningP *=array[i]
		
		
	return products