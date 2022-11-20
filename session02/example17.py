# Example with index, swapping elements
my_list = []
# You can generate a list
for i in range(6):
    my_list.append(i**2)
print(my_list)

# We use negative index and list lenght
for i in range(1,((len(my_list)//2)+1)):
    my_list[i-1],my_list[-i] = my_list[-i],my_list[i-1]

print(my_list)

# You have a built in method to reverse a list!!!!!
my_list.reverse()
print(my_list)

