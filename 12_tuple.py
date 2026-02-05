# tuple = () : ordered, unchangeable, allows duplicate members

colors = ("red", "green", "blue", "red")
print(colors)

for i in colors:
    print(i)

# tuple operations
print(colors) # print entire tuple
print(colors[0]) # access first element
print(colors[1:3]) # slicing from index 1 to 2
print(colors[1:]) # from index 1 to end
print(colors[:3]) # from start to index 2
print(colors[-1]) # last element
print(colors[-3:]) # last 3 elements
print(colors[::2]) # skipping one element
print(colors[::-1]) # reverse tuple


# tuple methods (tuples have only 2 methods because they are immutable)

print(colors.count("red"))    # returns the number of times a value appears
print(colors.index("green"))  # returns the index of the first occurrence of a value

# Why only 2 methods?
# Tuples are immutable (unchangeable), so methods like append(), insert(),
# remove(), pop(), sort(), reverse() are NOT available for tuples.

# Convert tuple to list, modify, then convert back
colors_list = list(colors)    # Convert tuple to list
colors_list.append("yellow")  # Now we can modify
colors = tuple(colors_list)   # Convert back to tuple
print(colors)  # ('red', 'green', 'blue', 'red', 'yellow')

# get help on tuple class: print(help(tuple))