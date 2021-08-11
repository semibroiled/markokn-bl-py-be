while True:
    x = input('Write a number: ')
    x = int(x)
    
    op = input('Write and operation symbol: ')
    
    y = input('Write a second number: ')
    y=int(y)
    print(f'You asked for: {x} {op} {y}')

    if op == '+' or 'add' in op :
        print(f'The sum is {x+y}.')
    elif op == ('/') or 'div' in op:
        print(f'The division gives {x/y}')
    elif op == ('-') or 'sub' in op:
        print(f'The difference gives {x-y}')
    elif op=='x' or op=='*' or 'multi' in op:
        print(f'The product is {x*y}')
    else:
        print('I don\' know the operation')
    choice = input('Do you want to continue? Press enter to skip: ')
    if 'ye' in choice:
        break
    else:
        pass
