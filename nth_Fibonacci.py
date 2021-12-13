#Time 2^n | Space O(n) => Worse of the solutions
def getNthFib(n):
	
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-1)+getNthFib(n-2)

#With memoization (caching)
#Time O(n) | Space O(n) => because of recursion and memoization to store values      
def getNthFib_2(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]

#With Iteration
#Time O(n) | Space O(1) 
def getNthFib_3(n):
    fib_array = [0,1]
    cnt = 3
    while cnt <= n:
        new_fib = fib_array[0] + fib_array[1]
        fib_array[0] = fib_array[1]
        fib_array[1] = new_fib
        cnt += 1
    return fib_array[1] if n > 1 else fib_array[0]
