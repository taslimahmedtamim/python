# Write a Python program to count how many numbers in a given list are positive, negative, and zero. 

n = [3, -1, 0, 5, -2, 0, 7]
positive_count = 0
negative_count = 0
zero_count = 0

for i in n:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers count: ", positive_count)
print("Negative numbers count: ", negative_count)
print("Zero numbers count: ", zero_count)