# Write a Python program to find the average of all elements in a list.

l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum += i
avg = sum / len(l)
print("Average:", avg)