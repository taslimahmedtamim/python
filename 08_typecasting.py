a = int("1") # convert string to integer
b = float("2.5") # convert string to float
c = str(1234) # convert integer to string
d = float(10) # convert integer to float
e = int(5.9) # convert float to integer (truncates decimal part)
f = str(3.14) # convert float to string
g = int(True) # convert boolean to integer (True=1, False=0)
h = float(False) # convert boolean to float (True=1.0, False=0.0)
i = str(True) # convert boolean to string ("True" or "False")
j = bool(1) # convert integer to boolean (0=False, non-zero=True)
k = bool(0) # convert integer to boolean (0=False, non-zero=True)
l = bool("") # convert empty string to boolean (""=False, non-empty=True)


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
print(k, type(k))
print(l, type(l))

# Example of typecasting with user input
x = input("enter a number: ")
y = input("enter a number: ")
print(x+y) #print as a string 

p = int(input("enter a number: "))
q = int(input("enter a number: "))
print(f'sum is {p+q}') #print sum 
