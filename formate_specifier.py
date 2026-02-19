# formate specifier = {value:flags} formate a value based on what flags are inserted.
# It is a way to format output in a specific way . It is used to control the output of numbers, strings, etc. It is used in f-strings and the format() method.

a = 123.456789
b = 12345
c = -1050
print(f"{a:.2f}") # 2 decimal places
print(f"{b:010}") # 10 characters wide, 2 decimal places
print(f"{b:10}") # 10 characters wide, right aligned
print(f"{b:>10}") # 10 characters wide, right aligned
print(f"{b:<10}") # 10 characters wide, left aligned
print(f"{b:^10}") # 10 characters wide, center aligned
print(f"{b:,}") # comma as thousand separator
print(f"{b:.2e}") # scientific notation with 2 decimal places
print(f"{b:+}  ") # show sign for positive numbers
print(f"{b:-}  ") # show sign for negative numbers only
print(f"{b: }  ") # show space for positive numbers, nothing for negative numbers
print(f"{c:,.2f}") # show sign, comma as thousand separator, 2 decimal places
