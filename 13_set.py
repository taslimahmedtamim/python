# set = {} : unordered, unindexed, no duplicate members

animals = {"cat", "dog", "bird", "cat"}
print(animals) # duplicates removed

for i in animals:
    print(i)

# set methods
animals.add("fish") # add element
animals.remove("dog") # remove element, raises error if not found
animals.discard("lion") # remove element if exists, no error if not found
