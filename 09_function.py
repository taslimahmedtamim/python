x = "awesome"
def myfunc1():
    print("Python is " + x)
myfunc1()
print("Python is ", x)

y = "awesome" # global variable
def myfunc2():
    y = "fantastic" # local variable
    print("python is " + y)
myfunc2()

def myfunc3(): 
    global z # use global keyword to modify global variable
    z = "fantastic"
myfunc3()
print("Python is " + z)

w = "awesome"
def myfunc4():
    global w 
    w = "Fantastic"
myfunc4()
print("python is " + w)


def yo():
    pass # empty function, does nothing

def greet(name="Tamim"): # default parameter value
    print("Hello, " + name + "!")
    
# Multiple arguments
def add(*args): # accepts variable number of arguments as a tuple
    return sum(args)
    
print(add(1, 2, 3, 4))

# Keyword arguments
def name(**kwargs): # accepts variable number of keyword arguments as a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

name(name="Tamim", age=22, city="Dhaka")