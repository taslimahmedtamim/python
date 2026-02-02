#for loop
for i in range(1,5): # range(start, stop) function generates numbers from 1 to 4
    print(i," ", end="") # end="" keeps the cursor on the same line
print("\nLoop ended")    

for j in range(1,10,2): # range(start, stop, step) with step of 2
    print(j," ", end="")
print("\nLoop ended")

#while loop
i = 1
while(i<5): # loop continues as long as i is less than 5
    print("Hello")
    i += 1
print("Loop ended")