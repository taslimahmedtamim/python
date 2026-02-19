# Write a Python program to find the sum of the numbers passed as parameters.

def sum(*n):
    total = 0
    for num in n:
        total += num
    return total    

result = sum(1, 2, 3, 4, 5, 7)
print("The sum is:", result)