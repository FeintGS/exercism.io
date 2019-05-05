import re

def is_isogram(string):
    string = string.lower()
    string = re.sub(r'\W+', '', string)

    char_set = set(string)
    return True if len(string)==len(char_set) else False
