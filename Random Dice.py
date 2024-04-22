import random


class Dice:

    def roll(self):
        luck = random.randint(1, 6)
        return luck


dice1 = Dice()
dice2 = Dice()

print(f"{dice1.roll()}, {dice2.roll()}")