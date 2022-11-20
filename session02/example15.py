# List with methods
my_list = []
for i in range (1,10):
    # append is a method
    my_list.append(2**i)

print(my_list)

my_list = []
for i in range (1,10):
    # we use insert method
    my_list.insert(0,2**i)

# Please check the difference between booth methods
print(my_list)
