while True:
    userinput = input('Would you like the iterative approach, sir? y/n \n')
    if userinput == 'y':
        x = input('Psst. Whadisurname? \n')
        y = x.split()
        length = 0
        for i in x:
            length+=1
        print(f'Your name is {length - len(y) +1} letters long')
    else:
        x = input('Psst. Whats your name bro? \n')
        y = len(x.split()) 
        print('Your name is ' + str(len(x)-y+1) +' letters long.') 

#my limitation is: I couldnt ignore the spaces directly so
#I had to take a roundabout mathematical way
#but if spacing convention is not proper this breaks down
#i guess there is a way to go out ignoring spaces by using 
#for and if combinations
# saying that for for everyy == space the length is subtracted 
#or sum shit like that
#would be interesting to try
