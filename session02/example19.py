# function vs method, sorted vs sort
import random

my_list = []
# You can generate a list
for i in range(10):
    my_list.append(random.randrange(100))
    
my_list_02 = sorted(my_list)
print(my_list)
print(my_list_02)
my_list.sort()
print(my_list)

