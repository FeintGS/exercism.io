import re

def abbreviate(words):
    words = re.sub("[^A-Za-z']+", ' ', words)
    acronym = ''
    for word in words.split():
        acronym += word[0].upper()
    return acronym
