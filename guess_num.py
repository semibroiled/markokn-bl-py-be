import random
x = int(input('Type any number within 5 digits:\n'))
guess = random.randint(0,99999)
while not x == guess:
    guess = random.randint(0,99999)
    print(guess)
    if x == guess:
        print(f'I\'ve guessed {x} correctly')