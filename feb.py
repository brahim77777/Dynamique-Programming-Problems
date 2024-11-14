def feb(n ,  steps = 0, storage={}):
	steps +=1
	if n in storage:
		return storage[n]
	if n <= 2: 
		return 1;
	else :
		storage[n] =  feb(n-1 , steps)+feb(n-2, steps)
		

	print(f"steps {steps}")
	return storage[n]







def canSum(n , array):
	if n in array :
		return True
	if n == 1 :
		return False
	if n == 0 : 
		return True
	for i in range(len(array)):
		if array[i] < n :
			return canSum(n-array[i],array)
	return False






