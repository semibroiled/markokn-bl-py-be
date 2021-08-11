idlst = [{'name': 'Alice', 'password': 'asdf'}, 
        {'name': 'Arnold', 'password': 'awfweq'}, 
        {'name': 'Bibity', 'password': 'Also'}
]
#try to match an username entry with my idlst

while True:
    username = input('Enter username or press enter to exit:\n')
    user = None
    for pot_user in idlst:
        if username == pot_user['name']:
            user = pot_user
        elif username == '':
            break
    if  user or username == '':
        break
    else:
        print('No such user in system. Try again')    

while True:
    password = input('Enter password or enter to exit:\n')
    if password == user['password']:
        print('Login Succesful!')
        break
    elif password == '':
        break
    else:
        print('Password incorrect, try again')

#Works just fine