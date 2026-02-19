# Write a Python program to find the smallest number from a set of numbers. 

set = {5, 2, 9, 1, 7, -1}
min = None 
print(min)
for i in set:
    if min is None or i < min:
        min = i
print("Smallest number: ", min)    