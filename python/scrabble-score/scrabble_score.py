def score(word):
    letter_value = {}
    letter_value = {**letter_value, **{key:1   for key  in 'aeioulnrst' }}
    letter_value = {**letter_value, **{key:2   for key  in 'dg'    }}
    letter_value = {**letter_value, **{key:3   for key  in 'bcmp'  }}
    letter_value = {**letter_value, **{key:4   for key  in 'fhvwy' }}
    letter_value = {**letter_value, **{key:5   for key  in 'k'     }}
    letter_value = {**letter_value, **{key:8   for key  in 'jx'    }}
    letter_value = {**letter_value, **{key:10  for key  in 'qz'    }}

    score = 0
    for c in word.lower():
        score += letter_value[c]
    return score
