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