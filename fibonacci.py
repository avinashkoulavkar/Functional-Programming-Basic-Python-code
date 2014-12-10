def fib(x):
	if x==0:
		return [1,1]
	tup = fib(x-1)
	print tup[0]
	return [tup[1],tup[0]+tup[1]]

a=999
fib(a)
