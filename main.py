import zipfile
import collections
import itertools
from itertools import permutations

# Task 1: unzip words.zip and ls output
zipfile.ZipFile('words.zip').extractall('.')

# load a dictioary of english words from words.txt into wordlist
file = open("words/words.txt", "r");

wordlist = []

wordlist = file.readlines() # all data in words.txt are stored in read_data

# Task 2:
# print(wordlist[:10])
# print(len(wordlist))

# converting a list to a set automatically removes the duplicates
wordclean = sorted(list(set(str(file).strip().lower() for file in wordlist)))

# Task 3
"""
 From the generated List wordclean, separate words into classes of words
with the same length. This involves creating of a Dictionary called words_bylength from the
wordclean List where key is the word length and the value is the set of words having the same
word length
"""

# dictionary called words_bylength
item = 0
words_bylength = {0 : []}

# index is the index (duh) and value is the string
# words_bylength[key] = value
def create_length_dictionary(strings):
    length_dict = {}

    for string in strings:
        length = len(string)
        if length in length_dict:
            length_dict[length].append(string)
        else:
            length_dict[length] = [string]

    return length_dict

result_dict = create_length_dictionary(wordclean)

# Print the resulting dictionary
# for length, strings in result_dict.items():
    #    print(f"Strings of length {length}: {strings}")

# print(result_dict)


# Task 4:
def generate_anagrams(word):
    # Generate all permutations of the letters in the word
    perms = permutations(word)
    
    # Join each permutation to form a string and store it in a list
    anagrams = [''.join(perm) for perm in perms]
    
    return anagrams

def create_anagram_dict(words):
    anagram_dict = {}
    
    for word in words:
        # Calculate the length of the word
        length = len(word)
        
        # If length key doesn't exist in the outer dictionary, create it with an empty inner dictionary
        if length not in anagram_dict:
            anagram_dict[length] = {}
        
        # If word key doesn't exist in the inner dictionary, generate anagrams and store them as a list
        if word not in anagram_dict[length]:
            anagram_list = generate_anagrams(word)
            anagram_dict[length][word] = anagram_list
    
    return anagram_dict

result_dict = create_anagram_dict(wordclean)

# prints the first five key value pairs
def print_dict(dic):
    first_five = itertools.islice(dic.items(), 2)
    for key, value in first_five:
        print(key, value)

# print out the anagram dict
print_dict(result_dict)


#for length, inner_dict in result_dict.items():
#    print(f"Length: {length}")
#    for word, anagrams in inner_dict.items():
#        print(f"{word}: {anagrams}")
#    print()


# Task 5:

file.close()
