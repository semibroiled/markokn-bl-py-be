idlst = [ {'name': 'Alice', 'password': 'asdf'}, 
        {'name': 'Arnold', 'password': 'awfweq'}, 
        {'name': 'Bibity', 'password': 'Also'}
]


while True : 
    username = input('Please enter your username:\n')
    user = None
    for potential_user in idlst:
        if username == potential_user['name']:
            
            password = input('Please enter your password:\n')
            
            if password == potential_user['password']:
                user = potential_user
                print(f'Logged in as {username}!')
                break
            else:

                break
    if user:
        break    
    else:
            
        print('Try again. Wrong Username or Password')   

# my ansatz was flawed
#i tried to get it done in one loop
#marko used one loop to match user and get the user out
#then he checked the password against that user 
#much simpler and more effective
#think global in terms of the problem and dont tunnel vision


#Update. Got it to work in one while loop! else at ennd without break was key to this. although functionality is a little different than the aufgabestellung. this is neat in its own regards