n = int(input("Enter your marks: "))

if(n>=80):
    print("A+")
elif(n>=70):
    print("A")
elif(n>=60):
    print("A-")
elif(n>=50):
    print("B")
elif(n>=40):
    print("C")
elif(n>=33):
    print("D")
else:
    print("F")  
    
# nested if-else

a = 33
b = 300
if b>a:
    print("B is greater than A")
    if a==33:
        print("A is 33")
    else:
        print("suiii")
elif a==b:
    print("A is equal to B")
else:
    print("A is less than B")