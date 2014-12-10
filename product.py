 #product of all numbers in a list

ls=range(1,5)

res=reduce(lambda x,y:x*y , ls)

print res
