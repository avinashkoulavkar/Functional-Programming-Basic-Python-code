#Converts every word in the list to lower case and returns list

def to_lower(x):
	
	if not x.isalpha():
		return 0
	else:
		return x.lower()

def rem(x):
	if x==0:
		return False
	else:
		return x

ls=['ABC','XYZ','MNO','AVI12','XYZ1']

ls=map(to_lower,ls)

ls=filter(rem,ls)

print ls
