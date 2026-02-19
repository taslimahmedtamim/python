# Write a Python program to remove duplicate elements from a list. 

l = [1, 2, 3, 2, 4, 1, 5]
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)
print("List after removing duplicates: ", new_l)