#21 April 2021

#Practice docstrings with a function

def fib(number): 
    '''This function returns a fibonacci sequence in a list
        number must be a positive integer
        '''
    # Above is docstring as recalled with help(functionname)
    
    f_0 = 0
    f_1 = 1

    fibonacci = [f_0, f_1]

    for i in range(number - 2):
        f_next = f_0 + f_1

        fibonacci.append(f_next)

        f_0=f_1
        f_1=f_next
    
    print(fibonacci)

'''while True:
    x= input('provide a number:\n')

    if x == '':
        break # Escape code from while loop

    fib(int(x)) '''

help(fib)



