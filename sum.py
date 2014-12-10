#Write a function to calculate sum of all numbers in a list

ls=range(20)

res=reduce(lambda x,y:x+y , ls)

print res
