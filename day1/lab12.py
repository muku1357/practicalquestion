# Write a Python program to update list element in a set.
#Sample: number = {1,2,3,4,5}
# Output: {1,2,3,4,5,7,8}


list1 = [1,2,3,4,5]
list2 = [7,8]

 # Lists converted to sets
set1 = set(list2)
set2 = set(list1)
 
# Update method
set1.update(set2)
 
# Print the updated set
print(set1)
 
