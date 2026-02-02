# this is how single line comment works
"""
    multiline comments
"""
'''
    also mutliline comments
'''

print("Hello, World")
print("Hello," + " " + "Tamim")
print("Welcome\nTamim")

print("Hi, " + input("What is your name?\n") + "!")

print("""
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.        
""")


# This will take a, b as a string 
a = input("Enter a number: ") # 1
b = input("Enter a number: ") # 2
print(a+b) # 12

# another way to print is f-string(formatted string literal)
print(f'sum is {a+b}')