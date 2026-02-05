# string in python is a sequence of characters. It is immutable. 

name = "Taslim Ahmed Tamim"

# String indexing and slicing
print(len(name)) #size of string
print(name[0]) # character at index 0
print(name[0:6]) # slicing from index 0 to 5
print(name[0:]) # from index 0 to end
print(name[:6]) # from start to index 5
print(name[-1]) # last character
print(name[-5:]) # last 6 characters
print(name[::2]) # skipping one character
print(name[::-1]) # reverse string


# String methods
print(name.capitalize()) # capitalize first letter
print(name.upper()) # convert to uppercase
print(name.lower()) # convert to lowercase
print(name.replace("Ahmed", "Majumder")) # replace substring
print(name.find("a")) # find the first occurence and give the index
print(name.rfind("a")) # find the last occurence and give the index
print(name.count("a")) # count occurrences of substring
print(name.split(" ")) # split string by space
print(name.startswith("Taslim")) # check starting substring
print(name.endswith("Tamim")) # check ending substring
print(name.strip()) # remove leading/trailing whitespace
print(name.title()) # capitalize first letter of each word
print(name.swapcase()) # swap case of each character
print(name.center(30, "-")) # center string with padding
print(name.ljust(30, "*")) # left justify with padding
print(name.rjust(30, "*")) # right justify with padding

# Character type checks
print("hello".isalpha()) # check if all characters are alphabetic
print("12345".isdigit()) # check if all characters are digits
print("hello123".isalnum()) # check if all characters are alphanumeric
print("   ".isspace()) # check if all characters are whitespace

# Join method
words = ["Hello", "World", "Python"]
print(" ".join(words)) # join list elements with space
print("-".join(words)) # join list elements with hyphen

# F-string formatting
age = 22
print(f"My name is {name} and I am {age} years old") # f-string
print(f"Name in uppercase: {name.upper()}") # f-string with method
print(f"2 + 2 = {2 + 2}") # f-string with expression


# get help on string class:
# print(help(str)) 