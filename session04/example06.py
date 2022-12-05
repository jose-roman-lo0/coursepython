# create a tuple with three elements
my_tuple = (1, 2, 3)

# access elements of the tuple by index
print(my_tuple[0])  # prints 1
# create a tuple with three elements
my_tuple = (1, 2, 3)

# access elements of the tuple by index
print(my_tuple[0])  # prints 1

# try to modify an element of the tuple
my_tuple[0] = 5  # this will raise an error because tuples are immutable
# tuples can be used in places where a list is expected
numbers = [1, 2, 3]
my_function(my_tuple)  # this is valid
my_function(numbers)  # this is also valid
