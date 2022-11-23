"""
Word Occurrences
Estimate: 20 minutes
Actual: 16 minutes
text is this is a collection of words of nice words this is a fun thing it is
"""

my_dictionary = {}

sentence = input("Text: ")
words = sentence.split()
for word in words:
    frequency = my_dictionary.get(word, 0)
    my_dictionary[word] = frequency + 1

words = list(my_dictionary.keys())
words.sort()
print(my_dictionary)

words = list(my_dictionary.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {my_dictionary[word]}")