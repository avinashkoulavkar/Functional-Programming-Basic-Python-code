#Converts every word in the list to lower case and returns list

def to_lower(x):
	
	return x.lower()


ls=['ABC','XYZ','MNO','AVINaSh']

ls=map(to_lower,ls)

print ls
