def is_armstrong_number(number):
    digits = [int(x) for x in str(number)]
    power = len(digits)
    digits_powered = map(lambda x: x**power, digits)

    return sum(digits_powered) == number
