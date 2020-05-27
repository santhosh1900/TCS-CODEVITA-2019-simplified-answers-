# A Python program to print all  

# permutations using library function 

from itertools import permutations 

# functio nto finf the smallest number which is higher than B

def high(arr , B):
	for i in range(len(arr)):
		if int_sol[i] > B :
			return arr[i]
		
	else:
		return -1
  
# Get all permutations of [1, 2, 3] 

A = input("Enther the value of A :  ")

B = int(input("Enter the vaue of B : "))

solutionList = [x for x in A]



# it a tuple wchih comntaind all the permuation combination of number A

permu = permutations(solutionList) 

sol1=[]
  

# appending the value to sol1 array the obtained permutations 

for i in permu:
	sol1.append("".join(i))


# sorting the permutated value

sol1.sort()

int_sol = []

# changing the all the string to integer


for i in range(len(sol1)):
	
	int_sol.append(int(sol1[i]))


print(f"permutaton combination of number {A} IS")

print(int_sol)


print(high(int_sol , B))















	