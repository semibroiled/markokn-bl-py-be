#leap year function

def is_leap(year):

    year = int(year)

    if (year%400 == 0) or (year%100 != 0 and year%4 == 0):
        return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year'

def check_prime(num):

    num = int(num)

    if num<=1:
        return False
    for divisors in range(2, num-1):
        if num%divisors == 0:
            return False
    return True

def prime_range( end,start = 0):

    num_range = list(range(int(start), int(end)))
    lst = []

    for i, num in enumerate(num_range):
        
        if check_prime(num):
            lst.append(num)

    return lst



while True:

    x = input('Enter: ')
    if x=='':
        break
    print(prime_range(x))

help(round)
