# Write a Python program to find the key with the maximum value in a dictionary.

d = {
    'a': 5,
    'b': 10,    
    'c': 3,
    'd': 8,
    'e': 2
    }

max_key = max(d, key=d.get)
print("Key with maximum value is : ", max_key)