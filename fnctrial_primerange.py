def prime_range( end,start = 0):

    num_range = list(range(int(start), int(end)))
    lst = []
    x= None
    for i, num in enumerate(num_range):
        
        if not num<=1:
            for divisors in range(2, num):
                if num%divisors == 0:
                    break
            else:
               lst.append(num)
       
    return lst
#UPDATE. Woek! line 12 else and line 12 break was the 
#secre sauce! 
#Really ingenious placements here

while True:

    x = input('Enter: ')
    print(prime_range(x))
    if x=='':
        break


    # i cant get this to work in a single function
    # num checks it singularly so it works
    #with the first one 
    # but i dont know how to do it all at once