#  Write a Python program to get the largest number from a list.

numbers = [3, 5, 1, 9, 2]
largest = None
for num in numbers:
    if largest is None or num > largest:
        largest = num
print("The largest number is:", largest)
