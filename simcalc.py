lst_calc = []

while True:
    save = { 'x-Value': 0,
             'y-Value': 0,
             'Operation':'choose',
             'Result': 0}
    
    x= int(input('Type in x value: '))
    save['x-Value']= x
    op = input('Type in operation: ')
    save['Operation'] = op
    y= int(input('Type in y value: '))
    save['y-Value'] = y
    

    if op == '+' or op =='sum':
        res = x+y
        save['Result'] = res
        lst_calc.append(save)
    
    elif op == '-' or op == 'diff':
        res = x-y
        save['Result'] = res
        lst_calc.append(save)
    
    elif op == '*' or op == 'multiply':
        res=x*y
        save['Result'] = res
        lst_calc.append(save)
    
    elif op == '/' or op == 'divide':
        res = x/y
        save['Result'] = res
        lst_calc.append(save)
    print(lst_calc)