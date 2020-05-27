# this code is used to find the most repeated value
  # why  i used here is,
 # length of the most repeated value will  be the remaing jars value

# for bottle neck solution

  
def most_repeated(array, n): 
  
    # Sort the array 
    array.sort() 
  
    # find the max frequency using 
    # linear traversal 
    max_count = 1; res = array[0]; curr_count = 1
      
    for i in range(1, n):  
        if (array[i] == array[i - 1]): 
            curr_count += 1
              
        else : 
            if (curr_count > max_count):  
                max_count = curr_count 
                res = array[i - 1] 
              
            curr_count = 1
      
    # If last element is most frequent 
    if (curr_count > max_count): 
      
        max_count = curr_count 
        res = array[n - 1] 
      
    return res 
 

 # this array_leength has no use in this code to dont get confuse
array_length = int(input("Enter the size of the array"))



# even if the input elements exceeds the array_length it wont affect the code 
arr = list(int(x) for x in input("Enter the number of jars :  ").split())

n = len(arr) 

repeated_value = most_repeated(arr, n)
print(f" {arr.count(repeated_value)} jars are remaining ")

# note : please check the question before reffering the code 