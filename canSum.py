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

