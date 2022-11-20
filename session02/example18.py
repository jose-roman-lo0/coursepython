import random

my_list = []
# You can generate a list
for i in range(10):
    my_random = random.randrange(100)
    my_list.append(my_random)
print(my_list)
# We sort the list
my_list.sort()
print(my_list)
# And reverse it
my_list.sort(reverse=True)
print(my_list)


