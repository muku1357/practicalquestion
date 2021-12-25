# Write a Python program to multiplies all the items in a list.

'''def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,8]))'''

A=[1,2,3,4,5,6]
mul=1
for digit in A:
    mul *= digit
    print(mul)
