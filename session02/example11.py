import time
# Example for loop
for i in range(20):
    print(i)

# Using increment
for i in range(2,20,2):
    print(i)
# Making some actions inside the loop
x = 2
for i in range(11):
    print (x**i)

# Using more real actions
for i in range(5):
    print(i," waiting Ms Daysy")
    time.sleep(1)

# Break and continue example
for i in range(10):
    if (i == 3):
        continue
    if (i == 6):
        break
    print("Printing inside the loop, loop number: ",i)
print("printing outside the loop")

# Example for odd numbers with continue
for i in range(10):
    if(not (i % 2)):
        continue
    print(i," is an odd number")

# Example using else in loops
j = 8
i = 1
while (j<5):
    print("Inside of while")
else:
    print("Inside of else")
