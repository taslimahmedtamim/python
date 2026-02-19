# 1. Write a Python program to find the sum of odd and even numbers from a set of numbers. 

set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

even_sum = 0
odd_sum = 0

for i in set:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
        
print("Sum of even numbers: ", even_sum)
print("Sum of odd numbers: ", odd_sum)