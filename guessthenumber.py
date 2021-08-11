import random

num = int(input('input any integer:\n'))



while True:
    
    guess = random.randint(0, num*10)
    
    if guess == num:
        print(f'Found a match for {num}, it\'s {guess}')
        break
    else:
        print(f'{guess} wasn\'t {num}')


