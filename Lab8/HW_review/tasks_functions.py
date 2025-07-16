
# ---------------------------------- Task 10 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""

## YOUR CODE HERE

def filter_words(words, minimum_lenght):
    # filtered_words = []
    # for x in words:
    #     if len(x) > minimum_lenght:
    #        filtered_words.append(x)
    # return filtered_words

    return [w for w in words if len(w) > minimum_lenght]

### TEST:
print(filter_words(["apple", "pear", "banana", "cherry"], 5))

### EXPECTED OUTPUT:
# ['banana', 'cherry']