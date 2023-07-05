import random
counter = 0

while counter <= 10:
    rand1 = random.randint(1, 10)
    guess = int(input("Enter number:  "))
    if guess == rand1:
        print("congratulations,You won!!!!")
        break
    counter = counter + 1



