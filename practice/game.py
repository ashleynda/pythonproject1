import random

counter = 0
rand1 = random.randint(1, 10)
while counter <= 10:
    guess = int(input("Enter number:  "))
    if guess > rand1:
        print("Too low,try again")
    if guess < rand1:
        print("Too high,try again")
    if guess == rand1:
        print("You have guessed correctly")
        break
    counter = counter + 1
