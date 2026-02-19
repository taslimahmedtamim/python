#  Write a Python program to find the difference between the largest and smallest elements in a list. 

n = [3, 5, 1, 9, 2]
largest = None
smallest = None
for num in n:
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
diff = largest - smallest

print("Difference between largest and smallest:", diff)
