#length of a list using map and reduce


ls=range(1,10)

ls1=map(lambda x:1 , ls)

res=reduce(lambda x,y:x+y , ls1)

print 'Length is:',res
