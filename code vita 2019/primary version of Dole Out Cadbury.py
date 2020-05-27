
# this the logic to find th how many childes get chocolate for one candy bar



def candycal(x , y):
	count =0
	while x > 0 and y > 0:
		if x == y:
			count = count+1
			x=0
			y=0
		if y > x:
			x , y = y , x
			x = x - y
			count = count+1
		if x > y:
			x = x - y
			count = count + 1
	return count
print(candycal(5,3))