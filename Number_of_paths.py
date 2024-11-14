def npaths(m,n, storage={}):
	# moving only right and down
	if (m,n) in storage:	
		return storage[(m,n)]
	if m==0 or n==0 :
		return 0
	if m== 1 or n==1 : 
		return 1
	storage[(m,n)] =  npaths(m-1,n) + npaths(m,n-1)
	return storage[(m,n)]


