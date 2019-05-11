import re

class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def luhn_double(self, num):
        result = num * 2
        if result > 9:
            result = result - 9
        return result

    def is_valid(self):
        card_num = self.card_num.replace(' ', '')

        if len(card_num) <= 1:
            return False
        if not card_num.isnumeric():
            return False

        # sum up all the digits, according to the Luhn algorithm
        digits = [int(x) for x in card_num]

        first_digits  = digits[-1::-2]
        second_digits = list(map(self.luhn_double, digits[-2::-2]))

        total = sum(first_digits) + sum(second_digits)
        if total % 10 == 0:
            return True
        else:
            return False

