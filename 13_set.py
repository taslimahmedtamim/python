# set = {} : unordered, unindexed, no duplicate members

# unordered: elements are not stored in a specific order, so we cannot access them by index
# unindexed: we cannot access elements by their position, but we can check for membership


animals = {"cat", "dog", "bird", "cat"}
print(animals) # duplicates removed
# print(animals[0]) # this will give an error because sets are unordered and unindexed

for i in animals:
    print(i)

# set methods
animals.add("fish") # add element
animals.remove("dog") # remove element, raises error if not found
animals.discard("lion") # remove element if exists, no error if not found
animals.clear() # remove all elements from the set
animals.pop() # remove and return an arbitrary element from the set