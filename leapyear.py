
while True:
    year_inspect = int(input('Provide a year: '))

    div_4 = year_inspect%4
    div_100 = year_inspect%100
    div_400 = year_inspect%400
    
    if div_4 == 0:
        
        if div_100 == 0:

            if div_400 == 0:
                print( str(year_inspect)+' is a leap year.')
            
            else:
                print( str(year_inspect)+' is a not leap year.')
        else:
            print( str(year_inspect)+' is a leap year.')
    else:
        print( str(year_inspect)+' is not a leap year.')