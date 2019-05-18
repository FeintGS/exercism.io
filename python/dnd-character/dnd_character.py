from random import random

class Character:

    def __init__(self):
        self.strength     = self.__randomize__()
        self.dexterity    = self.__randomize__()
        self.constitution = self.__randomize__()
        self.intelligence = self.__randomize__()
        self.wisdom       = self.__randomize__()
        self.charisma     = self.__randomize__()

        self.hitpoints    = 10 + modifier(self.constitution)

    def __randomize__(self):
        dice_rolls = []
        dice_rolls.append(int(random()*6)+1)
        dice_rolls.append(int(random()*6)+1)
        dice_rolls.append(int(random()*6)+1)
        dice_rolls.append(int(random()*6)+1)

        highest_3 = sorted(dice_rolls)[1:4]
        return sum(highest_3)

    def ability(self):
        return self.strength

def modifier(constitution):
    return (constitution-10) // 2
