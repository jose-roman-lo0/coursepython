# Using list in loops

my_list = []
# You can generate a list
for i in range(1,20,2):
    my_list.append(i**2)

# And iterate with for
for j in my_list:
    print(j)
