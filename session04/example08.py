# create a dictionary
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# create a sorted list of the dictionary's keys
sorted_keys = sorted(my_dict)

# iterate over the sorted list of keys
for key in sorted_keys:
    # print the key and its corresponding value
    print(key, my_dict[key])

# create a dictionary
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# create a sorted list of the dictionary's key-value pairs
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

# iterate over the sorted list of key-value pairs
for key, value in sorted_items:
    # print the key and its corresponding value
    print(key, value)

# create a dictionary
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# sort the dictionary in-place by its keys
my_dict.sort()

# iterate over the sorted dictionary
for key, value in my_dict.items():
    # print the key and its corresponding value
    print(key, value)

