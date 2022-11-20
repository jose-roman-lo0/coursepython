# List slice
import random
from nltk.corpus import inaugural
my_list = inaugural.words('1789-Washington.txt')
my_list_02 = random_words = [random.choice(my_list) for _ in range(100)]
print(my_list_02)
word_search = input("Introduce a word to search:\n")
if (word_search in my_list_02):
    print("The word is in the list")