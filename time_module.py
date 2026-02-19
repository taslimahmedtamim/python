import time

print(time.ctime()) # current time in human-readable format

def count(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1) # pause for 1 second
    print("Done counting!")
    
count(1, 5)