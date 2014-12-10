#product of all even numbers in a list

def find_odd(x):
	if x % 2 == 0:
		return True
	else:
		return False

ls=range(1,10)

ls=filter(find_odd,ls)

res=reduce(lambda x,y:x*y , ls)

print res
