# Write a Python program to find the largest number between two numbers using a function

def largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = largest(num1, num2)
print("The largest number is:", res)