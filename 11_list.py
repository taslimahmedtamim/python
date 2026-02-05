# list = [] : ordered, changeable, allows duplicate members

fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)

for i in fruits:
    print(i)

# list operations
print(fruits) # print entire list
print(fruits[0]) # access first element
print(fruits[1:3]) # slicing from index 1 to 2
print(fruits[1:]) # from index 1 to end 
print(fruits[:3]) # from start to index 2
print(fruits[-1]) # last element
print(fruits[-3:]) # last 3 elements
print(fruits[::2]) # skipping one element
print(fruits[::-1]) # reverse list  

# list methods
fruits.append("orange") # add element to end
fruits.insert(1, "grape") # insert element at index 1
fruits.remove("apple") # remove first occurrence of element
fruits.pop() # remove and return last element
fruits.pop(1) # remove and return element at index 1
fruits.sort() # sort list in ascending order
fruits.sort(reverse=True) # sort list in descending order
fruits.reverse() # reverse the order of the list
fruits.extend(["kiwi", "mango"]) # extend list by appending elements from another list
fruits.count("banana") # count occurrences of element
fruits_index = fruits.index("cherry") # get index of first occurrence of element
fruits_copy = fruits.copy() # create a shallow copy of the list
fruits.clear() # remove all elements from the list
fruits = fruits_copy # restore from copy
print(fruits) # print modified list

# Check membership
print("apple" in fruits)      # True if element exists
print("grape" not in fruits)  # True if element does not exist

# Built-in functions commonly used with lists
num = [3, 4, 5, 2, 1]
print(len(num))      # length of list
print(max(num))   # maximum value
print(min(num))   # minimum value
print(sum(num))   # sum of all elements
print(sorted(num))   # returns new sorted list (original unchanged)
print(list(reversed(num)))  # returns reversed iterator, convert to list


# get help on list class: print(help(list))
