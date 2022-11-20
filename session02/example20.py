# List slice
import random
from nltk.corpus import inaugural
my_list = inaugural.words('1789-Washington.txt')
my_list_02 = random_words = [random.choice(my_list) for _ in range(100)]
print (my_list_02)
print(len(my_list_02))
my_list_03 = my_list_02[20:40]
print(my_list_03)



