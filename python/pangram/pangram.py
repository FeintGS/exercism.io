import re

def is_pangram(sentence):
    sanitized = re.sub('[^a-z]+', '', sentence.lower())
    alphabet_count = len(set(list(sanitized)))

    return alphabet_count == 26
