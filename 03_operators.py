x=3
y=2

# arithemetic operators
print(x+y) # addition
print(x-y) # subtraction
print(x*y) # multiplication
print(x/y) # division
print(x//y) # floor division
print(x%y) # modulus
print(x**y) # exponentiation

# bitwise operators
print(x&y) # bitwise AND
print(x|y) # bitwise OR
print(x^y) # bitwise XOR
print(x>>1) # right shift
print(x<<1) # left shift
print(~x) # bitwise NOT (inverts all bits)

# comparison operators
print(x==y) # equal to
print(x!=y) # not equal to
print(x>y) # greater than
print(x<y) # less than
print(x>=y) # greater than or equal to
print(x<=y) # less than or equal to

# logical operators
print(x and y) # logical AND
print(x or y) # logical OR
print(not x) # logical NOT

a = 5
a += 3 # a = a + 3
a -= 2 # a = a - 2
a *= 4 # a = a * 4
a /= 2 # a = a / 2
a %= 3 # a = a % 3
a //= 2 # a = a // 2
a **= 2 # a = a ** 2


# bitwise assignment operators
b = 5
b &= 3 # b = b & 3
b |= 2 # b = b | 2
b ^= 1 # b = b ^ 1
b >>= 1 # b = b >> 1
b <<= 2 # b = b << 2

# identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 
print(list1 is list3) # True - same object in memory
print(list1 is list2) # False - different objects with same value
print(list1 is not list2) # True - not the same object

# membership operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # True - apple exists in list
print("mango" in fruits) # False - mango doesn't exist
print("mango" not in fruits) # True - mango is not in list
print("a" in "apple") # True - works with strings too
print("z" not in "apple") # True - works with strings too

# operator precedence - (), **, *, /, //, %, +, -, <, <=, >, >=, ==, !=, &, ^, |, and, or
# i++, i-- increment, decrement operators are not supported in Python