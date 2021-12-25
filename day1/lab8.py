# Write a Python program to convert a tuple to a string.
'''
tuple=("g","e","e","k","s")
str = convertTuple(tuple)
print(str)'''

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

