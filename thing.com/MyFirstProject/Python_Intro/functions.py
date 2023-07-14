import random

def random_number(max_int):
    print("Rolling the Dice!")
    randNum = random.randint(1, max_int)
    return randNum



a_number = random_number(12)
print(a_number)