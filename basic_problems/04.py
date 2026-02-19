# Write a Python program to find the second-highest number from a set of numbers. 

set = {5, 2, 9, 1, 7, -1}

max1 = None
max2 = None

for i in set:
    if max1 is None or i > max1:
        max2 = max1
        max1 = i
    elif max2 is None or (i > max2 and i != max1):
        max2 = i
        
print("Second-highest number: ", max2)