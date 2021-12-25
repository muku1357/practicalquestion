# Write a Python program to print a specified list after removing the 4th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4)]
print(color)
