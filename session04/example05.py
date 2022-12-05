# define a global variable
my_var = 5

# define a function that modifies the value of the global variable
def my_function():
  # use the global keyword to extend the scope of the global variable
  global my_var
# modify the value of the global variable
  my_var = 10

# print the value of the global variable before and after calling the function
print(my_var)  # prints 5
my_function()
print(my_var)  # prints 10
