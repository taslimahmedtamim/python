a = 1 # integer type 
b = 2.4 # float type
c = "Tamim" # string type
d = False # boolean type
e = None # NoneType
f = [1,2,3,"a",0.5] # list type - mutable
g = (1,2,3,"b",1.3) # tuple type - immutable
h = {
        "name": "Taslim", 
        "age": 22
    } # dictionary type - key-value pairs
i = {1,2,3} # set type - unordered unique elements
j = frozenset([1,2,3]) # frozenset type - immutable set

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))