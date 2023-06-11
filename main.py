import zipfile
import collections
import math

# Task 1: unzip words.zip and ls output
zipfile.ZipFile('words.zip').extractall('.')

# load a dictioary of english words from words.txt into wordlist
file = open("words/words.txt", "r");

wordlist = []

with open("words/words.txt", "r") as file:
    wordlist = file.readlines() # all data in words.txt are stored in read_data
file.close()

# Task 2:
# print(wordlist[:10])
# print(len(wordlist))

# converting a list to a set automatically removes the duplicates
# wordclean = sorted(list(set(str(file).strip().lower() for file in wordlist)))
# print(wordclean[:10])

# Task 3
"""
 From the generated List wordclean, separate words into classes of words
with the same length. This involves creating of a Dictionary called words_bylength from the
wordclean List where key is the word length and the value is the set of words having the same
word length
"""

# dictionary called words_bylength

