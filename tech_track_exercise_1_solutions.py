# Write a function that takes a list of words and returns a report of all the words that are longer than
# 10 characters but don't contain a hyphen.
# If those words are longer than 15 characters, then they should be shortened to 15 characters and
# have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."


words = [
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism',
    "abiogenetically",
    "abnormalization",
    "aboriginalitiesing",
    "absorbabilitiesing",
    "absorptiometers",
    "absorptiometricing",
]


# Main function
def report_list_of_words(word: list[str]) -> list:
    filtered_words = filter_words(words)
    shortened_words = shorten_words(filtered_words)
    return shortened_words


# step 1: filter words that are longer than 10 characters but don't contain a hyphen.
def filter_words(words: list[str]) -> list:
    filtered_words = []
    for word in words:
        if word.isalpha() and len(word) > 10:
            filtered_words.append(word)

    return filtered_words


# Step 2: shorten words that are longer than 15 char, and add "...".
def shorten_words(words: list[str]) -> list:
    words_copy = words
    for i, word in enumerate(words_copy):
        if len(word) > 15:
            words_copy[i] = words_copy[i][:15] + "..."
    return words_copy


print(report_list_of_words(words))
