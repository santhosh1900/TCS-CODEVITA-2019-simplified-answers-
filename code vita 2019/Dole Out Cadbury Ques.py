S_length  	 =		int(input("Enter the minimun length"))
L_length 	 =		int(input("Enter the maximum length"))
S_width 	 =		int(input("Enter the minimum width"))
L_width  	 = 		int(input("Enter the maximun width"))



# this function will return no of students for each candy bar
def candycal(x , y):
	count =0
	while x > 0 and y > 0:
		if x == y:
			count = count+1
			x=0
			y=0
		# i am interchanging this because length must always be greater than width
		if y > x:
			x , y = y , x
			# x = x-y beacuse 
			# for exampe : in 5 x3 bar 3 x 3 is max sq ,
			# so if we break tha 3 x 3 sq that candy bar will reduce to 2 x 3 bar
			#  3x3 bar is given to a child so i increment the child count
			x = x - y
			count = count+1
		if x > y:
			x = x - y
			count = count + 1
	return count
		

result = 0

for i in range(S_length , L_length+1):
	for j in range(S_width , L_width+1):
		result = result + candycal(i,j)
print(result)


