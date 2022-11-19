# List example
my_list = [1,20,30,40,50,2]

for i in my_list:
    print (i)

# Manipulating list
my_list[2] = 0
my_list[1] = my_list[3]
print(my_list)

# List operations
print("Lenght of list is: ",len(my_list))

# Remove an element
del my_list[0]
print(my_list)
