import random


# random.seed(32)
# for roll in range(10):
#     print(random.randrange(1, 7), end=' ')

def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return(die1, die2)

def display_dice(dice):
    

