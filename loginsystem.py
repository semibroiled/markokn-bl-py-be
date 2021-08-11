#Generate Dictionary of Usernames and Passwords

idkey = []

while True:
    x= None
    
    id = { 'name': 'name',
            'password': 'password'}
    
    id['name']=input('Type in an username:\n')
    id['password']=input('Type in a secure password:\n')
    
    idkey.append(id)
    
    choice = input('Press enter to continue or enter \'q\' to exit:\n')
   
    if choice == '':
        pass
    elif choice == 'q':
        x = choice
    if x:
        break

print(idkey)

#I didnt use a while here before. best to use it for 
#seamlessly tying in entries i guess
while True :
    exit = None
    
    username = input('Please enter your username:\n')

    for user in idkey:
        if username == user['name']:
            
            password = input('Please enter your password:\n')
            
            if password == user['password']:
                exit = 1
                print(f'Logged in as {username}')
                break
    if exit:
        break
    else:
         print('Wrong username or password. Try Again? y/n\n')
         x = input()
    if x == 'n':
        pass
    elif x=='y':
        exit = 1
    if exit:
        break
# my ansatz was flawed
#i tried to get it done in one loop
#marko used one loop to match user and get the user out
#then he checked the password against that user 
#much simpler and more effective
#think global in terms of the problem and dont tunnel vision


#Not so bad. Deffo an improvement
#aLthough there is some redundancy ging on here. Defnitely 
#makes sense to user the first part for a different program
#and saving it in a filesystem and comparing things to that
