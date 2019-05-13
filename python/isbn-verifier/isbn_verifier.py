def verify(isbn):
    # parse and preprocess the string for validity
    s = isbn.replace('-', '')
    if len(s) != 10:
        return False
    if not s[0:9].isnumeric():
        return False
    if not s[9].isnumeric() and not 'X' in s[9]:
        return False

    # split the string into a list of integers
    digits = [int(x) for x in s[0:9]]
    digits.append(10 if s[9]=='X' else int(s[9]))

    # some arithmetic to confirm validity
    total = 0
    for i in range(0, 10):
       total += digits[i] * (i+1)
    return (total % 11) == 0
