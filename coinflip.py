import random
#Variable counters
win_count = 0
lose_count = 0
while True:
    cp_flip = random.choice(['heads','tails'])
    
    user_guess = input('Write h for heads and t for tails:\n')
    
    if user_guess == 'h':
        user_guess = 'heads'
    elif user_guess =='t':
        user_guess = 'tails'
    else:
        print('Please enter a value')
    print(f'You guessed {user_guess}, and the computer tossed a.....{cp_flip}')
    if user_guess == cp_flip:
        print('You won!')
        win_count +=1
    elif not user_guess == cp_flip:
        print('Nice try..but you lost')
        lose_count +=1
    else:
        pass
    print(f'You won {win_count} times\n',f'You lost {lose_count} times')
