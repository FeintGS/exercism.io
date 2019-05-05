import re

def word_count(phrase):
    # lowercase and strip all non-alphanumeric/non-apostrophe characters
    phrase = phrase.lower()
    phrase = re.sub("[^a-zA-Z0-9' ]+", " ", phrase)

    dictionary = {}
    for word in phrase.split():
        # strip leading and trailing quotation marks if they exist
        word = word.strip('"')
        word = word.strip("'")

        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word]+1

    return dictionary
