age = int(input('How old are you? '))

country = input('Which country are you from? ')

if age >= 18:
    print('You\'re an adult')

    if country == ('de' or 'en' or'us'):
        print('and you can drink legally!')
    else:
        print('I don\'t know about the laws in that country')
else:
    print('You\'re a minor. You can\'t drink legally.')
    
