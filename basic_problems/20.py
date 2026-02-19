# Write a Python program to merge two dictionaries. 

dict1 = {'p': 1, 'q': 2}
dict2 = {'r': 3,'s': 4}

merge = {**dict1, **dict2}
print("Merged dictionary:", merge)