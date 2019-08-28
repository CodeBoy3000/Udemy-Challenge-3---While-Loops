import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
while guess != answer:
    if guess == 0:
        print("Game Ended")
        break
    if guess < answer:
        print("Please guess higher!")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
if guess == answer:
    print("Well done, you guessed it")




import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = 0    # initializes to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game Over!")
        break
    if guess < answer:
        print("Please guess higher!")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it!")